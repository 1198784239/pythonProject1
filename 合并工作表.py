import pandas as pd
import os
import xlwings as xw
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

# 初始化tkinter并隐藏主窗口，纯弹窗操作
root = tk.Tk()
root.withdraw()
# 设置弹窗中文显示正常，不乱码
root.encoding = 'utf-8'


def merge_excel_files(save_name='合并后的表格.xlsx'):
    """
    Excel表格批量合并【全弹窗可视化终极版】
    ✅ 全程鼠标操作，无命令行输入、无黑窗口、无代码修改
    ✅ 核心规则：第一张表完整保留表头，其他表自动跳过表头，所有表统一删表尾
    ✅ 兼容xls/xlsx、中文路径、中文文件名、带括号/空格的文件，自动过滤空行
    """
    # ============ 弹窗1：可视化选择要合并的表格文件夹（鼠标点选，最自然） ============
    folder_path = filedialog.askdirectory(title="📂 请选择【需要合并的Excel表格】所在文件夹")
    if not folder_path:
        messagebox.showinfo("提示", "未选择文件夹，程序已退出！")
        return

    # 筛选所有xls/xlsx格式文件，兼容大小写后缀
    excel_suffix = ['.xls', '.xlsx', '.XLS', '.XLSX']
    excel_files = [f for f in os.listdir(folder_path)
                   if any(f.endswith(suffix) for suffix in excel_suffix) and f != save_name]

    if not excel_files:
        messagebox.showwarning("警告", f"在选中的文件夹中，未找到任何.xls或.xlsx格式的表格文件！")
        return

    # ============ 弹窗2：输入【表头行数】弹窗（带提示+默认值2，双表头直接用） ============
    while True:
        head_input = simpledialog.askstring(
            title="表头行数设置",
            prompt="📌 请输入表格的【表头总行数】\n例：双表头填2 | 单表头填1 | 无表头填0\n(默认值：2，直接回车即可使用)",
            initialvalue="2"  # 默认值，双击可修改
        )
        # 点击取消按钮
        if head_input is None:
            messagebox.showinfo("提示", "操作已取消，程序退出！")
            return
        # 输入为空则用默认值2
        if head_input.strip() == "":
            head_rows = 2
            break
        # 校验是否为有效数字
        try:
            head_rows = int(head_input)
            if head_rows >= 0:
                break
            else:
                messagebox.showerror("输入错误", "❌ 请输入【0及以上的纯数字】，比如0、1、2！")
        except ValueError:
            messagebox.showerror("输入错误", "❌ 只能输入纯数字，比如0、1、2，不能输入文字/符号！")

    # ============ 弹窗3：输入【删除表尾行数】弹窗（带提示+默认值2，直接用） ============
    while True:
        tail_input = simpledialog.askstring(
            title="表尾行数设置",
            prompt="📌 请输入每张表要【删除的末尾行数】\n例：删2行合计填2 | 不删填0\n(默认值：2，直接回车即可使用)",
            initialvalue="2"  # 默认值，双击可修改
        )
        # 点击取消按钮
        if tail_input is None:
            messagebox.showinfo("提示", "操作已取消，程序退出！")
            return
        # 输入为空则用默认值2
        if tail_input.strip() == "":
            tail_rows = 2
            break
        # 校验是否为有效数字
        try:
            tail_rows = int(tail_input)
            if tail_rows >= 0:
                break
            else:
                messagebox.showerror("输入错误", "❌ 请输入【0及以上的纯数字】，比如0、1、2！")
        except ValueError:
            messagebox.showerror("输入错误", "❌ 只能输入纯数字，比如0、1、2，不能输入文字/符号！")

    # 开始处理表格数据
    all_merge_data = []
    success_count = 0
    fail_files = []

    for file_idx, file_name in enumerate(excel_files):
        file_full_path = os.path.join(folder_path, file_name)
        try:
            # 万能读取引擎，兼容xls/xlsx所有格式，无报错
            app = xw.App(visible=False, add_book=False)
            app.display_alerts = False
            app.screen_updating = False
            wb = app.books.open(file_full_path)
            ws = wb.sheets[0]  # 默认读取第一个工作表，如需指定sheet：ws = wb.sheets["数据"]
            df = pd.DataFrame(ws.used_range.value)
            wb.close()
            app.quit()

            # 过滤空行，数据整洁
            df = df.dropna(how='all').reset_index(drop=True)
            if len(df) == 0:
                fail_files.append(f"{file_name}（无有效数据）")
                continue

            # 对所有表格生效：删除指定行数的表尾
            if tail_rows > 0 and len(df) > tail_rows:
                df = df.iloc[:-tail_rows]

            # ============ 核心规则：精准匹配你的需求 ============
            if file_idx == 0:
                # ✅ 第一张表：完整保留【所有表头+标题+全部数据】，一行不删
                all_merge_data.append(df)
                success_count += 1
            else:
                # ✅ 第2-N张表：自动跳过表头行数，只追加纯数据行，无重复表头
                if len(df) > head_rows:
                    data_only = df.iloc[head_rows:]
                    data_only = data_only.dropna(how='all')
                    all_merge_data.append(data_only)
                    success_count += 1
                else:
                    fail_files.append(f"{file_name}（数据行数不足，跳过表头后无数据）")

        except Exception as e:
            fail_files.append(f"{file_name}（读取失败：{str(e)}）")
            continue

    # 合并数据并保存
    if all_merge_data:
        final_df = pd.concat(all_merge_data, ignore_index=True)
        save_path = os.path.join(folder_path, save_name)
        final_df.to_excel(save_path, index=False, header=False)

        # 合并成功弹窗提示
        tip_msg = f"🎉 合并成功！\n✅ 成功处理 {success_count} 个表格文件\n✅ 合并后总数据行数：{len(final_df)}\n✅ 合并文件已保存至：\n{save_path}"
        if fail_files:
            tip_msg += f"\n⚠️  以下文件处理失败/跳过：\n{chr(10).join(fail_files)}"
        messagebox.showinfo("合并完成", tip_msg)
    else:
        messagebox.showwarning("合并失败", "❌ 本次合并无任何有效数据，请检查表格文件！")


# 程序主入口
if __name__ == "__main__":
    merge_excel_files()