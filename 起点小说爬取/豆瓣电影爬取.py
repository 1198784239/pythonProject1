import requests
from lxml import etree
import re

url="https://movie.douban.com/top250"
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}

allMovieList=[]
flag = True
while flag:
    html = requests.get(url, headers=header).text
    list = etree.HTML(html)
    lis = list.xpath('//ol[@class="grid_view"]/li')
    for oneSelector in lis:
        name = oneSelector.xpath("div/div[2]/div[1]/a/span[1]/text()")[0]
        score = oneSelector.xpath("div/div[2]/div[2]/div/span[2]/text()")[0]
        people = oneSelector.xpath("div/div[2]/div[2]/div/span[4]/text()")[0]
        people = re.findall("(.*?)人评价",people)[0]
        oneMovieList = [name,score,people]
        allMovieList.append(oneMovieList)
    #获取下一页地址
    try:
        next_url = list.xpath('//span[@class="next"]/a/@href')[0]
        if next_url:
            url = "https://movie.douban.com/top250"+ next_url
    except:
        flag = False
print(allMovieList)


