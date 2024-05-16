import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import PictorialBar
from pyecharts.globals import SymbolType


Content = pd.read_excel('医院名单表.xls')
# print(Content)
Sum = Content.groupby(['省份'])['医院'].count()
# print(Sum)
Index = Sum.index.values[:8]
# 需要修改为加了tolist()方法的，把pandas数据转换为python 列表：--------------------不能直接引用行数据，要转换为列表
Count = Sum.values[:8].tolist()
M = list(Index)
# print([z for z in zip(M, Y)])
# 两个列表值一一对应转化为字典/列表
# print([list(z) for z in zip(M, num)])

c = (
    PictorialBar()
    .add_xaxis(M)
    .add_yaxis(
        "",
        Count,
        label_opts=opts.LabelOpts(is_show=False),
        symbol_size=18,
        symbol_repeat="fixed",
        symbol_offset=[0, 0],
        is_symbol_clip=True,
        symbol=SymbolType.ROUND_RECT,
    )
    .reversal_axis()
    .set_global_opts(
        title_opts=opts.TitleOpts(title="PictorialBar-各省份人口数量（虚假数据）"),
        xaxis_opts=opts.AxisOpts(is_show=False),
        yaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_show=False),
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(opacity=0)
            ),
        ),
    )
    .render("pictorialbar_base.html")
)
