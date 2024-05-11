from selenium import webdriver
from bs4 import BeautifulSoup
import time
import ddddocr
from selenium.webdriver.common.by import By

class api():
    def __init__(self):
        self.OCR = ddddocr.DdddOcr()

    def imgtext(self,img_page):
        # im = open(img_page,'rb').read()
        res = self.OCR.classification(img_page).upper()
        # print(res)
        return res

url = 'https://so.gushiwen.cn/user/login.aspx?'
#打开浏览器
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=option)
browser.get(url)
#定位输入框
email = "13033059109"
pwd = "lkc19990201"
#定位验证码图片
img = browser.find_element(By.XPATH,'//*[@id="imgCode"]').screenshot_as_png
# img_page = 'img.png'
# 识别二维码
OCR = api()
# 传入数据
a = OCR.imgtext(img_page=img)
# print(a)
#账号
browser.find_element(By.XPATH,'//*[@id="email"]').send_keys(email)
#密码
browser.find_element(By.XPATH,'//*[@id="pwd"]').send_keys(pwd)
#验证码
browser.find_element(By.XPATH,'//*[@id="code"]').send_keys(a)
# 登录按钮
browser.find_element(By.XPATH,'//*[@id="denglu"]').click()


#获取cook
cookies = browser.get_cookies()

#保存到本地
with open('cookies.txt', 'w') as f:
    f.write(str(cookies))
    print('保存成功')

browser.close()

#打开新的窗口看能不能
new_bro = webdriver.Chrome(options=option)

#打开网站
new_bro.get(url)

#读取cookie并添加到浏览器
with open('cookies.txt', 'r') as fb:
    cookdata =eval(fb.read())
    print("读取成功")
    print(cookies)

for cookie in cookdata:
    new_bro.add_cookie(cookie)
    print('正在添加')
    time.sleep(1)

new_bro.get(url='https://so.gushiwen.cn/user/login.aspx?')
print('添加成功')
new_bro.find_element(By.XPATH,'//*[@id="html"]/body/div[1]/div[1]/div/div[2]/div[1]/a[6]').click()