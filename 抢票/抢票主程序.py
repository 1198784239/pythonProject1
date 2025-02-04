import os
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

class RailwayBot:
    def __init__(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=option)
        self.login_url = "https://kyfw.12306.cn/otn/resources/login.html"
        self.search_url = "https://kyfw.12306.cn/otn/leftTicket/init"
        self.cookie_file = '12306_cookies.json'

    def handle_captcha(self):
        """处理滑动验证码（需手动干预或接入打码平台）"""
        # 示例：手动滑动（实际需自动化识别）
        time.sleep(20)  # 留出时间手动操作

    def load_cookies(self):
        """加载保存的 cookies"""
        if os.path.exists(self.cookie_file):
            with open(self.cookie_file, 'r') as f:
                cookies = json.load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)

    def save_cookies(self):
        """保存当前会话的 cookies 到本地文件"""
        cookies = self.driver.get_cookies()
        with open(self.cookie_file, 'w') as f:
            json.dump(cookies, f)

    def login(self):
        if os.path.exists(self.cookie_file):
            self.driver.get(self.search_url)
            self.load_cookies()
            self.driver.refresh()  # 刷新页面使 cookies 生效
            # 检查是否已经登录成功
            try:
                # 这里可以根据登录成功后页面上的某个元素来判断，例如用户名显示元素
                self.driver.find_element(By.ID, "用户名显示元素的 ID")
                print("使用 cookies 登录成功")
                return
            except:
                print("cookies 失效，重新登录")

        self.driver.get(self.login_url)
        self.driver.find_element(By.ID, "J-userName").send_keys("LKC13515662665")
        self.driver.find_element(By.ID, "J-password").send_keys("Lkc19990201")
        self.driver.find_element(By.ID, "J-login").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "id_card").send_keys("2415")
        self.handle_captcha()  # 处理验证码
        self.save_cookies()  # 登录成功后保存 cookies

    def query_tickets(self):
        """查询车票并下单"""
        self.driver.get(self.search_url)
        # 填写查询条件（示例：北京-上海 2023-12-25）
        self.driver.find_element(By.ID, "fromStationText").click()
        self.driver.find_element(By.ID, "fromStationText").send_keys("淮南")
        self.driver.find_element(By.ID, "fromStationText").send_keys(Keys.RETURN)
        self.driver.find_element(By.ID, "toStationText").click()
        self.driver.find_element(By.ID, "toStationText").send_keys("南京")
        self.driver.find_element(By.ID, "toStationText").send_keys(Keys.RETURN)
        self.driver.find_element(By.ID, "train_date").click()
        self.driver.find_element(By.ID, "train_date").send_keys(Keys.END)
        self.driver.find_element(By.ID, "train_date").clear()
        # 选择乘车的日期
        self.driver.find_element(By.ID, "train_date").send_keys("2025-02-05")
        self.driver.find_element(By.ID, "train_date").send_keys(Keys.RETURN)
        self.driver.find_element(By.ID, "query_ticket").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="_ul_station_train_code"]/li[5]').click()
        time.sleep(2)

        # 选择车次（示例：G123）
        # 选择第几辆列车  假如为1，则填写1，为2，则3（1，3，5，7，9）
        ticket_btn = self.driver.find_element(By.XPATH, '//*[@id="queryLeftTable"]/tr[3]/td[11]').text
        while ticket_btn == "无":
            self.driver.find_element(By.ID, "query_ticket").click()
            time.sleep(3)
            print(ticket_btn)
        # 第几列
        self.driver.find_element(By.XPATH, '//*[@id="queryLeftTable"]/tr[3]/td[13]').click()
        time.sleep(2)
        self.masge()

    def masge(self):
        namelist = self.driver.find_elements(By.CSS_SELECTOR, '#normal_passenger_id li')
        for index, li in enumerate(namelist, start=1):
            if "李伟" in li.text:
                print(f"包含 '李克聪' 的 li 标签编号为: {index}")
                self.driver.find_element(By.XPATH, f'//*[@id="normal_passenger_id"]/li[{index}]/input').click()
                # self.driver.find_element(By.XPATH, f'//*[@id="submitOrder_id"]').click()
                time.sleep(2)
                break
        else:
            print("未找到包含 '李克聪' 的 li 标签")


if __name__ == "__main__":
    bot = RailwayBot()
    bot.login()
    bot.query_tickets()