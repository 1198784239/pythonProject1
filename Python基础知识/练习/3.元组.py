# 让列表不可以被修改，以保护数据安全
# info2=(1,2,3)
# # info1=(1)
# # print(info2[0])
# # for i in info2:
# #     print(i)
# # print(info1)
# info=('likecong',20)
# print('我叫%s,今年%s岁'%info)
# # 元组和列表之间的转换 list tuple
# print(list(info))

# ------------zidian = {}
zidian = {
    '姓名':'lkc',
    '年龄':50
}
xiaoming = {"name": "小明",
            "age": 18,
            "gender": True,
            "height": 1.75}

# for k,v in zidian.items():
#     print(k,v)
# for k in zidian:
#     print(k,zidian[k])

print(zidian.items())
print(zidian.values())
# 取值
print(zidian.get('姓名'))
#增加
print(zidian.setdefault('地址','安徽'))
# 两个字典合并
print(zidian.update(xiaoming))
#删除
print(zidian.pop('年龄'))
print(zidian)
