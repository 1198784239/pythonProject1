import cv2
from selenium import webdriver
import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


def HuaK(a,b):
    # 读取背景图片和缺口图片
    bg_img = cv2.imread(a) # 背景图片
    tp_img = cv2.imread(b) # 缺口图片

    # 识别图片边缘
    bg_edge = cv2.Canny(bg_img, 100, 200)
    tp_edge = cv2.Canny(tp_img, 100, 200)


    # 转换图片格式
    bg_pic = cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2RGB)
    tp_pic = cv2.cvtColor(tp_edge, cv2.COLOR_GRAY2RGB)
    # cv2.imwrite('bg11.png', bg_pic)
    # cv2.imwrite('bg12.png', tp_pic)

    # 缺口匹配
    res = cv2.matchTemplate(bg_pic, tp_pic, cv2.TM_CCOEFF_NORMED)
    # print(res)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res) # 寻找最优匹配
    print(min_val, max_val, min_loc, max_loc)
    X = max_loc[0]

    # 绘制方框
    th, tw = tp_pic.shape[:2]
    tl = max_loc # 左上角点的坐标
    br = (tl[0]+tw,tl[1]+th) # 右下角点的坐标
    cv2.rectangle(bg_img,    tl, br, (0, 0, 255), 2) # 绘制矩形
    cv2.imwrite('out.jpg', bg_img) # 保存在本地
    #算出移动距离
    m = tl[0]*0.66+15
    print(tl[0])
    return m
# 调用参数
HuaK('12.jpg','123.jpg')

url = 'https://dun.163.com/trial/jigsaw'
#设置参数 防止闪退
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=options)
driver.get(url)
#获取链接
driver.find_element(By.XPATH,'/html/body/main/div[1]/div/div[2]/div[2]/ul[2]/li[2]').click()
time.sleep(0.5)
a = driver.find_element(By.XPATH,'/html/body/main/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div[3]/div/div/div[2]/div[2]')
time.sleep(1)
first =driver.find_element(By.XPATH,'/html/body/main/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div[3]/div/div/div[1]/div/div[1]/img[2]')
last = driver.find_element(By.XPATH,'/html/body/main/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div[3]/div/div/div[1]/div/div[1]/img[1]')
#缺口
m = first.get_attribute('src')
#图片
t = last.get_attribute('src')

# 获取图片
r = requests.get(m)
t1 = requests.get(t)
# r1 = requests.get(path1)
# r.raise_for_status()
#下载图片到文件夹里
with open('123.jpg', 'wb')as f:
    f.write(r.content)
with open('12.jpg', 'wb')as f:
    f.write(t1.content)
# print(path1)
time.sleep(1)

# ------------鼠标滑动操作------------
action = ActionChains(driver)
# 第一步：在滑块处按住鼠标左键
action.click_and_hold(a)
# 第二步：相对鼠标当前位置进行移动
action.move_by_offset(HuaK('12.jpg','123.jpg'),0)
# 第三步：释放鼠标
action.release()
# 执行动作
action.perform()



