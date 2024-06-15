import pandas as pd
import requests
import xlwt
from bs4 import BeautifulSoup
def main():
        m = Html_Info()
        save_excel(m)
        Save_Img(m)
        print(Html_Info())

 # 保存图片
def Save_Img(m):
    for  i,img in enumerate(m['地址']):
        img_pic = requests.get(img).content
        with open(f'./图片和表格库/{i+1}.jpg', 'wb') as f:
            f.write(img_pic)

def Html_Info():
    movie_info = {
        '地址': [],
        '电影名字': [],
        '类型': [],
        '国家': [],
        '时长': [],
        '上映时间': [],
        '分数': [],

    }
    for page in range(1, 8):
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'}
        url = f'https://ssr1.scrape.center/page/{page}'
        response = requests.get(url, headers=header)
        Soup = BeautifulSoup(response.text, 'html.parser')
        result = Soup.find_all('div', class_='p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 el-col-md-16')
        result1 = Soup.find_all('div', class_='el-col el-col-24 el-col-xs-5 el-col-sm-5 el-col-md-4')
        img = Soup.find_all('div', class_='el-col el-col-24 el-col-xs-8 el-col-sm-6 el-col-md-4')
        # print(img)
        for i in range(len(result)):
            movie_info['地址'].append(img[i].img.get('src'))
            movie_info['电影名字'].append(result[i].h2.string)
            btn_list = result[i].find_all('button','el-button category el-button--primary el-button--mini')
            movie_type = ''
            for btn in btn_list:
                # print(btn.span.string)
                movie_type += btn.span.string+','
            movie_info['类型'].append(movie_type)
            info_list = result[i].find_all('div','m-v-sm info')
            span_list = info_list[0].find_all('span')
            movie_info['国家'].append(span_list[0].text)
            movie_info['时长'].append(span_list[2].text)
            movie_info['上映时间'].append(info_list[1].text.strip())
            num = result1[i].find_all('p','score m-t-md m-b-n-sm')
            movie_info['分数'].append(num[0].text.strip())
    # print(movie_info)
    return movie_info

# with open('123.xls', 'wb') as f:
#     writer = xlwt.Workbook(f)
#     writer.sheet1 = writer.add_sheet('Sheet1', cell_overwrite_ok=True)
#     for i in range(len(movie_info)):
#         writer.sheet1.write(i, 0, movie_info[i])
#         writer.save()
def save_excel(movie_info):
    data = pd.DataFrame(movie_info)
    data.to_excel('./图片和表格库/12323.xlsx',index=False)




if __name__ == '__main__':
    main()



