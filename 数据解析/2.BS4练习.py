from bs4 import BeautifulSoup
import time

html = """
<html >
<head>
<meta charset="UTF-8">
<title>this is a title</title>
</head>
<body>
<p class="news"><a >123456</a>
<a >78910</a></p>
<p class="contents" id="i1">456</p>
<a href="http://www.baidu.com" rel="external nofollow" rel="external nofollow" rel="external nofollow" rel="external nofollow" rel="external nofollow" >advertisements</a>
</body>
</html>
"""

Soup = BeautifulSoup(html, "html.parser")
# print(Soup)
# print(type(Soup))
# 获取标签头
print(Soup.title)
# 获取标签头名
# print(Soup.title.text)
# # print(Soup.title.string)
# # print(Soup.title.get_text())
# #获取p标签 仅限第一个
# print(Soup.p)
# #获取节点
# print(Soup.head)
# #获取属性 是个字典
# print(Soup.p.attrs)
# #获取属性名
# print(Soup.p.attrs['class'])
# print(Soup.p['class'])
# #获取属性值
# print(Soup.p.get('class'))

#-----------------------------------------
#获取子节点
# print(Soup.p.contents)
# #返回迭代器
# a = Soup.p.children
# for i,child in enumerate(a):
# #     print(i,child)
# # print(a)
# # #获取字孙节点
# print(Soup.p.descendants)
# #返回迭代器
# a = Soup.p.descendants
# for i,child in enumerate(a):
#     print(i,child)
# # print(a)
#
# c3=Soup.title.parent
# print(c3)

#使用select筛选
m =Soup.select('.news')
a = m[0].name
a = m[0].attrs
a = m[0].attrs['class']
print(a)

#使用find\find_all方式
s =Soup.find_all(attrs='news')
print(s)
print(s[0].text)
print(s[0].name)
print(s[0].attrs)