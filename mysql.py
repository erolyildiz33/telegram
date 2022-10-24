import os
os.system("""python -m pip install PyMySQL""")
import pymysql.cursors
db = pymysql.connect(host='185.136.84.129', #'185.136.84.129',
                             user='maydryco_telegraf',#'maydryco_telegraf',
                             password='Telgraf33!',#'Telgraf33!',
                             db='maydryco_telegraf',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
baglanti = db.cursor()
userid="erol"
sql="SELECT * FROM users WHERE apiid=%s"
baglanti.execute(sql,userid)
exist = baglanti.fetchone()
if exist is None:
    newsql="INSERT INTO users (apiid) VALUES (%s)"
    baglanti.execute(newsql, (userid))
    db.commit()
else:
     print(exist["search_key"])
baglanti.close()

#sql = "INSERT INTO users (None,apiid)VALUES (%s,%s)"
#val = ("Ram")
   
#baglanti.execute(sql, val)
#baglanti.commit()

