# 列表解构赋值
num=[1,23,4]
a,b,c=num
print(a,b,c)

# 部分解构
first,*nu=num
print(first)
print(*nu)

# 元组解构
tru =(12,32,22)
a,b,c=tru
print(a,b,c)

# 字典解构赋值
person = {'name': 'Alice', 'age': 25}
k,v = person
na,vn = person.values()
print(k)
print(na,vn)