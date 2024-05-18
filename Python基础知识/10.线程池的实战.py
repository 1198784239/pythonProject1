import time

from lxml import etree
import requests
from concurrent.futures import thread, ThreadPoolExecutor


def get_html():
    proxy ={'http':'110.43.213.99:443'}
    url ='https://desk.zol.com.cn/dongman/'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
    }
    response = requests.get(url,verify=False,proxies=proxy,headers=headers)
    response.encoding='gb2312'
    res = response.text
    # print(res)
    lxml = etree.HTML(res)
    # print(lxml)
    start_time = time.time()
    # 创建线程池
    with ThreadPoolExecutor(max_workers=100) as executor:
        List = []
        for i in range(1, 100):
            try:
                title = lxml.xpath(f'//div[1]/ul[1]/li{[i]}/a/span/em/text()')
                scr = lxml.xpath(f'//div[1]/ul[1]/li{[i]}/a/img/@src')
                list = [title[0], scr[0]]
                List.append(list)
                print(scr)
                #提交线程池submit(任务，传递的参数，参数）
                executor.submit(down_img,scr,title)
                #如果保错跳过
            except Exception as e:
                pass
        print(List)
    #线程结束提交完成
    end_time = time.time()
    print('all over')
    print(end_time - start_time)




def down_img(scr,title):
    img = scr[0]
    # print(img)
    # 请求图片地址
    download = requests.get(img,verify=False)
    with open(f'img/{title[0]}.jpg', 'wb') as f:
        f.write(download.content)
    print(title[0],'下载完毕')

if __name__ == '__main__':
    HTML = get_html()
    down_img(HTML)