import requests
from lxml import etree

url  = 'http://spiderbuf.cn/h02/'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'}
r = requests.get(url, headers=header)
# print(r.text)
Data = []
Data1 = []
Html  =etree.HTML(r.text)
content = Html.xpath('/html/body/div[2]/div[@style="margin-top: 10px;"]')
# print(content)

i = 1
for div in content:
    dic = {
        'img': "",
        'title': "",
        'num': "",
        'author': "",
        'time': "",
        'cou': "",
    }
    if i % 2 ==0:
        # for num in  range(1,8):
        cou = div.xpath('//div[3]/div/text()')[0]
        Data1.append(cou)
    else:
        img = div.xpath('./div/div[1]/img/@src')[0].split('/')[-1]
        title = div.xpath('./div[1]/h2/text()')[0]
        num = div.xpath('//div[2]/div/div[2]/span[1]/following::text()[1]')[0]
        author = div.xpath('./div[1]/div[2]/span[2]/span[2]/text()')[0]
        time= div.xpath('./div[1]/div[2]/span[9]/span[2]/text()')[0]
        Data.append([img,title,num,time,author])
        # Data.append(img)
        # Data.append(title)
        # Data.append(num)
        # Data.append(time)
        # Data.append(author)

    i += 1
# print(Data)
# print(Data1)
h=[item for sublist in zip(Data,Data1) for item in sublist]
print(h)
