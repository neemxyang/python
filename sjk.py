# _*_ coding:utf-8 _8_
# 数据库mysql练习
# root 123456
import pymysql

db = pymysql.connect(
    host="localhost", 
    user="root", 
    password="123456", 
    db="world", 
    port=3306, 
    charset="utf8"
    )
cur = db.cursor()

sql = "select * from city;"
cur.execute(sql)
results = cur.fetchall()

n = []
for row in results:
    name = row[1]
    country = row[2]
    n.append([name,country])
m = []
# for i in n:
#     if n[i][1] == "CHN":
#       m.append([n[i]])  
print(len(n))
# print(m)
cur.close()
db.close()