import pandas as pd
from pulp import LpProblem, LpVariable, LpInteger, LpMinimize, lpSum, LpStatus
import numpy as np


def find_all_matching_combinations(file_path=None, target_amount=0, data_col="原始金额",
                                   export_path="所有财务凑数结果.xlsx", max_combinations=10):
    """
    财务凑数：枚举所有与目标金额最接近的凑数组合，支持Excel导入/导出
    :param file_path: Excel文件路径（None则生成测试数据）
    :param target_amount: 目标凑数金额
    :param data_col: 明细金额列名
    :param export_path: 结果导出Excel路径
    :param max_combinations: 最大枚举组合数（避免数据量过大）
    """
    # 1. 数据加载与清洗
    if file_path:
        df = pd.read_excel(file_path)
        df[data_col] = pd.to_numeric(df[data_col], errors='coerce').fillna(0)
    else:
        # 生成测试数据（模拟财务对账明细）
        df = pd.DataFrame({
            "序号": range(1, 21),
            "原始金额": [125.6, 348.2, 569.8, 78.1, 902.3, 456.7, 231.9, 678.4, 890.1, 102.5,
                         321.8, 543.2, 765.9, 987.3, 111.4, 222.5, 333.6, 444.7, 555.8, 666.9],
            "摘要": ["客户回款", "供应商付款", "服务费收入", "银行手续费", "房租支出",
                     "货款收入", "备用金提现", "结算收入", "工资代发", "杂费收入",
                     "客户回款", "供应商付款", "服务费收入", "银行手续费", "房租支出",
                     "货款收入", "备用金提现", "结算收入", "工资代发", "杂费收入"]
        })

    amount_list = df[data_col].values
    n_rows = len(df)
    all_combinations = []  # 存储所有可行凑数组合
    optimal_diff = None  # 记录最优差值（最小绝对差值）

    # 2. 第一步：找到最优差值（先获取一组最优解，确定最小差值）
    prob = LpProblem("Find_Optimal_Diff", LpMinimize)
    select_vars = [LpVariable(f"select_{i}", cat=LpInteger, lowBound=0, upBound=1) for i in range(n_rows)]
    selected_sum = lpSum([select_vars[i] * amount_list[i] for i in range(n_rows)])
    target_diff = selected_sum - target_amount

    # 辅助变量处理绝对值
    pos_diff = LpVariable("pos_diff", lowBound=0)
    neg_diff = LpVariable("neg_diff", lowBound=0)
    prob += target_diff == pos_diff - neg_diff
    prob += lpSum([pos_diff, neg_diff])  # 最小化绝对值差值

    # 宽松约束，避免偏离过大
    max_possible = sum(amount_list)
    prob += selected_sum <= min(target_amount * 1.5, max_possible)
    prob += selected_sum >= 0

    # 求解最优解，获取最小差值
    solve_status = prob.solve()
    if solve_status != 1:
        print("警告：未找到任何可行凑数组合！")
        return df, pd.DataFrame()

    # 提取最优解结果，计算最优差值
    selected_mask = [int(var.varValue) if (var.varValue is not None and var.varValue > 0.5) else 0 for var in
                     select_vars]
    total_matched = sum(amount_list[i] * selected_mask[i] for i in range(n_rows))
    optimal_diff = abs(total_matched - target_amount)
    print(f"找到最优差值：{optimal_diff:.6f}")

    # 3. 第二步：枚举所有最优解（差值=optimal_diff的所有组合）
    combination_count = 0
    while combination_count < max_combinations:
        # 初始化线性规划问题
        prob = LpProblem(f"Find_Combination_{combination_count + 1}", LpMinimize)
        select_vars = [LpVariable(f"select_{i}", cat=LpInteger, lowBound=0, upBound=1) for i in range(n_rows)]
        selected_sum = lpSum([select_vars[i] * amount_list[i] for i in range(n_rows)])

        # 目标：最小化差值（确保是最优解），同时可以额外优化（如最小化选中笔数）
        target_diff = selected_sum - target_amount
        pos_diff = LpVariable(f"pos_diff_{combination_count}", lowBound=0)
        neg_diff = LpVariable(f"neg_diff_{combination_count}", lowBound=0)
        prob += target_diff == pos_diff - neg_diff
        prob += lpSum([pos_diff, neg_diff]) == optimal_diff  # 强制等于最优差值（筛选所有最优解）

        # 宽松约束
        prob += selected_sum <= min(target_amount * 1.5, max_possible)
        prob += selected_sum >= 0

        # 关键：添加约束，排除已找到的组合（避免重复）
        for existing_comb in all_combinations:
            existing_mask = existing_comb["选中掩码"]
            # 约束：当前组合与已存在组合的差异至少为1（避免重复）
            prob += lpSum([select_vars[i] for i in range(n_rows) if existing_mask[i] == 1]) + \
                    lpSum([(1 - select_vars[i]) for i in range(n_rows) if existing_mask[i] == 0]) >= 1

        # 执行求解
        solve_status = prob.solve()
        if solve_status != 1:
            print(f"已枚举所有可行组合，共找到 {combination_count} 组")
            break

        # 提取当前组合结果
        selected_mask = [int(var.varValue) if (var.varValue is not None and var.varValue > 0.5) else 0 for var in
                         select_vars]
        total_matched = sum(amount_list[i] * selected_mask[i] for i in range(n_rows))
        current_diff = abs(total_matched - target_amount)

        # 验证是否为最优解（避免误差）
        if np.isclose(current_diff, optimal_diff, rtol=1e-6):
            combination_info = {
                "组合编号": combination_count + 1,
                "目标凑数金额": target_amount,
                "实际凑数合计": total_matched,
                "最终差额": total_matched - target_amount,
                "绝对差值": current_diff,
                "选中笔数": sum(selected_mask),
                "选中掩码": selected_mask  # 记录选中状态，用于去重
            }
            all_combinations.append(combination_info)
            combination_count += 1
            print(f"已找到第 {combination_count} 组凑数组合")

    # 4. 处理结果，生成明细与汇总
    if not all_combinations:
        print("未找到任何可行凑数组合！")
        return df, pd.DataFrame()

    # 生成汇总表
    summary_df = pd.DataFrame(all_combinations).drop(columns=["选中掩码"])
    summary_df["凑数状态"] = ["成功（完全匹配）" if np.isclose(row["绝对差值"], 0, rtol=1e-6) else "未完全匹配（最优解）"
                              for _, row in summary_df.iterrows()]

    # 生成明细对照表（包含所有组合的选中状态）
    df_combined = df.copy()
    for comb in all_combinations:
        comb_id = comb["组合编号"]
        selected_mask = comb["选中掩码"]
        df_combined[f"是否选中_组合{comb_id}"] = selected_mask
        df_combined[f"凑数计算_组合{comb_id}"] = df_combined[data_col] * selected_mask

    # 5. 导出所有结果到Excel
    with pd.ExcelWriter(export_path, engine="openpyxl") as writer:
        summary_df.to_excel(writer, sheet_name="所有组合汇总", index=False)
        df_combined.to_excel(writer, sheet_name="组合明细对照", index=False)

    # 打印结果提示
    print("=" * 60)
    print("财务凑数组合枚举完成！")
    print(f"目标金额：{target_amount:.2f}")
    print(f"最优绝对差值：{optimal_diff:.6f}")
    print(f"共找到 {combination_count} 组可行凑数组合")
    print(f"结果已导出至：{export_path}")
    print("=" * 60)

    return df_combined, summary_df


# ---------------------- 运行示例（枚举所有凑数组合）----------------------
if __name__ == "__main__":
    # 自定义参数：枚举所有最优凑数组合
    find_all_matching_combinations(
        target_amount=2024,  # 125.6+348.2+569.8=1043.6（可完全匹配）
        export_path="所有财务凑数组合.xlsx",
        max_combinations=10  # 最多枚举10组组合
    )