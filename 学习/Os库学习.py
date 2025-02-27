import os

# 获取当前项目的目录
# get=os.getcwd()
# print(get)
# 显示当前使用的平台
# print(os.name)
# 改变当前工作目录到指定的路径。
# os.chdir('C:\\Users\李克聪\\PycharmProjects\\pythonProject1\\图片爬取')
# os.getcwd()
# print(os.getcwd())
# os.chdir() 方法用于改变当前的工作目录
# new_dir = '/path/to/new/directory'
# os.chdir(new_dir)
# print(f"已将工作目录更改为: {os.getcwd()}")
# 创建文件夹
# os.makedirs('C:/Users/李克聪/PycharmProjects/pythonProject1/图片爬取/111', mode=0o777)
# # 创建文件不是文件夹
# os.mkdir('C:/Users/李克聪/PycharmProjects/pythonProject1/图片爬取/12', mode=0o777)
# print('完成')

# 列出目录下的所有文件和文件夹
# m=os.listdir('C:/Users/李克聪/PycharmProjects/pythonProject1/图片爬取')
# print(m)

# 删除指定路径的文件  os.remove（）
# s =os.remove('C:/Users/李克聪/PycharmProjects/pythonProject1/图片爬取/loging.txt')

# rename =os.rename('C:/Users/李克聪/PycharmProjects/pythonProject1/图片爬取/12',"444")
# src -- 要修改的目录名 命名文件或目录,能对相应的文件进行重命名
# dst -- 修改后的目录名
# data = 'C:/Users/李克聪/PycharmProjects/pythonProject1/学习'
# os.chdir(data)#设置工作空间
# print(os.getcwd())
# os.rename('C:/Users/李克聪/PycharmProjects/pythonProject1/学习/444',"520")


# directory='.学习',
# files = os.listdir(directory)
# for i in files:
#     print(i)

# os.renames() 用于递归重命名目录或文件

# print(os.path.abspath('12.py'))#返回绝对路径
# print(os.path.basename('C:/Users/李克聪/PycharmProjects/pythonProject1/学习'))

# 路径 path 存在，返回 True；如果路径 path 不存在，返回 False
a=os.path.exists('C:/Users/李克聪/PycharmProjects/pythonProject1/学习')
b=os.path.exists('C:/Users/李克聪/PycharmProjects/pythonProject1/学习1')
print(a,b)

s = os.path.join('C:/Users','wuzhengxiang/Desktop/','股票数据分析')
print(s)

Path1 = 'home'
Path2 = 'develop'
Path3 = 'code'
Path4=Path1+Path2+Path3
print(Path4)
m=os.path.join(Path1,Path2,Path3)
print(m)

# os.path.split把路径分割成 dirname 和 basename，返回一个元组
print(os.path.split(r'D:\Python\test\data.txt'))
# os.path.splitdrive()os.path.splitdrive()
print(os.path.splitdrive(r'D:\Python\test\data.txt'))
print(os.path.splitext(r'D:\Python\test\data.txt'))

# os.path.walk(arg, dirname, names)遍历path
# dirname表示当前目录的目录名，names代表当前目录下的所有文件名，args则为walk的第三个参数
# print(list(os.walk('C:/Users/李克聪/PycharmProjects/pythonProject1/学习')))

abs_cur='C:/Users/李克聪/PycharmProjects/pythonProject1/学习'
file_url=[]
for i,x,y in os.walk(abs_cur):
    for file in y:
        file_url.append(os.path.join(abs_cur,file))
print(file_url,len(file_url))