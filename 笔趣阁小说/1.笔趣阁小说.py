import requests
from bs4 import BeautifulSoup
url = 'https://www.bqguu.cc/top/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
"Cookie":'log=; v=A3Pn2vNiEQZBw90G2nwpuDtOAnyYqAWVwT5LuSUQzAbIbJ1irXiXutEM29o2'
           }
response = requests.get(url, headers=headers,verify=False)

dic ={
    "Tiltle":'',
    "Name":'',
}
list = []
try:
    # 解析数据
    Soup = BeautifulSoup(response.text,'html.parser')
    # 获取页面所有h2标签里主小说名
    title1 = Soup.find_all('h2')
    for title in title1:
        # 遍历其数据
        list.append( [title.get_text()])
        name1 = Soup.find_all('div', {"class": "blocks"})
        # 获取小说的名字
        for name in name1:
            for Name1 in name.find_all('li'):
                name2 = Name1.find('a').get_text()
                src = Name1.find('a').attrs['href']
                list.append([name2])
                list.append(src)
                str = 'https://www.bqguu.cc/'+src
                print(str)
                res = requests.get(str, headers=headers,verify=False)
                soup = BeautifulSoup(res.text,'html.parser')
                author = soup.find('dd')
                print(author.get_text())
    # print(list)
except Exception as e:
    pass