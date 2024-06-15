import time
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

Info =[]
url ='https://beian.cfdi.org.cn/CTMDS/apps/pub/ylqxPublic1.jsp'

option = webdriver.ChromeOptions()
# 防止访问的时候浏览器关闭
option.add_experimental_option("detach",True)
brower =webdriver.Chrome(options=option)
brower.get(url)
time.sleep(5)
# 设置点击页数
for page_num in range(1,2):
    page = brower.page_source
    # print(page)
    Data = etree.HTML(page)
    # 访问一行的列表//*[@id="searchTable"]/tbody/tr[5]/td[8]/a
    for i in range(1,3):
        brower.find_element(By.XPATH,f'//*[@id="searchTable"]/tbody/tr{[i]}/td[8]/a').click()
        time.sleep(1)
        # 爬取人员名单
        for m in range(1,100):
            num = brower.page_source
            a = etree.HTML(num)
            time.sleep(1)
            zhuanye = a.xpath(f'//*[@id="item"]/div[2]/table/tbody/tr{[m]}/td[1]/text()')
            aurth = a.xpath(f'//*[@id="item"]/div[2]/table/tbody/tr{[m]}/td[2]/text()')
            work = a.xpath(f'//*[@id="item"]/div[2]/table/tbody/tr{[m]}/td[3]/text()')
            if zhuanye == [] :
                brower.find_element(By.XPATH, '//*[@id="ethicClsbtn"]').click()
                print(Info)
                print('下一页')
                break
            else:
                list = [zhuanye[0], aurth[0], work[0]]
                Info.append(list)
                print(list)
        # print('一项爬取成功')
            # 写成一个列表
            # list = [pro, company, name, tel]
            # 添加到总列表里
            # Info.append(list)
        # 点击下一页按钮
print(Info)
# with open('医院名单人员列表.xls','w',encoding='utf-8')as f:
