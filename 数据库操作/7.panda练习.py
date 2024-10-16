import numpy as np
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar

# 时间序列
time_range = pd.date_range('20190101', '20211231')
# print(len(time_range))
#水果和用户
fruits = ["香蕉","苹果","葡萄","橙子","哈密瓜","芭乐","梨","桃子"]
fruit_list = np.random.choice(fruits,len(time_range))
# print(fruit_list)

names = ["Mike" ,"John" ,"Tom" ,"xiaoming","Jimmy","Lym","Michk"]
name_list = np.random.choice(names,len(time_range))
# print(name_list)
# 3、生成订单数据
order = pd.DataFrame({
    "time":time_range,  # 下单时间
    "fruit":fruit_list,  # 水果名称
    "name":name_list,  # 顾客名
    # 购买量
    "kilogram":np.random.choice(list(range(50,100)), size=len(time_range),replace=True)
})

# print(order)
# 4、生成水果的信息数据
infortmation = pd.DataFrame({
    "fruit":fruits,
    "price":[3.8, 8.9, 12.8, 6.8, 15.8, 4.9, 5.8, 7],
    "region":["华南","华北","西北","华中","西北","华南","华北","华中"]
})

# 5、数据合并
df =pd.merge(order, infortmation, how="outer").sort_values('time').reset_index(drop=True)
# print(df)

df['amount'] = df['price'] * df['kilogram']
# print(df.head(5))

df['year'] = df['time'].dt.year
df['month'] = df['time'].dt.month
df['year_month']=df['time'].dt.strftime('%Y%m')
# print(df.head(5))
# print(df.dtypes)

# 分年月统计销量
df1 = df.groupby(["year_month"])["kilogram"].sum().reset_index()
# print(list(df1['year_month'].values))
# print(df1["kilogram"].values.tolist())
# c = (
#     Bar()
#     .add_xaxis(
#         list(df1['year_month'].values)
#     )
#     .add_yaxis("year_month", df1["kilogram"].values.tolist())
#     .set_global_opts(
#         xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
#         title_opts=opts.TitleOpts(title="分年月统计并展示", subtitle=""),
#     )
#     .render("bar_rotate_xaxis_label.html")
# )
# 2019-2021销售额走势
df2 = df.groupby(['year_month'])["amount"].sum().reset_index()
# print(df2)
# import pyecharts.options as opts
# from pyecharts.charts import Line
#
# x_data = df2['year_month'].values.tolist()
# y_data = df2['amount'].values.tolist()
#
#
# (
#     Line()
#     .set_global_opts(
#         tooltip_opts=opts.TooltipOpts(is_show=False),
#         xaxis_opts=opts.AxisOpts(type_="category"),
#         yaxis_opts=opts.AxisOpts(
#             type_="value",
#             axistick_opts=opts.AxisTickOpts(is_show=True),
#             splitline_opts=opts.SplitLineOpts(is_show=True),
#         ),
#     )
#     .add_xaxis(xaxis_data=x_data)
#     .add_yaxis(
#         series_name="",
#         y_axis=y_data,
#         symbol="emptyCircle",
#         is_symbol_show=True,
#         label_opts=opts.LabelOpts(is_show=False),
#     )
#     .render("basic_line_chart.html")
# )
# 年度销量、销售额和平均销售额
df3 = df.groupby(['year']).agg({'kilogram':'sum','amount':'sum'}).reset_index()
print(df3.dtypes)
df['mean_amount']=df['amount']/df['kilogram']
# print(df)
df3["year"] = df3["year"].astype(str)
df3["amount"] = df3["amount"].apply(lambda x: round(x,2))
print(df3)
print(df3.dtypes)

import pandas as pd

person = {
  "name": ['Google', 'Runoob' , 'Taobao'],
  "age": [50, 40, 12345]    # 12345 年龄数据是错误的
}

df = pd.DataFrame(person)

for x in df.index:
  if df.loc[x, "age"] > 120:
    df.drop(x, inplace = True)

print(df.to_string())
