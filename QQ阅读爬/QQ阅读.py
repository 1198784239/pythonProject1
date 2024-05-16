import requests
from bs4 import BeautifulSoup
import re
first_char = int(input("请输入第一章节："))
last_char = int(input("请输入最后章节："))

for i in range(first_char,last_char+1):
    url = f'https://book.qq.com/book-read/48731165/{i}'
    res = requests.get(url).text
    # print(res)
    data =re.compile('<title>.*_(.*?)在线阅读-QQ',re.S)
    list =re.compile(',chapterContent:"(.*?)bookChapters',re.S)
    title = re.findall(data,res)[0]
    content = re.findall(list,res)
    content1 =str(content).replace("\\r",'').replace("\\\\n",'')
    a=content1.replace("\\u3000",'').replace('\\','').replace('」「','').replace('b','')
    # m=a.replace('u003Cu002Fpu003Eu003Cpu003E','')
    pattern = r'[a-z]+[0-9]+\w'
    rep = ''
    newstr = re.sub(pattern,rep,a)
    print(title)
    print(newstr)

#a 是不覆盖之前的
    with open('book.txt','w',encoding='utf-8') as f:
        f.write(title+'\n')
        f.write(newstr+'\n')
        f.write('\n')
        print('----------------写入成功-------------------')


# data = BeautifulSoup(res, 'lxml')
# con = data.find_all('p')
# for i in con:
    # print(i)
# print(type(con))
# # con.replace('</p>, <p>','')
# print(con)



