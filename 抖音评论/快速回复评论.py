import ddddocr
from selenium import webdriver
import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import title_contains

url = 'https://live.douyin.com'
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="douyin-header"]/div[1]/header/div/div/div[1]/div/div[2]/div/div/input').send_keys('大大脑袋小小梦想',Keys.ENTER)
s = driver.find_element(By.XPATH,'//*[@id="vc_captcha_box"]/div/div/div[4]/div/div[2]/div[2]/div').send_keys('大大脑袋小小梦想',Keys.ENTER)


# ------------鼠标滑动操作------------
action = ActionChains(driver)
# 第一步：在滑块处按住鼠标左键
action.click_and_hold(s)
# 第二步：相对鼠标当前位置进行移动
action.move_by_offset(100,0)
# 第三步：释放鼠标
action.release()
# 执行动作
action.perform()