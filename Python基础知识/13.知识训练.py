# 列表合并

# 方法1
list2 = [1,2,56,4,3,4]
list1 = [2,45,65,563,3,2]
# 列表追加
a = list1+list2
# print(a)
zips = [ list(m) for m in zip(list2,list1)]
print(zips)

# 方法2
# list1.extend(list2)
# print(list1)
# 方法会改变原来的列表，而不是创建一个新的列表。

# 方法3
# 三、 * 运算符和 zip() 函数
zip1 = [item for pair in zip(list2,list1) for item in pair]
print(zip1)
# 将两个列表中对应位置的元素合并在一起

# 方法4
# 使用列表推导式 直接尾部添加 不是交叉添加
zip2 = [item for sublist in [list2,list1] for item in sublist]
print(zip2)

# 方法五
# itertools.chain() 合并列表
from  itertools import chain
merged_list = list(chain(list1,list2))
print(merged_list)