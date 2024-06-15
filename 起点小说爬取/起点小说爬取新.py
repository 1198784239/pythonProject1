import csv
import bs4
import requests

def get_Html():
    Info = []
    Fil_name = ['Rank','Name','Lex','Con','List']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
        "Cookie": '_yep_uuid=42ed399c-2a57-2eb4-dfea-fd7063dbc88d; e1=%7B%22l6%22%3A%22%22%2C%22l1%22%3A5%2C%22pid%22%3A%22qd_P_rank%22%2C%22eid%22%3A%22qd_C40%22%7D; e2=%7B%22l6%22%3A%22%22%2C%22l1%22%3A5%2C%22pid%22%3A%22qd_P_rank%22%2C%22eid%22%3A%22qd_C40%22%7D; '
                  'newstatisticUUID=1662801251_493794012; supportwebp=true; supportWebp=true; navWelfareTime=1686143265622; _csrfToken=SZxQu6yP9AeHvgk8Nxwz73ZmZogWNSyUkmCPbFx4; fu=1203045347; e2=; e1=%7B%22l6%22%3A%22%22%2C%22l1%22%3A3%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A18%22%7D; traffic_utm_referer=https%3A//cn.bing.com/; w_tsfp=ltvgWVEE2utBvS0Q6K/'
                  'onUmsEzs7Z2R7xFw0D+M9Os09BaQoVp+F0o9yt9fldCyCt5Mxutrd9MVxYnGEUd8hfBEQRcyXb5tH1VPHx8NlntdKRQJtA8+NWlFKKrNxvTZBeGlacUayjGp/INBAybBl3g0E4Scg37ZlCa8hbMFbixsAqOPFm/97DxvSliPXAHGHM3wLc+6C6rgv8LlSgX2NuwDuLi1mH6gTghvNl3VOUmop8xG7dOldNRytI86vWO0wrTPzwjn3apCs2RYj4VA3sB49EMnmim2ffC0HZVZ5b0q2hrh3KqaiMO8t6jdLXqpISwgQrQ4btOcwq0NNWH66MmfC'
        }
    for m in range(1,5):
        url = f'https://www.qidian.com/rank/yuepiao/year2024-month05-page{m}/'
        response =requests.get(url,headers=headers, verify=False)
        res = response.text
        Soup = bs4.BeautifulSoup(res,'lxml')
        for i in range(0,20):
            datas =Soup.find_all(attrs='book-img-box')
            Rank =datas[i].text
            data =Soup.find_all('h2')
            Name = data[i].text
            leix =Soup.find_all(attrs='author')
            Lex=leix[i].text
            content = Soup.find_all(attrs='intro')
            Con=content[i].text
            list = Soup.find_all(attrs='update')
            List =list[i].text
            # Info.append(list(Rank))
            # Info.append(list(Name))
            # Info.append(list(Lex))
            # Info.append(list(Con))
            # Info.append(list(List))
            DATE=[Rank,Name,Lex,Con,List]
            # print(f'第{i}条数据爬取完毕')
            dic = {k:v for k,v in zip(Fil_name,DATE)}
            Info.append(dic)
    print(Info[0].keys())
    return Info

def Save_csv(Info):
    with open('qidian.csv','w',encoding='utf-8') as f:
        writer = csv.writer(f)
        # 先写入columns_name
        writer.writerow(Info[0].keys())
        for x in Info:
            writer.writerow(x.values())
    print('----------------------------文件写入成功-------------------------------------')

def main():
    a = get_Html()
    Save_csv(a)

if __name__ == '__main__':
    main()