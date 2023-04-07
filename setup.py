import mysql.connector

con = mysql.connector.connect(user='root', password='Manish@2701',host='localhost')

cursor = con.cursor()

class_no = input("enter the class for which you want to create a management system for :-")

cursor.execute(f"create database class{class_no};")

cursor.execute(f"use class{class_no};")

cursor.execute("create table students (roll_no int(10), name varchar(30), gender varchar(10);")


