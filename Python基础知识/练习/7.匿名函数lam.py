# lambda [arg1 [,arg2,.....argn]]:expression

x = lambda a,b: a+b
print(x(1,2))


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

f = lambda: "Hello, world!"
print(f())  # 输出: Hello, world!

# lambda 函数通常与内置函数如 map()、filter() 和 reduce() 一起使用，以便在集合上执行操作
numbers = [1, 2, 3, 4, 5]
squared =list(map(lambda n: n**2, numbers))
print(squared)
# 使用 lambda 函数与 filter() 一起，筛选偶数
squared1 =list(filter(lambda n: n%2==0, numbers))
print(squared1)
# 下面是一个使用 reduce() 和 lambda 表达式演示如何计算一个序列的累积乘积：
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# 使用 reduce() 和 lambda 函数计算乘积
product = reduce(lambda x, y: x * y, numbers)

print(product)  # 输出：120