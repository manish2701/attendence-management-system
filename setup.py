import mysql.connector

con = mysql.connector.connect(user='root', password='Manish@2701',host='localhost')

cursor = con.cursor()

class_no = input("enter you class for which you have to create a management system :  ")

cursor.execute("create database classes;")

cursor.execute("use classes;")

cursor.execute(f"create table class{class_no} (roll_no int(10) primary key, name varchar(30), gender varchar(10));")


