import pymysql

connection = pymysql.connect(
    host='localhost',
    user='munis',
    password='munis123',
    db='munis',
)
try:
    with connection.cursor() as cursor:
        sql = "DELETE FROM tasks WHERE id = %s"
        try:
            cursor.execute(sql, (1,))
            print("Successfully Deleted...")
        except:
            print("Oops! Something wrong")

    connection.commit()
finally:
    connection.close()