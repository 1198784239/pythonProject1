from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os, json

# 配置Chrome驱动路径（需提前下载对应版本的chromedriver）
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option)
cookie_file = 'boss_cookies.json'

def load_cookies():
    """加载保存的 cookies"""
    if os.path.exists(cookie_file):
        with open(cookie_file, 'r') as f:
            cookies = json.load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)

def save_cookies():
    """保存当前会话的 cookies 到本地文件"""
    cookies = driver.get_cookies()
    with open(cookie_file, 'w') as f:
        json.dump(cookies, f)

def login_bosszhipin():
    """登录BOSS直聘"""
    if os.path.exists(cookie_file):
        driver.get("https://www.zhipin.com/")
        time.sleep(3)
        load_cookies()
        driver.refresh()  # 刷新页面使 cookies 生效
        # 检查是否已经登录成功
        try:
            # 这里可以根据登录成功后页面上的某个元素来判断，例如用户名显示元素
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//li[@class="nav-figure"]'))
            )
            print("使用 cookies 登录成功")
            return
        except:
            print("cookies 失效，重新登录")

    driver.get("https://www.zhipin.com/")
    # 点击登录按钮
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@ka="header-login"]'))
    )
    login_button.click()
    time.sleep(2)

    # 输入手机号（需替换为实际账号）
    phone_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="tel"]'))
    )
    phone_input.send_keys("13033059109")
    time.sleep(1)

    # 发送验证码（需手动输入验证码）
    send_code_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@ka="signup_submit_button_click"]'))
    )
    send_code_button.click()
    input("请手动输入验证码，输入完成后按回车键继续...")
    save_cookies()
    time.sleep(5)

def search_and_apply(job_keyword, max_pages=1):
    """搜索职位并自动投递"""
    # 进入职位搜索页
    driver.get(f"https://www.zhipin.com/web/geek/job?query={job_keyword}")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="search-job-result"]'))
    )

    all_jobs = []  # 用于存储所有职位信息的列表

    for page in range(max_pages):
        print(f"正在处理第 {page + 1} 页...")
        # 获取当前页所有职位列表
        job_list = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[@class="search-job-result"]//li'))
        )
        print(len(job_list))
        for i in range(len(job_list)):
            try:
                # 重新获取当前职位元素，避免 stale element 异常
                job = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, '//div[@class="search-job-result"]//li'))
                )[i]

                # 提取职位名称
                job_name = WebDriverWait(job, 10).until(
                    EC.presence_of_element_located((By.XPATH, './/span[@class="job-name"]'))
                ).text
                # 提取工作地点
                job_area = WebDriverWait(job, 10).until(
                    EC.presence_of_element_located((By.XPATH, './/span[@class="job-area"]'))
                ).text
                # 提取薪资
                job_salary = WebDriverWait(job, 10).until(
                    EC.presence_of_element_located((By.XPATH, './/span[@class="salary"]'))
                ).text
                # 提取标签列表
                job_taglist = WebDriverWait(job, 10).until(
                    EC.presence_of_element_located((By.XPATH, './/ul[@class="tag-list"]'))
                ).text

                # 将每个职位的信息组合成一个字典
                job_info = {
                    'job_name': job_name,
                    'job_area': job_area,
                    'job_salary': job_salary,
                    'job_taglist': job_taglist
                }

                # 将职位信息字典添加到 all_jobs 列表中
                all_jobs.append(job_info)
            except Exception as e:
                print(f"提取职位信息失败: {e}")

        # 打印当前页的所有职位信息
        for job_info in all_jobs:
            print(job_info)

        # 翻页
        try:
            next_page = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//i[@class="ui-icon-arrow-right"]'))
            )
            if 'disabled' not in next_page.get_attribute('class'):
                next_page.click()
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//div[@class="search-job-result"]'))
                )
            else:
                print("已经是最后一页，无法继续翻页")
                break
        except Exception as e:
            print(f"翻页失败: {e}")
            break

if __name__ == "__main__":
    login_bosszhipin()
    search_and_apply("Python开发", max_pages=1)  # 搜索关键词和页数
    driver.quit()