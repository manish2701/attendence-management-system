import mysql.connector

con = mysql.connector.connect(user='root', password='Manish@2701',host='localhost')

cursor = con.cursor()



#checking if database exists or not if not then creating it
cursor.execute("show databases;")
db_lst = cursor.fetchall()

db_name = "classes"

if (db_name,) in db_lst:
    cursor.execute("use classes")
else:
    cursor.execute("create database classes;")
    cursor.execute("use classes;")


#checking if table exists or not if not then creating it
cursor.execute("show tables;")
tb_lst = cursor.fetchall()

class_no = input("enter you class for which you have to create a management system :  ")
tb_name = f"class{class_no}"

if (tb_name,) in tb_lst:
    None
else:

    cursor.execute(f"CREATE TABLE class{class_no} (roll_no INT,name VARCHAR(30), gender VARCHAR(10) ,PRIMARY KEY (roll_no, name));")

    print(f"You have successfuly created a system for class {class_no}")

