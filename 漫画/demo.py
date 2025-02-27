import requests
import re
import os
# 分析网站
#获取每一章数据
dic =[]
headers={
    'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
         }
for num in range(1,11):
    url = f'http://www.mkzhan.com/category/?order=1&is_vip=1&page={num}'
    all_res = requests.get(url,headers=headers).text
    href =re.findall(r'<a class="cover" href="/(.*?)/" target',all_res)
    book =re.findall(r'/" target="_blank">(.*?)</a></p>',all_res)
    books = re.sub(r'\\/:*<>|', '',book[0])
    dic.append(book)
    path = f'data\\{books}'
    if not os.path.exists(path):
        os.makedirs(path)
        for i in href:
            #获取所有章节数据
            chapter = f'https://comic.mkzcdn.com/chapter/v1/?comic_id={i}'
            # 请求数据
            chapter_response = requests.get(url=chapter,headers=headers).json()
            chapter_ids = chapter_response['data']
            for chapter_ide in chapter_ids:
                chapter_id = chapter_ide['chapter_id']
                titles = chapter_ide['title']
                title =re.sub(r'\\/:*<>|','',titles)
                url = f'https://comic.mkzcdn.com/chapter/content/v1/?chapter_id={chapter_id}&comic_id={i}&format=1&quality=1&type=1'
                response = requests.get(url=url, headers=headers).json()
                #获取数据
                data = response['data']['page']
                tiao = 0
                for index in data:
                    image_url = index['image']
                    tiao  += 1
                    # 请求图片地址
                    img_reponse = requests.get(url=image_url,headers=headers).content
                    with open(path + f'\{title}{tiao}张.jpg','wb') as f:
                        f.write(img_reponse)
                            # print(img_reponse)
            print(book)