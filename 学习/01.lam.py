# a = 1198784239
# b = [454,454,45]
# # s =lambda a,b:a+b
# # print(s(a,b))
# print(list(map(str,b)))
#
# m = '正确' if a>100 else '错误'
# print(m)
#
# reslut =[]
# for i in range(10):
#     if i%2==0:
#         reslut.append(i)
# print(reslut)
#
# # list=[x for x in range(10) if x%2==0]
# # print(list)
#
# app = '李克聪'
# list1 = [x for x in app ]
# print(list1[1])

# 对列表中的每个元素进行平方操作
numbers = [1,2,3,4,5,6,7,8,9,10]
squared=list(map(lambda x: x ** 2,numbers))
print(squared)

# 对两个列表对应元素进行相加操作
list1 = [1, 2, 3]
list2 = [4, 5, 6]
sum1=list(map(lambda a,b: a+b,list1,list2))
print(sum1)

# 示例 3：将列表中的字符串转换为大写
words = ['apple', 'banana', 'cherry']
up=list(map(lambda word: word.upper(),words))
print(up)

# 处理嵌套列表并筛选数据
students = [
    ["Alice", 85, 90, 78],
    ["Bob", 70, 65, 72],
    ["Charlie", 92, 88, 95]
]

aver=list(map(lambda student:(student[0], sum(student[1:])/len(student[1:])),students))
sy=list(filter(lambda ok_student:ok_student[1]>80,aver))
print(sy)

# 例题 2：复杂字典数据处理
products = [
    {"name": "Apple", "price": 5, "stock": 100},
    {"name": "Banana", "price": 3, "stock": 200},
    {"name": "Cherry", "price": 8, "stock": 50}
]

total=list(map(lambda data:(data["name"],data["price"]* data["stock"]),products))
maxData=max(total,key=lambda x: x[1])
print(total)
print(maxData)

# 例题 3：字符串列表的复杂转换
sentences = [
    "hello world python",
    "this is a test",
    "data science is fun"
]
processed_sentences=list(map(lambda sentence:" ".join([word.capitalize() for word in sentence.split(" ") if len(word)>3]),sentences))
print(processed_sentences)