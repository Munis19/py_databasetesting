import pymysql

connection = pymysql.connect(
    host='localhost',
    user='munis',
    password='munis123',
    db='munis',
)
try:
    with connection.cursor() as cursor:
        sql = "UPDATE tasks SET `title`=%s, `descrip`=%s WHERE `id` = %s"
        try:
            cursor.execute(sql, ('go to fish market', 'buy fresh fishes', 1))
            print("Successfully Updated...")
        except:
            print("Oops! Something wrong")

    connection.commit()
finally:
    connection.close()