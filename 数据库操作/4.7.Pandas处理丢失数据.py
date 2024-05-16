import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=list('ABCD'))
df.iloc[2,3] = np.nan
df.iloc[4,2] = np.nan
print(df)
# 使用dropna（）函数去掉NaN的行或列
print(df.dropna(axis=0,how='any'))#0对行进行操作 1对列进行操作 any:只要存在NaN即可drop掉 all:必须全部是NaN才可drop
# 使用fillna（）函数替换NaN值
print(df.fillna(value=1))
# 使用isnull()函数判断数据是否丢失
# print(df.isin(df))
#
# # --------8.Pandas导入导出---------
# dates = pd.read_csv('//')
# dates.to_excel('')

# ------------append添加数据-----------
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
s1 = pd.Series([1,2,3,4], index=['a','b','c','d'])
print(s1)
res =df1._append(df2,ignore_index=True)
print(res)
res =df1._append(s1,ignore_index=True)
print(res)
