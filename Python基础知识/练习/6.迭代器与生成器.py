# 字符串，列表或元组对象都可用于创建迭代器
# iter() 和 next()。
# import sys
# list1 = [1,2,3,4,5,6,7,8,9]
# it = iter(list1)# 创建迭代器对象
# # print(next(it))# 输出迭代器的下一个元素
# # print(next(it))
# # for i in it:
# #     print(i,end=' ')
#
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

class Mynumber:
    def __iter__(self):
        self.num = 1
        return self
    def __next__(self):
        if self.num <= 20:
            x = self.num
            self.num += 1
            return x
        else:
            raise StopIteration

mylist = Mynumber()
it = iter(mylist)

for i in it:
    print(i)
