import pymysql as db
import pymysql
# -----------------查询数据-------------------
con = pymysql.connect(host='localhost',
                      user='root',
                      password='123456',
                      charset='utf8',
                      database='lkcwork',
                    autocommit=True         # 自动提交更改
                      )
#
cur = con.cursor()
# cur.execute('select * from work')
# res=cur.fetchall()
# # cur.close()
# print(res)
# # ------------------添加数据------------------------
# sql ="INSERT INTO work (name,url) VALUES('xiaoli','hr')"
# cur.execute(sql)
# con.commit()
# print(res)
# ------------------更新数据------------------------
# # 前面是被更新 后面是更新的内容
# sql ="UPDATE work SET  name ='John' where url='hr'"
# res = cur.execute(sql)
# con.commit()
# print(res)
# # ------------删除数据------------
# sql ="DELETE from work where url='hr'"
# res = cur.execute(sql)
# con.commit()
# print(res)
# ----------查询数据------------
sql = 'select * from lkcwork.学员表'
cur.execute(sql)
rows = cur.fetchall()
for row in rows:
    print(row)