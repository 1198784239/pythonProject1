#
# def decorator_function(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
# #     return wrapper
# def decorator_function(func):
#     def wrapper(*args, **kwargs):
#         for arg in args:
#             try:
#                 arg = float(arg)
#             except:
#                 print('只能浮点运算')
#                 return
#         return func(*args, **kwargs)
#     return wrapper
#
# @decorator_function
# def musum(*args):
#     return sum(args)
#
# print(musum(1,2,3,4))

# new_musum = decorator_function(musum)

# print(new_musum(1,2,3))
# print(musum(1,2,3))

import time

def jishi(func):
    def inner(*args, **kwargs):
        start = time.time()
        func()#被装饰的函数
        end = time.time()
        print("耗时",end - start)
        # return func()
    return inner

@jishi
def ab():
    list = []
    for i in range(10001):
        list.append(i)
    print(list)

ab()

