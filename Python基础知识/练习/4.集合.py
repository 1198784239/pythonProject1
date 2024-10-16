import time
set1= {1,2,3,5}
# 使用 set() 函数从列表创建集合
set2= set([1,2,3,5])
# print(type(set1))
# print(type(set2))
print(1 in set1)
print(set2)
# 同样集合支持集合推导式(Set comprehension):
print({x for x in 'abracadabra' if x not in 'abc'})
def http_error(status):
    match status:
        case 401|403|404:
            return "Not allowed"

print(http_error(400))

# while True:
#     print(time.time())

for x in range(6):
  print(x)
else:
  print("Finally finished!")