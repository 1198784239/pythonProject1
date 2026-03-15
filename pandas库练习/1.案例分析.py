import pandas as pd
import random


products =["笔记本电脑","键盘","鼠标","硬盘","显卡","显示器"]
names = ['小李','小城',"小城","小王","小孩"]

for i in range(10):
    data = {
        "销售人":[random.choice(names) for j in range(10)],
        "产品":[random.choice(products) for j in range(10)]
    }
    df = pd.DataFrame(data)
    df.to_excel(f'C:/Users/李克聪/PycharmProjects/pythonProject1/pandas库练习/文件/产品{i}.xlsx',index=False)