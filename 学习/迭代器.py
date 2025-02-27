# list=['1','s','3']
# num=0
# while num<len(list):
#     print(list[num])
#     num=num+1

# 迭代器 字典，集合，文件
# iter()
l=[1,2,3,4,5]
m=iter(l)
s='张大仙'
q=iter(s)
j=(1,2,3,4,5)
iter(j)
z={'name':'sdsd','age':23}
mm=iter(z)
# print(next(q))
# print(next(m))
# print(next(m))

while True:
    try:
        print(next(mm))
    except StopIteration:
        break
# print(next(mm))
# print(next(mm))
# print(next(mm,None))

x=11
y=10
# 三元表达式
res= 12 if x>y else 55
print(res)

# 列表生成式
s=['老坛酸菜','牛肉面','老谭酸菜']
li=[]
# for i in s:
#     if i.endswith("酸菜"):
#         li.append(i)
# print(li)

new_list=[i for i in s if i.endswith("酸菜")]
new_list1=[i for i in s if True]
new_list2=[i.replace('酸菜',"1") for i in s if i.endswith("酸菜")]
print(new_list)
print(new_list1)
print(new_list2)

# # 字典生成式
# s=['老坛酸菜','牛肉面','老谭酸菜']
# res={name:5 for name in s}
# print(res,type(res))
#
# # 集合生成式
# s=['老坛酸菜','牛肉面','老谭酸菜']
# res={name for name in s}
# print(res,type(res))

m=[('老坛酸菜',5),('牛肉面',6),('老谭酸菜',8)]
res1={k:v for k,v in m if not k.startswith("老")}
print(res1,type(res1))

# 元组生成式
s=['老坛酸菜','牛肉面','老谭酸菜']
res=(name for name in s)
print(next(res))
print(res.send(11))