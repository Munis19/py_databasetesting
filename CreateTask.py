import pymysql

connection = pymysql.connect(
    host='localhost',
    user='munis',
    password='munis123',
    db='munis',
)

title = input("Enter title of your task: ")
desc = input("Add some description to it: ")
date = input("Enter the date for this task (YYYY-MM-DD): ")

try:
    with connection.cursor() as cursor:
        sql = "INSERT INTO tasks (`title`, `descrip`, `date`) VALUES (%s, %s, %s)"
        try:
            cursor.execute(sql, (title, desc, date))
            print("Task added successfully")
        except:
            print("Oops! Something wrong")

    connection.commit()
finally:
    connection.close()