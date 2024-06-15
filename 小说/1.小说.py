import csv

import requests
from lxml import etree

def get_html():
    list = []
    start = int(input('请输入第几章：'))
    end = int(input('到第几章：'))
    cha = 48 + start
    enda = 49 + end
    for page in range(cha,enda):
        for num in range(1,3):
            url =f'https://s.laishu88.org/two/28161/2040877{page}_{num}.html'
            response = requests.get(url)
            # print(response.text)
            Html = etree.HTML(response.text)
            title =Html.xpath('//*[@id="nr_title_GbJ94B"]/text()')
            content =Html.xpath('//*[@id="ccc"]/text()')
            # new_lst = ''.join(str(i) for i in content)
            list.append(content)
            # print(new_lst)
            print('--------------------------------结束一页----------------------------------')
        print('--------------------------------结束一章----------------------------------')
    print('--------------------------------完成----------------------------------')
    print(list)
    return list

def Save_csv(list):
    with open('xinshu.csv','w',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(list[1])

if __name__ == '__main__':
    get_html()
    Save_csv(list)