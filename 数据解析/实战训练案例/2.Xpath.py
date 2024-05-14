# 导入库
import requests
from bs4 import BeautifulSoup
import bs4
from lxml import etree


# 1. 从网络上获取大学排名网页内容
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
# 2. 提取网页内容中信息到合适的数据结构（二维数组）
# 查看网页源代码，观察并定位到需要爬取内容的标签；
# 使用bs4的查找方法提取所需信息-'排名，学校名称，总分'
def fillUnivList(ulist, html):
    data = etree.HTML(html)
    # print(data)
    for i in range(1,31):
        rank = data.xpath(f'//*[@id="content-box"]/div[2]/table/tbody/tr[{i}]/td[1]/div/text()')[0].replace('\n','').replace(' ','')
        title =data.xpath(f'//*[@id="content-box"]/div[2]/table/tbody/tr[{i}]/td[2]/div/div[2]/div[1]/div/div/a/text()')[0].replace('\n','').replace(' ','')
        leixin =data.xpath(f'//*[@id="content-box"]/div[2]/table/tbody/tr[{i}]/td[2]/div/div[2]/p/text()')[0]
        img =data.xpath(f'//*[@id="content-box"]/div[2]/table/tbody/tr[{i}]/td[2]/div/div[1]/img/@src')[0]
        pro =data.xpath(f'//*[@id="content-box"]/div[2]/table/tbody/tr[{i}]/td[3]/text()')[0].replace('\n','').replace(' ','')
        sum =data.xpath(f'//*[@id="content-box"]/div[2]/table/tbody/tr[{i}]/td[5]/text()')[0].replace('\n','').replace(' ','')
        ulist.append([rank,title,leixin,img,pro,sum])
    print(ulist)
# 3. 利用数据结构展示并输出结果
# 对中英文混排输出问题进行优化:对format()，设定宽度和添加参数chr(12288)
def printUnivList(ulist, num=20):
    pass
# ulist=[]
u_info = [] # 存储爬取结果的容器
url = 'https://www.shanghairanking.cn/rankings/bcur/2024'
html = getHTMLText(url)
fillUnivList(u_info, html) # 爬取
# printUnivList(u_info, num=30) # 打印输出30个信息
