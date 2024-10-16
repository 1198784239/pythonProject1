str = ' Hello  word  dsds  '
str1 = ' Hello \n word \r dsds  '
# print(str[:4])
# 循环字符串的索引和内容
# for i,el in enumerate(str):
#     print(i,el)
# 寻找字符的索引 只能选择第一个搜索到的
# print(str.find('l'))
# 寻找字符在字符串里
# print("m" in str)0
# 后两个参数指定范围
# print(str.index('e',1,3))
# 查找指定的字符的个数
# print(str.count('l'))
# 后面是指定替换的个数
# print(str.replace('l','m',2))
# 后面是分割次数
# print(str.split(' ',2))
# 去除收尾的空格/字符
# print(str.strip())
# 全部转化为大写或小写
# print(str.upper())

# --------拆分---------
# 把字符串 string 分成一个 3 元素的元组 (str前面, str, str后面)
# print(str.partition('e'))
# 以 str 为分隔符拆分 string，如果 num 有指定值，则仅分隔 num + 1 个子字符串，str 默认包含 ‘\r’, ‘\t’, ‘\n’ 和空格
# print(str.split('e'))
# 按照换行符进行分割
# print(str1.splitlines())
# str3 = 'like'
# # print(str.join(str3))
# a = str3+str
# print(a)