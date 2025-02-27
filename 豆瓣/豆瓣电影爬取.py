import requests
from lxml import etree
import re
import csv

# 豆瓣电影 Top250 的起始 URL
url = "https://movie.douban.com/top250"
# 设置请求头，模拟浏览器访问
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
}

# 用于存储所有电影数据的列表
allMovieList = []
# 标志位，用于控制是否继续爬取下一页
flag = True

while flag:
    # 发送请求获取页面内容
    html = requests.get(url, headers=header).text
    # 使用 lxml 解析 HTML 内容
    tree = etree.HTML(html)
    # 查找所有电影项
    lis = tree.xpath('//ol[@class="grid_view"]/li')
    for oneSelector in lis:
        # 提取电影名称
        name = oneSelector.xpath('div/div[2]/div[1]/a/span[1]/text()')[0]
        # 提取电影评分
        score = oneSelector.xpath('div/div[2]/div[2]/div/span[2]/text()')[0]
        # 提取评价人数
        people = oneSelector.xpath('div/div[2]/div[2]/div/span[4]/text()')[0]
        # 使用正则表达式提取评价人数的具体数字
        people = re.findall(r'(.*?)人评价', people)[0]
        # 将电影名称、评分和评价人数组成一个列表
        oneMovieList = [name, score, people]
        # 将该电影的数据添加到总列表中
        allMovieList.append(oneMovieList)

    # 获取下一页地址
    try:
        next_url = tree.xpath('//span[@class="next"]/a/@href')[0]
        if next_url:
            url = "https://movie.douban.com/top250" + next_url
    except IndexError:
        # 如果没有下一页，将标志位设置为 False，停止循环
        flag = False

# 打印所有电影数据
print(allMovieList)

# 打开 CSV 文件，以写入模式打开，设置编码为 UTF-8 并避免出现空行
with open('douban.csv', 'w', encoding='utf-8', newline='') as f:
    # 创建一个 csv.writer 对象
    writer = csv.writer(f)
    # 写入 CSV 文件的表头
    writer.writerow(['Name', 'score', 'people'])
    # 遍历所有电影数据，将每条数据写入 CSV 文件
    for row in allMovieList:
        writer.writerow(row)

# 打印文件写入成功的信息
print('文件写入成功')