# 列表(list)推导式
# 字典(dict)推导式
# 集合(set)推导式
# 元组(tuple)推导式
# [表达式 for 变量 in 列表]
# [out_exp_res for out_exp in input_list]
# 或者
# [表达式 for 变量 in 列表 if 条件]
# [out_exp_res for out_exp in input_list if condition]
# 过滤掉长度小于或等于3的字符串列表，并将剩下的转换成大写字母：
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names =[name.upper() for name in names if len(name)>=3]
print(new_names)
# 计算 30 以内可以被 3 整除的整数：
multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)

# 字典推导式---------
listdemo = ['Google','Runoob', 'Taobao']
# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
new_dic = [{key:len(key)} for key in listdemo]
print(new_dic)
print(type(new_dic))

# 提供三个数字，以三个数字为键，三个数字的平方为值来创建字典：
dic = {x: x**2 for x in (2, 4, 6)}
print(dic)
print(type(dic))


# 集合推导式---------
setnew = {i**2 for i in (1,2,3)}
print(setnew)
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a,type(a))

# 元组推导式（生成器表达式-------
a1 = (x for x in range(1,10))
print(a1)
# 使用 tuple() 函数，可以直接将生成器对象转换成元组
print(tuple(a1))