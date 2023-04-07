import mysql.connector

con = mysql.connector.connect(user='root', password='Manish@2701', host='localhost', database='classes')
        
cursor = con.cursor()

class_no = input("enter class number : ")


def show_name():
    print()
    cursor.execute(f"select * from class{class_no}")
    rows=cursor.fetchall()

    cursor.execute(f"desc class{class_no}")
    desc=cursor.fetchall()
    
    print("your list of students is below :\n")

    print("Roll No |          Name         ")

    for row in rows:
        for col in row:
            if col == row[-1]:
                break
            if col == row[1]:
                print(f'    {col.title()}')
            else:
                print(' '*2,col,end='\t|')
    

#use this in a systematic function when you return
show_name()
