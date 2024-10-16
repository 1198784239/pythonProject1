a = 1198784239
b = [454,454,45]
# s =lambda a,b:a+b
# print(s(a,b))
print(list(map(str,b)))

m = '正确' if a>100 else '错误'
print(m)

reslut =[]
for i in range(10):
    if i%2==0:
        reslut.append(i)
print(reslut)

list=[x for x in range(10) if x%2==0]
print(list)

app = '李克聪'
list1 = [x for x in app ]
print(list1[1])