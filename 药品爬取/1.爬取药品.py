import time
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import openpyxl

Info =[]
url ='https://beian.cfdi.org.cn/CTMDS/apps/pub/ylqxPublic1.jsp'
def get_Html():
    option = webdriver.ChromeOptions()
    # 防止访问的时候浏览器关闭
    option.add_experimental_option("detach",True)
    brower =webdriver.Chrome(options=option)
    brower.get(url)
    time.sleep(5)
    # 设置点击页数
    for page_num in range(1,5):
        page = brower.page_source
        # print(page)
        Data = etree.HTML(page)
        # 访问一页的列表
        for i in range(1,11):
            pro =Data.xpath(f'//*[@id="searchTable"]/tbody/tr{[i]}/td[1]/text()')[0]
            company =Data.xpath(f'//*[@id="searchTable"]/tbody/tr{[i]}/td[3]/text()')[0]
            name =Data.xpath(f'//*[@id="searchTable"]/tbody/tr{[i]}/td[5]/text()')[0]
            tel =Data.xpath(f'//*[@id="searchTable"]/tbody/tr{[i]}/td[6]/text()')[0]
            # print(pro,company,name,tel)
            # 写成一个列表
            list = [pro,company,name,tel]
            # 添加到总列表里
            Info.append(list)
            # 点击下一页按钮
        brower.find_element(By.XPATH,'//*[@id="searchTable_pt_nextPage"]').click()
        time.sleep(3)
    print(Info)

def Save_url():
    with open('医院名单.csv', 'w', encoding='utf-8') as f:
        header = ['省份', '医院', '联系人', '电话']
        writer = csv.writer(f)
        # 写入标题行
        writer.writerow(header)
        #写入数据
        writer.writerows(Info)
        print("数据写入成功")

def Save_data():
        # 创建工作表
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet['A1']='省份'
    sheet['B1']='医院'
    sheet['C1']='联系人'
    sheet['D1']='电话'
    for i in range(len(Info)):
        sheet.append([Info[i][0],Info[i][1],Info[i][2],Info[i][3]])
    workbook.save('医院名单表.xls')
    print('写入成功')
def main():
    get_Html()
    Save_url()
    Save_data()

if __name__ == '__main__':
    main()