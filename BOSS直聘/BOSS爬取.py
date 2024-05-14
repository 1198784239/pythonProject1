import csv
from DrissionPage import ChromiumPage
import time
# option = webdriver.ChromeOptions()
# option.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=option)
#1.打开浏览器
driver = ChromiumPage()
#2.请求数据
# driver.get('https://www.zhipin.com/web/geek/job?query=%E5%89%8D%E7%AB%AF&city=101190100&page={i}')
# time.sleep(2)
for i in range(0,3):
    driver.get(f'https://www.zhipin.com/web/geek/job?query=%E5%89%8D%E7%AB%AF&city=101190100&page={i}')
    # time.sleep(1)
    #下滑到最下面
    # driver.scroll.to_bottom()
    #3。监听包
    driver.listen.start('wapi/zpgeek/search/joblist.json?scene=1&query=%E5%89%8D%E7%AB%AF&city=101190100&experience=&pay')
    #4.等待请求
    res = driver.listen.wait()
    # print(res)
    #5发送请求
    json_data = res.response.body
    #6.获取信息
    # print(json_data)
    #创建文件
    f = open('boss.csv', 'w', encoding='utf-8')
    csv.writer = csv.DictWriter(f, [
            '工作',
            '地点',
            '公司',
            '人数',
            '工资',
            '年限',
            '学历',
            '技能',
            '福利',
    ])
    csv.writer.writeheader()
    #创建一个字典
    lists = json_data['zpData']['jobList']
    for list in lists:
        dic = {
            '工作':list['jobName'],
            '地点':list['areaDistrict'],
            '公司':list['brandName'],
            '人数':list['brandScaleName'],
            '工资':list['salaryDesc'],
            '年限':list['jobLabels'][0],
            '学历':list['jobLabels'][1],
            '技能':list['skills'],
            '福利':list['welfareList'],

        }
        csv.writer.writerow(dic)
        print(dic)
        #点击下一页
        # driver.ele('css:.ui-icon-arrow-right').click()

