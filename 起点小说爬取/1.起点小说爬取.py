import csv
import sqlite3
import re
import requests
from bs4 import BeautifulSoup

def get_Page():
    Info = []
    for i in range(1, 3):
        url = f'https://www.qidian.com/rank/yuepiao/year2024-month05-page{i}/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
            "Cookie": '_yep_uuid=42ed399c-2a57-2eb4-dfea-fd7063dbc88d; e1=%7B%22l6%22%3A%22%22%2C%22l1%22%3A5%2C%22pid%22%3A%22qd_P_rank%22%2C%22eid%22%3A%22qd_C40%22%7D; e2=%7B%22l6%22%3A%22%22%2C%22l1%22%3A5%2C%22pid%22%3A%22qd_P_rank%22%2C%22eid%22%3A%22qd_C40%22%7D; '
                      'newstatisticUUID=1662801251_493794012; supportwebp=true; supportWebp=true; navWelfareTime=1686143265622; _csrfToken=SZxQu6yP9AeHvgk8Nxwz73ZmZogWNSyUkmCPbFx4; fu=1203045347; e2=; e1=%7B%22l6%22%3A%22%22%2C%22l1%22%3A3%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A18%22%7D; traffic_utm_referer=https%3A//cn.bing.com/; w_tsfp=ltvgWVEE2utBvS0Q6K/'
                      'onUmsEzs7Z2R7xFw0D+M9Os09BaQoVp+F0o9yt9fldCyCt5Mxutrd9MVxYnGEUd8hfBEQRcyXb5tH1VPHx8NlntdKRQJtA8+NWlFKKrNxvTZBeGlacUayjGp/INBAybBl3g0E4Scg37ZlCa8hbMFbixsAqOPFm/97DxvSliPXAHGHM3wLc+6C6rgv8LlSgX2NuwDuLi1mH6gTghvNl3VOUmop8xG7dOldNRytI86vWO0wrTPzwjn3apCs2RYj4VA3sB49EMnmim2ffC0HZVZ5b0q2hrh3KqaiMO8t6jdLXqpISwgQrQ4btOcwq0NNWH66MmfC'
        }
        try:
            # 建议去掉 verify=False 以保证安全
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            res = response.text
            html_Info(res, Info)
            print(f'第{i}页数据爬取完毕')
        except requests.RequestException as e:
            print(f"请求第{i}页时出错: {e}")
    return Info

def html_Info(res, Info):
    Fil_name = ['Rank', 'Name', 'Lex', 'Con', 'List', 'Time']
    soup = BeautifulSoup(res, 'lxml')
    datas = soup.find_all(attrs='book-img-box')
    names = soup.find_all('h2')
    leix = soup.find_all(attrs='author')
    content = soup.find_all(attrs='intro')
    list_ = soup.find_all(attrs='update')

    for i in range(min(len(datas), len(names), len(leix), len(content), len(list_))):
        Rank = datas[i].text.strip()
        Name = names[i].text.strip()
        Lex = leix[i].text.strip()
        Con = content[i].text.strip()
        List = list_[i].text.strip()
        # 修正拼写错误
        Time_match = re.search(r'\d{4}-\d{2}-\d{2}', List)
        Time = Time_match.group(0) if Time_match else None
        DATE = [Rank, Name, Lex, Con, List, Time]
        print(f'第{i}条数据爬取完毕')
        dic = {k: v for k, v in zip(Fil_name, DATE)}
        Info.append(dic)
    print(Info)

def Save_csv(Info):
    with open('qidian.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Rank', 'Name', 'Lex', 'Con', 'List', 'Time'])
        writer.writeheader()
        for row in Info:
            writer.writerow(row)
    print('文件写入成功')

def Save_to_DB(Info):
    conn = sqlite3.connect('qidian.db')
    cursor = conn.cursor()
    print("数据库连接已打开")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS qidian_books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Rank TEXT,
            Name TEXT,
            Lex TEXT,
            Con TEXT,
            List TEXT,
            Time DATE
        )
    ''')
    print("表已创建或已存在")

    for data in Info:
        try:
            values = (data['Rank'], data['Name'], data['Lex'], data['Con'], data['List'], data['Time'])
            print(f"要插入的数据值: {values}")  # 打印要插入的数据值用于调试
            cursor.execute('''
                INSERT INTO qidian_books (Rank, Name, Lex, Con, List, Time)
                VALUES (?,?,?,?,?,?)
            ''', (data['Rank'], data['Name'], data['Lex'], data['Con'], data['List'], data['Time']))
            print("数据插入成功")
        except sqlite3.IntegrityError as e:
            print(f"插入数据时出现完整性错误: {e}")
        except sqlite3.OperationalError as e:
            print(f"插入数据时出现操作错误: {e}")
        except Exception as e:
            print(f"插入数据时出现未知错误: {e}")

    conn.commit()
    conn.close()
    print("数据库连接已关闭")

def main():
    Info = get_Page()
    # Save_csv(Info)
    Save_to_DB(Info)

if __name__ == '__main__':
    main()