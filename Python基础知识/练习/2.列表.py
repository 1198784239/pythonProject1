list = [2,34,3454,767]
# 1.添加
str = 'Hello Python'
# list.append(str)
m = '343'
# 将列表2 的数据追加到列表
# list.extend(m)
list.insert(2,44)
print(list)
print(len(list))

#2.修改
list[3] = 11
print(list)

# 3.删除
list.remove(34)
# 删除末尾数据
list.pop()
list.pop(2)
# 删除指定索引的数据
del list[0]
print(list)

# 4.统计
print(len(list))
# print(list.count())

# 排序
list1= [2343,34,3454,767]
mm = list1.sort()
print(mm)
