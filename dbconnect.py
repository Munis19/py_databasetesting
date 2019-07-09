import pymysql


db = pymysql.connect("localhost", "munis", "munis123", "munis")


cursor = db.cursor()


cursor.execute("SELECT VERSION()")


data = cursor.fetchone()
print("Database version : %s " % data)

# disconnect from server
db.close()
