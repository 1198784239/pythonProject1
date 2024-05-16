a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
zipped = zip(a,b)     # 打包为元组的列表
print(zipped)
print(list(zipped))

# 简化写 外加【】显示数据
print([list(x) for x in zip(a,b)])
#显示最短的
print([list(x) for x in zip(a,c)])