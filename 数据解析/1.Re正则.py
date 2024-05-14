import re

# print("\\n") # 输出 \n
# print(r"\n") #输出 \n

#re.match函数  re.match(pattern, string, flags=0)
result = re.match("itcast","itcast.cn")
print(result.group())

# 匹配单个字符
ret = re.match("i.c","itcast.cn")
print(ret.group())

# ⼤⼩写h都可以的情况
ret = re.match("[hH]","hello Python,HEllo")
print(ret.group())
#匹配数字
ret = re.match("[0-9]Hello Python","7Hello Python")
print(ret.group())

# 匹配多个字符 *是0个或多个  +一个或多个 ？要么0此或者1次 {2:}大于两次 {2:4}2次到4次
ret = re.match("[A-Z][a-z]*","Aabcdef")
print(ret.group())

ret = re.match("[A-Z][a-z]+","Aabcdef")
print(ret.group())

ret = re.match("[A-Z][a-z]?","Aabcdef")
print(ret.group())

# 匹配出，变量名是否有效
names = ["name1", "_name", "2_name", "__name__"]
for name in names:
    ret = re.match("[a-zA-Z_]+[\w+]*", name)
    if ret:
        print("变量名 %s 符合要求" % ret.group())
    else:
        print("变量名 %s ⾮法" % name)


#提取区号和电话号码
ret = re.match("([^-]*)-(\d+)","010-12345678")
print(ret.group())
print(ret.group(1))
print(ret.group(2))

ret = re.match(r"<([a-zA-Z]*)>(\w*)</\1>", "<html>hh</html>")
print(ret.group(2))

labels = ["<html><h1>www.itcast.cn</h1></html>", "<html><h1>www.itcast.cn</h2></html>"]
# for name in labels:
#     ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", name)
#     print(ret.group())

# 起别名(?P<name>)引用名字 (?P=name)
ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>","<html><h1>www.itcast.cn</h1></html>")
print(ret.group())

# re.split(pattern, string, maxsplit=0, flags=0)
a = re.split(r":| ","info:xiaoZhang 33 shandong")
print(a)

# 贪婪匹配"*","?","+","{m,n} 非贪婪加上？变成非贪婪
import re
s="This is a number 234-235-22-423"
#正则表达式模式中使⽤到通配字，那它在从左到右的顺序求值时，会尽量“抓取”满⾜匹配最⻓字符串，在我们上⾯的例⼦⾥⾯，“.+”会从字符串的启始处抓取满⾜模式的最⻓字符，其中包括我们想得到的第⼀个整型字段的中的⼤部分，“\d+”只需⼀位字符就可以匹配，所以它匹配了数字“4”，⽽“.+”则匹配了从字符串起始到这个第⼀位数字4之前的所有字符
r=re.match(".+(\d+-\d+-\d+-\d+)",s)
print(r.group(1))
#⾮贪婪操作符“？”，这个操作符可以⽤在"*","+","?"的后⾯，要求正则匹配的越少越好
r=re.match(".+?(\d+-\d+-\d+-\d+)",s)
print(r.group(1))

test_str="<img data-original=https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973.jpg>"
s = re.match('<.+=(.*?)>',test_str)
print(s.group(1))

# r的作⽤
import re
mm = "c:\\a\\b\\c"
print(mm)#c:\a\b\c
ret = re.match("c:\\\\",mm).group()
print(ret)#c:\
ret = re.match("c:\\\\a",mm).group()
print(ret)#c:\a
ret = re.match(r"c:\\a",mm).group()
print(ret)#c:\a
ret = re.match(r"c:\a",mm).group()
print(ret)#AttributeError: 'NoneType' object has no attribute 'group'