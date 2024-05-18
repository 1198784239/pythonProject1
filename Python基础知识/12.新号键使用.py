# 1.*乘法
# print(2*3)



#2.长参数
def num(*args,**kwargs):
    m = args[1]
    s = kwargs.items()
    for i in s:
        print(i[0],i[1])
    # print(m)
    # print(s)
    # print(args)
    # print(kwargs)

Num = num(1,2,3,4,5 , a=1,b=2,c=3)


a = [1,2,3,4,5]
b =[5,6,7,8,9]
print([s for s in zip(a,b)])

for s in zip(a,b):
    print(list(s))