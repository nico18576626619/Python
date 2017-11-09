import pymysql
db=pymysql.connect('localhost','root','123456','mysql')
cur=db.cursor()
sql='SELECT * FROM engine_cost;'
cur.execute(sql)
data=cur.fetchall()
print(cur.arraysize)
# print(cur)
# for i in data:
#     print(i)
# print('database version{}'.format(data))

