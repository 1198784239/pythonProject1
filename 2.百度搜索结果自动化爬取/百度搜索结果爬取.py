from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import title_contains
#打开浏览器
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
browser =webdriver.Chrome(options=option)
browser.get('https://www.baidu.com')
time.sleep(1)

#获取搜索
browser.find_element(By.XPATH,'//*[@id="kw"]').send_keys('小说',Keys.ENTER)

wait = WebDriverWait(browser, 10).until(title_contains('小说'))
while True:
    list = browser.find_elements(By.CSS_SELECTOR,'h3.t')
    for h3 in list:
        print(h3.text)
    time.sleep(2)
    browser.find_element(By.XPATH,'//*[@id="page"]/div/a[last()]').click()