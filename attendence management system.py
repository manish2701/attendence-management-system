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

def add_student():
    global name,roll_no,roll_lst,gender
    print()
    print("Enter details of the student below : \n")

    roll_no = int(input("roll number = "))

    cursor.execute(f"select * from class{class_no}")
    roll_lst = cursor.fetchall()

    for i in roll_lst:
        if roll_no==i[0]:
            print("This roll number already exists\n")
            break
        
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
    edit_list_of_students()


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
        None
    elif list_input==3:
        None
    elif list_input==4:
        dashboard


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
