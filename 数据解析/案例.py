import pandas as pd
import time
import selenium.common.exceptions
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

url = 'https://www.zhipin.com/web/geek/job?query=Python&city=101280100'
# driver= webdriver.Edge("C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe")
# driver=webdriver.PhantomJS()
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option)

import re
# print(html)
# wait = WebDriverWait(driver, 20)


def get_Boss():
    driver.get(url)
    time.sleep(5)
    html = driver.page_source
    # try:
    jobs = []  # 岗位列表，保存所以岗位
    adders = []  # 地址
    moneys = []  # 薪酬
    dems = []  # 要求
    # 页数，可自定义
    for i in range(2):
        # #获取网页源码
        html = driver.page_source
        bs = BeautifulSoup(html, 'html.parser')
        print(html)


        job = bs.find_all('span', {'class': 'job-name'})  # 找到对应属性的span标签，格式为列表
        adder = bs.find_all('span', {'class': 'job-area'})
        money = bs.find_all('span', {'class': 'salary'})
        # dem = bs.X('ul', {'class': 'tag-list'}).findChild()
        m =re.compile('<ul class="tag-list"><li>(.*?)</li>',re.S)
        dem =re.findall(m,html)
        # print(dem)
        # print(job)
        for j in job:
            j = j.get_text()  # 提取标签下text文本
            # print(j)
            jobs.append(j)  # 添加到列表
            # f = pd.DataFrame(data={})
        for a in adder:
            a = a.get_text()
            adders.append(a)
            # print(a)
            # f = pd.DataFrame(data={})
        for m in money:
            m = m.get_text()
            moneys.append(m)
            # print(m)
            # f = pd.DataFrame(data={})
        for d in range(30):
            if d==0:
                dems.append(dem[d])
            else:
                g = d*2
                dems.append(dem[g])
        # print(dems)

        print(jobs,adders,moneys,dems)
        print(len(jobs),len(adders),len(moneys),len(dems))

        #点击下一页
        driver.find_element(By.CSS_SELECTOR,'#wrap > div.page-job-wrapper > div.page-job-inner > div > div.job-list-wrapper > div.search-job-result > div > div > div > a:nth-child(10)').click()
        # wrap > div.page-job-wrapper > div.page-job-inner > div > div.job-list-wrapper > div.search-job-result > div > div > div > a:nth-child(10))
        # btn = driver.until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, '#main > div > div.job-list > div.page > a.next')))
        # driver.execute_script('arguments[0].click();', btn)
        time.sleep(20)
    # 文件保存
    f = pd.DataFrame(data={'岗位': jobs, '地址': adders, '薪酬': moneys, '要求': dems})
    f.to_csv('Boss直聘招聘信息.csv', encoding='utf-8')
    # except selenium.common.exceptions.NoSuchElementException:
    #     print('运行出错了！')


if __name__ == '__main__':
    get_Boss()


