import pymysql

con = pymysql.connect(host='localhost',
                      user='root',
                      password='123456',
                      charset='utf8',
                      database='test001',
                    autocommit=True         # 自动提交更改
                      )

cur = con.cursor()
sql = 'select DISTINCT NAME from test001.sheet1'
cur.execute(sql)
rows = cur.fetchall()
list = []
result=''
for row in rows:
    name = row[0]
    list.append(name)
print(list)
result=','.join(list)
print(result)
