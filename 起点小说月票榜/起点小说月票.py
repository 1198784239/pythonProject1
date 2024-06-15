import requests
from lxml import etree
import openpyxl
import os

info = []
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
        "Cookie": '_yep_uuid=42ed399c-2a57-2eb4-dfea-fd7063dbc88d; e1=%7B%22l6%22%3A%22%22%2C%22l1%22%3A5%2C%22pid%22%3A%22qd_P_rank%22%2C%22eid%22%3A%22qd_C40%22%7D; e2=%7B%22l6%22%3A%22%22%2C%22l1%22%3A5%2C%22pid%22%3A%22qd_P_rank%22%2C%22eid%22%3A%22qd_C40%22%7D; '
                  'newstatisticUUID=1662801251_493794012; supportwebp=true; supportWebp=true; navWelfareTime=1686143265622; _csrfToken=SZxQu6yP9AeHvgk8Nxwz73ZmZogWNSyUkmCPbFx4; fu=1203045347; e2=; e1=%7B%22l6%22%3A%22%22%2C%22l1%22%3A3%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A18%22%7D; traffic_utm_referer=https%3A//cn.bing.com/; w_tsfp=ltvgWVEE2utBvS0Q6K/'
                  'onUmsEzs7Z2R7xFw0D+M9Os09BaQoVp+F0o9yt9fldCyCt5Mxutrd9MVxYnGEUd8hfBEQRcyXb5tH1VPHx8NlntdKRQJtA8+NWlFKKrNxvTZBeGlacUayjGp/INBAybBl3g0E4Scg37ZlCa8hbMFbixsAqOPFm/97DxvSliPXAHGHM3wLc+6C6rgv8LlSgX2NuwDuLi1mH6gTghvNl3VOUmop8xG7dOldNRytI86vWO0wrTPzwjn3apCs2RYj4VA3sB49EMnmim2ffC0HZVZ5b0q2hrh3KqaiMO8t6jdLXqpISwgQrQ4btOcwq0NNWH66MmfC'
    }
for page in range(1,2):
    url = f'https://www.qidian.com/rank/yuepiao/year2024-month06-page{page}/'
    res = requests.get(url,headers=headers)


    lxml=etree.HTML(res.text)
    for i in range(1,21):

        num = lxml.xpath(f'//*[@id="book-img-text"]/ul/li{[i]}/div[1]/span/text()')[0]
        img1 = lxml.xpath(f'//*[@id="book-img-text"]/ul/li{[i]}/div[1]/a/img/@src')[0]
        title = lxml.xpath(f'//*[@id="book-img-text"]/ul/li{[i]}/div[2]/h2/a/text()')[0]
        aurth = lxml.xpath(f'//*[@id="book-img-text"]/ul/li{[i]}/div[2]/p[1]/a[1]/text()')[0]
        leixin = lxml.xpath(f'//*[@id="book-img-text"]/ul/li{[i]}/div[2]/p[1]/a[2]/text()')[0]
        content = lxml.xpath(f'//*[@id="book-img-text"]/ul/li{[i]}/div[2]/p[2]/text()')[0]
        content1 = lxml.xpath(f'//*[@id="book-img-text"]/ul/li{[i]}/div[2]/p[3]/a/text()')[0]
        time = lxml.xpath(f'//*[@id="book-img-text"]/ul/li{[i]}/div[2]/p[3]/span/text()')[0]
        img= "https:"+img1+'.webp'
        # print(img,title,aurth,leixin,content,content1,time)
        info.append([num,img,title,aurth,leixin,content,content1,time])
print(info)
    # print(f'第{page}页爬取完毕'+'-'*100)


root = "C://Users//李克聪//PycharmProjects//pythonProject1//起点小说月票榜/图片/"
workbook = openpyxl.Workbook()
worksheet = workbook.active
for i in info:
    worksheet.append(i)
    resimg = requests.get(i[1], headers=headers)
    name = root + i[2]+'.webp'
    with open(name,'wb') as f:
        f.write(resimg.content)
        f.close()
        print(name+'已经保存成功！')
workbook.save('起点.xls')
print(f'第{page}页保存完毕' + '-' * 100)

