import requests
import re
def getHTMLText(url):
    """
    请求获取html，（字符串）
    :param url: 爬取网址
    :return: 字符串
    """
    try:
        # 添加头信息,
        kv = {
            'cookie': 'cna=/djLFQ8jF2ACAXWINWH5tONp; miid=1550538301329058581; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; _samesite_flag_=true; cookie2=18e02cf90d454c8cb926a114f60ec7cc; t=688ab2add990e3bffb0ed2a50ed372a6; _tb_token_=eb3da51a61f59; sgcookie=ECGrrC7L0rNhRvhN%2B1145; unb=4210925800; uc3=lg2=U%2BGCWk%2F75gdr5Q%3D%3D&id2=Vy65UIACXO2M1g%3D%3D&vt3=F8dBxGR1SmOsGPiY82E%3D&nk2=F5RMGyVIy88whPU%3D; csg=3ce250f7; lgc=tb926953644; cookie17=Vy65UIACXO2M1g%3D%3D; dnk=tb926953644; skt=8e1b9d0b02177148; existShop=MTU4NzYzOTY0Mg%3D%3D; uc4=nk4=0%40FY4HXg9QErMhoZFWuJFJVNeezM6cXg%3D%3D&id4=0%40VXkerg5gGAYhi1vj74vRDu5h8rY4; tracknick=tb926953644; _cc_=URm48syIZQ%3D%3D; _l_g_=Ug%3D%3D; sg=40e; _nk_=tb926953644; cookie1=ACux%2Fc1GxpWNNJyD3iL%2BFynlCW5Ee7Kf63jSrmtUsqU%3D; tfstk=cKURBvw4etXo82NrbyImRhCFnzCGaA6KhQMHJ69Py1kN8tTwSsXTSPlEKgGBeqCA.; enc=a552yClWGHYG%2FJ5A40IGImVJ%2FBLDMVEw8f3Xgy8g0boJ9eryWA2QY%2FE4RFJD1KKCJ7FoRcSsBp2Un540LK1taA%3D%3D; mt=ci=31_1; v=0; uc1=cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&cookie21=W5iHLLyFe3xm&cookie15=W5iHLLyFOGW7aA%3D%3D&existShop=false&pas=0&cookie14=UoTUPcqfFetGuw%3D%3D; JSESSIONID=1E7324D67003202D798CD0F5DE2668C9; isg=BJycKuUFLg4Esdm1F5aeOK_AbbpOFUA_AfYh3Had4gdqwT1Lnib0z1V3ISk5z3iX; l=eBMvzQKIqfn3dCYMBOfaPurza77TKIRbouPzaNbMiT5POTCp5qeGWZjXETT9CnGVHs6pR37el_8YBAYNcydqJxpsw3k_J_qI3dC..',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
        r = requests.get(url, timeout=30, headers=kv)
        # r = requests.get(url, timeout=30)
        # print(r.status_code)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "爬取失败"
def parsePage(glist, html):
    '''
    解析网页，搜索需要的信息
    :param glist: 列表作为存储容器
    :param html: 由getHTMLText()得到的
    :return: 商品信息的列表
    '''
    try:
        # 使用正则表达式提取信息
        price_list = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        name_list = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(price_list)):
            price = eval(price_list[i].split(":")[1])  #eval（）在此可以去掉""
            name = eval(name_list[i].split(":")[1])
            glist.append([price, name])
    except:
        print("解析失败")
def printGoodList(glist):
    tplt = "{0:^4}\t{1:^6}\t{2:^10}"
    print(tplt.format("序号", "商品价格", "商品名称"))
    count = 0
    for g in glist:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))
# 根据页面url的变化寻找规律，构建爬取url
goods_name = "书包"  # 搜索商品类型
start_url = "https://s.taobao.com/search?q=" + goods_name
info_list = []
page = 3  # 爬取页面数量
count = 0
for i in range(page):
    count += 1
    try:
        url = start_url + "&s=" + str(44 * i)
        html = getHTMLText(url)  # 爬取url
        parsePage(info_list, html) #解析HTML和爬取内容
        print("\r爬取页面当前进度: {:.2f}%".format(count * 100 / page), end="")  # 显示进度条
    except:
        continue
print()
printGoodList(info_list)
