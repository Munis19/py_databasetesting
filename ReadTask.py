import pymysql

connection = pymysql.connect(
    host='localhost',
    user='munis',
    password='munis123',
    db='munis',
)

try:
    with connection.cursor() as cursor:
        sql = "SELECT `id`, `title`, `descrip` FROM tasks WHERE `date` = CURDATE()"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()

            print("Id\t\t Title\t\t\t\t\tDescription")
            print("---------------------------------------------------------------------------")
            for row in result:
                print(str(row[0]) + "\t\t" + row[1] + "\t\t\t" + row[2])

        except:
            print("Oops! Something wrong")

    connection.commit()
finally:
    connection.close()

