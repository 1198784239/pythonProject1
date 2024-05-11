import pymysql
db = pymysql.connect(host='localhost',
                     user='root',
                     password='123456',
                     database='lkcwork',
                     )
    #database是选择那个数据库
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# SQL 查询语句
sql = "SELECT * FROM 学员表 where ID=2"

try:
   # 执行SQL语句
   cursor.execute(sql)
   #获取数据
   print(cursor.fetchall())
except:
   print ("Error: unable to fetch data")

db.close()