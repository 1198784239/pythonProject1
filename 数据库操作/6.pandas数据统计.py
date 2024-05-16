import pandas as pd
import numpy as np


data ={'user':['user1','user1','user1','user2','user2','user3','user2'],
                        '交易类型':[0,0,1,1,1,1,0],
                        '消费金额':[12,12,12,15,15,17,20],
                        '消费数量':[2,2,2,5,5,7,2]}
df = pd.DataFrame(data)
print(df)
a= df.groupby(['user']).sum()
print(a)


df = pd.DataFrame(data={'user':['user1','user1','user1','user2','user2','user3','user2'],
                        '交易类型':[0,0,1,1,1,1,0],
                        '消费金额':[12,12,12,15,15,17,20],
                        '消费数量':[2,2,2,5,5,7,2]})
print(df)
print(df.groupby(['user']).sum())
print(df.groupby(['user']).mean())
print(df.groupby(['user'])['交易类型'].mean())

