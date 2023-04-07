import mysql.connector

con = mysql.connector.connect(user='root', password='Manish@2701', host='localhost', database='classes')
        
cursor = con.cursor()

class_no = input("enter class number : ")



cursor.execute(f"select * from class{class_no}")

rows=cursor.fetchall()


for row in rows:
    for col in row:
        print(col,end=' ')
    print()
    

