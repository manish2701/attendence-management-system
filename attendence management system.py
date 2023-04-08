
from datetime import date
import mysql.connector



con = mysql.connector.connect(user='root', password='Manish@2701', host='localhost', database='classes')
        
cursor = con.cursor()

class_no = input("Enter your class number : ")

#gets today's date
today = date.today()

def show_list_of_students():
    print()

    cursor.execute(f"select * from class{class_no};")
    rows=cursor.fetchall()
    
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


    while 2>1:
        return_input = int(input("\nPress 1 to return to dashboard : "))

        if return_input==1:
            dashboard()
            break
        else:
            None



def edit_list_of_students():
    print("\n=====List Of Students=====")
    print("1. add a student")
    print("2. remove a student")
    print("3. update data")
    print("4. exit \n")

    list_input = int(input("Enter the task number you want to do : "))

    if list_input==1:
        add_student()
    elif list_input==2:
        remove_student()
    elif list_input==3:
        update_student()
    elif list_input==4:
        dashboard()

def add_student():
    global name,roll_no,roll_lst,gender

    print("\nEnter details of the student below : \n")

    roll_no = int(input("roll number = "))

    cursor.execute(f"select * from class{class_no}")
    roll_lst = cursor.fetchall()


    for i in roll_lst:
        if roll_no==i[0]:
            print("This roll number already exists\n")
            add_student()
        else:
            None
        
    name = input("Name = ")

    print("\nGenders :- ")
    print("1. male")
    print("2. female")

    gen = int(input("Enter your gender number : "))

    if gen==1:
        gender = "male"
    elif gen==2:
        gender  = "female"

    cursor.execute(f"insert into class{class_no} values({roll_no},'{name}','{gender}');")
    con.commit()

    print("Your student details have been added")

    dashboard()

def remove_student():
    global roll_no,name,check


    cursor.execute(f"select * from class{class_no};")
    rows=cursor.fetchall()

    print("Roll No |          Name         ")

    for row in rows:
        for col in row:
            if col == row[-1]:
                break
            if col == row[1]:
                print(f'    {col.title()}')
            else:
                print(' '*2,col,end='\t|')

    print("\nEnter detail of student you want to remove : \n")

    roll_no = input("roll number = ")

    cursor.execute(f"select * from class{class_no} where roll_no = '{roll_no}';")
    check = cursor.fetchone()

    if check is not None:
        None
    else:
        remove_student()

    name = input("name = ")

    print(f"\nstudent data has been deleted where \n\nroll number is \t{roll_no} \nname is \t{name}")

    cursor.execute(f"delete from class{class_no} where roll_no={roll_no} and name='{name}';")
    con.commit()

def update_student():
    global roll_no,name,rollno

    print("Enter detail of student for which you have to update data :")
    roll_no = input("roll number = ")

    cursor.execute(f"select * from class{class_no} where roll_no = '{roll_no}';")
    check = cursor.fetchone()

    if check is not None:
        None
    else:
        print("\nEnter a roll number which is associated with a student")
        cursor.execute(f"select * from class{class_no};")
        rows=cursor.fetchall()

        print("\nRoll No |          Name         ")

        for row in rows:
            for col in row:
                if col == row[-1]:
                    break
                if col == row[1]:
                    print(f'    {col.title()}')
                else:
                    print(' '*2,col,end='\t|') 

        update_student()   

    name = input("name = ")

    def rollno():
        global new_roll_no
        print("\nEnter the NEW DETAILS of the student : ")

        new_roll_no = int(input("roll number = "))

        cursor.execute(f"select * from class{class_no} where roll_no = {new_roll_no};")
        check = cursor.fetchone()

        if check is not None:
            cursor.execute(f"select name from class{class_no} where roll_no = {new_roll_no}")
            exist_name = cursor.fetchall()
            for i in exist_name:
                for j in i:
                    the_name = j
            print(f"This roll number is occupied by {the_name}\n")
            rollno()
        else:
            None

    rollno()

    new_name = input("name = ")
        
    print("\nGenders :- ")
    print("1. male")
    print("2. female")

    gen = int(input("Enter your gender number : "))

    if gen==1:
        new_gender = "male"
    elif gen==2:
        new_gender  = "female"

    cursor.execute(f"update class{class_no} set roll_no = {new_roll_no}, name = '{new_name}', gender = '{new_gender}' where roll_no = {roll_no} or name = '{name}';")

    con.commit()
    dashboard()




def dashboard():
    print("\n======DASHBOARD======\n")
    print("1. show list of students")
    print("2. edit list of students")
    print("3. take attendence")
    print("4. show attendence \n")

    main_input = int(input("Enter the menu number you want to open : "))

    if main_input==1:
        show_list_of_students()
    elif main_input==2:
        edit_list_of_students()
        

dashboard()
