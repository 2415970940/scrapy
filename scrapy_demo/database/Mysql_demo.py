import pymysql

conn = pymysql.connect(host="localhost",user="root",password="123",
                       database="school",port=3306,charset='utf8')
cursor = conn.cursor()

# sql = """select * from info_student"""
# cursor.execute(sql)
# result = cursor.fetchall()
# print(result)

sql = """insert into info_student(name,banji_id) values(%s,%s)"""
name="史诗"
banji_id="2"
cursor.execute(sql,(name,banji_id))
conn.commit()


cursor.close()