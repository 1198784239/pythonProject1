import pandas as pd

# df = pd.read_json('8.测试文件.js')
# # print(pd)
# # 删除缺失值
# # df = df.dropna()
# # print(df)
# # 用指定的值填充缺失值
# df = df.fillna({'age':20,'score':30})
# # print(df)
# # 重命名列名
# df =df.rename(columns={'age':'年龄','age':'年龄','gender':'性别','score':'成绩'})
# # 按成绩排序
# df = df.sort_values('成绩',ascending=False)
# # 按性别分组并计算平均年龄和成绩
# df1 = df.groupby('性别').agg({'年龄': 'mean', '成绩': 'mean'})
# # print(df1)
# # 选择成绩大于等于90的行，并只保留姓名和成绩两列
# df2 = df.loc[df['成绩']>=90,['name','成绩']]
# # print(df2)
# # 计算每列的基本统计信息
# df3 = df.describe()
# # print(df3)
# # 计算每列的平均值
# df4 =df['成绩'].mean()
# print(df4)
#
# # # 计算每列的中位数
# # median = df.median()
# # print(median)

data = {
    'boshi':['7k-9k','10k-15','1k-3k'],
    'suoshi':['10k-15','6k-8k','2k-3k'],
    'gaozhong':['1k-3k','2k-4k','3k-4k']
}
df = pd.DataFrame(data,index=['1year','2year','3year'])
print(df)
def cut_word(word):
    postion =word.find('-')
    min = int(word[:postion].strip('kK'))
    max = int(word[postion:].strip('kK-'))

    return (min+max)/2
print(cut_word('10k-15'))


import numpy as np
import pandas as pd

df=pd.DataFrame(np.random.randn(4,3),columns=list('bde'),index=['utah','ohio','texas','oregon'])
print(df)
f = lambda x:x.max()-x.min()
t1 = df.apply(f)
print(t1)
print(df.duplicated().gaozhong.apply(cut_word))
