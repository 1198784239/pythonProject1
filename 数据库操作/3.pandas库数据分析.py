import numpy as np
import pandas as pd

# Pandas数据结构
# 1.Series
s = pd.Series([1, 2, 3, 4, 5])
# print(s) 索引在左边 值在右边
# 2.DataFrame 可以看成由Series组成的字典。
dates=pd.date_range('20180310',periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
# print(df)
# # 类型
# print(df.dtypes)
# # 打印A列
# print(df['A'])
# # 打印索引
# print(df.index)
# # 打印列
# print(df.columns)
# # 打印值
# print(df.values)
# 打印数字总结
# print(df.describe())

# 5.---------------Pandas选择数据----------
# print(df.A)/df['A']

# 切片选择
# print(df[0:3])/df['20180310':'20180314']两次进行选择 第一次切片选择 第二次按照筛选条件进行选择

# 根据标签loc-行标签进行选择数据
# print(df.loc['2018-03-10',['A']])#按照行标签进行选择 精确选择

# 根据序列iloc-行号进行选择数据
# print(df.iloc[3,1])#输出第三行第一列的数据 从0开始
# print(df.iloc[3:5,0:1])
# print(df.iloc[[1,2,4],[0,2]])#进行不连续筛选

# # 根据判断筛选
# print(df[df.A>0])#筛选出df.A大于0的元素 布尔条件筛选

# -----------------Pandas设置数据-----------
date = pd.date_range('20180310', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)), index=date, columns=['A', 'B', 'C', 'D'])
print(df)
# # 单点设置
# # df.iloc[1,1] = 10/df.loc['2018-03-11', 'B']=10
# # print(df)
# # 根据条件设置
# df[df.B>20]=100
# print(df)
# # 根据行或列设置  设置为空
df['E'] = np.nan
# print(df)
# # 添加数据
df['F'] =pd.Series([1,2,3,4,5,6],index=pd.date_range('20180310', periods=6))
print(df)

