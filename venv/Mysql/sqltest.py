import pymysql
db = pymysql.connect(host="localhost",user="root",
        password="Qq379248402",db="sakila",port=3306)

cur = db.cursor()
cur.execute("SELECT VERSION()")
data = cur.fetchone()
print ("Database version : %s " % data)