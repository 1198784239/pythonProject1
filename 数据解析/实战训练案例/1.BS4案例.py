import bs4
from bs4 import BeautifulSoup
import requests


def get_html(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
    }
    response =requests.get(url,headers=headers).content.decode('utf-8')
    return response
    # print(response)
def get_Soup(response,data):
    Soup = BeautifulSoup(response,'html.parser')
    titles = Soup.tbody.children
    for tr in Soup.find('tbody').children:  # 先检索到tbody标签
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')  # 查询tr中的td标签，等价于tr.find_all('td')
            # 新版的排名封装在a标签中，所以这里需要具体到查找属性为'name-cn'的a标签并存储其字符串，即大学的中文名称
            a = tr('a', 'name-cn')
            data.append([tds[0].string.strip(), a[0].string.strip(), tds[2].text.strip(), tds[4].string.strip()])
            print(data)
    # for i,title in enumerate(titles):
    #     # print(type(title))
    #     rank = title.div.text.replace('\n                        ','').replace(' ','')
    #     name = title.a.text
    #     zhonglei = title.p.text
    #     list = title('a','name-cn')
    #     print(title[4])
    #     # Place=province.text.replace(' ','').replace('\n','')
        # leixin = title.td(3).text
        # data.append(rank)
        # print(province)


    # for tr in Soup.find('tbody').children:
    #     if isinstance(tr, bs4.element.Tag):
    #         tds = tr('td')
    #         print(tds[0].string)
            # 根据实际提取需要的内容，
            # ulist.append([tds[0].string, tds[1].string, tds[3].string])

def printUnivList(data, num):
    tplt = "{0:^10}\t{1:{4}^10}\t{2:^10}\t{3:^20}"
    # {3}表示需要填充时使用format的第三个变量进行填充，即使用中文空格
    print(tplt.format("排名", "学校名称", "地区", "总分", chr(12288)))

    for i in range(num):
        n = data[i]
        print(tplt.format(n[0], n[1], n[2], n[3], chr(12288)))

def main():
    url = 'https://www.shanghairanking.cn/rankings/bcur/2024'
    data = []
    html = get_html(url)
    get_Soup(html,data)
    printUnivList(data,20)

if __name__ == '__main__':
    main()