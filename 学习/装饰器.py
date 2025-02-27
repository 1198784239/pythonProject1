import time
from functools import wraps
# def outers(func):
#     @wraps(func)
#     def warrper(*args, **kwargs):
#         '''cdds'''
#         StartTime=time.time()
#         res=func(*args, **kwargs)
#         EndTime=time.time()
#         out=EndTime-StartTime
#         print(f"耗时:{out}")
#         return res
#
#     # warrper.__name__ = func.__name__
#     # warrper.__doc__ =func.__doc__
#
#     return warrper
#
# @outers
# def timeo():
#     '''cdd7s'''
#     time.sleep(1)
#     print("派送中")
#
#
# timeo()
# print(timeo.__name__)
# print(timeo.__doc__)

# def union(func):
#     def warrper(*args, **kwargs):
#         name=input("请输入账号:")
#         word=int(input("请输入密码:"))
#         if word==123:
#             res=func()
#             return res
#         else:
#             print("登陆失败")
#     return warrper
#
# @union
# def message():
#     time.sleep(2)
#     print("Welcome")
#
# message()

# 带参装饰器
# def d_outer(name):
#     def outers(func):
#         def warrper(*args, **kwargs):
#             print(name)
#             res=func(*args, **kwargs)
#             return res
#         return warrper()
#     return outers
# @d_outer("李克聪")
# def name():
#     print("welcom")


def g_union(source):
    def union(func):
        def warrper(*args, **kwargs):
            name=input("请输入账号:")
            word=int(input("请输入密码:"))
            if source =="file":
                if name=="jack" and word==123:
                    res=func()
                    print("文件登录")
                    return res
                else:
                    print("登陆失败")
            elif source=="mysql":
                print("mysql登录")
            elif source=="ldap":
                print("ldap")
            else:
                print("登陆错误")
        return warrper
    return union

# @g_union
# def message():
#     time.sleep(2)
#     print("Welcome")

@g_union(source="file")
def file():
    print("Welcome")

@g_union(source="mysql")
def mysql():
   pass
@g_union(source="ldap")
def ldap():
    pass
file()
mysql()
ldap()

