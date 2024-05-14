from lxml import etree
import requests
from pip._internal.utils.misc import tabulate


def get_html():
    url = 'https://www.douguo.com/'
    response = requests.get(url)
    res = response.text
    return res

def get_etree(res):
    data = []
    list = etree.HTML(res)
    for i in range(1,9):
        img = list.xpath(f'//ul[@class="recipe-list clearfix"]/li[{i}]/a[@class="cover br8"]/img/@src')
        title = list.xpath(f'//ul[@class="recipe-list clearfix"]/li[{i}]/div/a[@class="name text-lips"]/text()')
        aurth = list.xpath(f'//ul[@class="recipe-list clearfix"]/li[{i}]/div/p[@class="author text-lips"]/a[1]/text()')
        data.append(img)
        data.append(title)
        data.append(aurth)
        # result = tabulate([[title, aurth]], headers=['Name', 'Author'], tablefmt='orgtbl')
        # print(result)
    print(data)
    return data

def save_csv(data):
    a = str(data)
    print(type(a))
    print(a)
    with open('foods.csv','w',encoding='utf-8') as f:
        f.write(a)
if __name__ == '__main__':
    get_html()
    s = get_etree(get_html())
    save_csv(s)