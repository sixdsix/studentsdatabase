import sqlite3
import time

conn = sqlite3.connect('/Users/nathanmiller/Documents/CPSC_Courses/CPSC_408/Assignment1/students.sqlite')  #
# establish connection to db
mycursor = conn.cursor()  # the cursor allows python to execute SQL statements

def welcome():
    while True:
        print('Welcome to the student database!')
        print('What would you like to do:')
        print('1. Display All Students and all of their attributes')
        print('2. Add New Students')
        print('3. Update Students')
        print('4. Delete Students')
        print('5. Search for Students')
        print('6. Exit')
        choice = input()

        if choice == '1':
            displayAll()
        elif choice == '2':
            addNew()
        elif choice == '3':
            updateStudent()
        elif choice == '4':
            deleteStudent()
        elif choice == '5':
            studentSearch()
        elif choice == '6':
            break
        else:
            print("ERROR: Please input only a integer value")

def displayAll():
    print('display all')
    mycursor.execute("SELECT StudentID, FirstName, LastName, Address, City, State, ZipCode, MobilePhoneNumber, Major, GPA, FacultyAdvisor FROM "
                     "Student WHERE isDeleted == 0;")
    rows = mycursor.fetchall()
    for row in rows:
        print(row)
    time.sleep(5)

def addNew():
    firstName = input('Enter First Name: ')
    while firstName.isnumeric() or not firstName.isalpha():
        print('ERROR: Must be Alphabetical')
        firstName = input('Enter First Name: ')

    lastName = input('Enter Last Name: ')
    while lastName.isnumeric() or not lastName.isalpha():
        print('ERROR: Must be Alphabetical')
        lastName = input('Enter Last Name: ')

    address = input('Enter Address: ')

    city = input('Enter City: ')
    while city.isnumeric():
        print('ERROR: Must be Alphabetical')
        city = input('Enter City: ')

    state = input('Enter State: ')
    while state.isnumeric() or not state.isalpha():
        print('ERROR: Must be Alphabetical')
        state = input('Enter State: ')

    zipCode = input('Enter Zip Code: ')
    while not zipCode.isnumeric():
        print('ERROR: Must be numeric')
        zipCode = input('Enter Zip Code: ')

    phoneNumber = input('Enter Phone Number: ')

    major = input('Enter Major: ')

    advisor = input('Input Advisor: ')

    boolean = True
    gpa = input('Enter GPA: ')
    while boolean:
        try:
            float(gpa)
            boolean = False
        except ValueError:
            print("ERROR: Must be a float")
            gpa = input('Enter GPA: ')
            boolean = True

    mycursor.execute("INSERT INTO Student('FirstName', 'LastName', 'Address', 'City', 'State', 'ZipCode', "
                     "'MobilePhoneNumber', 'Major', 'GPA', 'FacultyAdvisor','isDeleted') VALUES (?,?,?,?,?,?,?,?,?,?,?)"
                     , (firstName,lastName,address,city,state,zipCode,phoneNumber,major,gpa,advisor,0,))
    conn.commit()
    print('SUCCESS: Student has been added to the database')

def updateStudent():
    ID = input('What is the student ID of the student you seek to update?: ')
    while not ID.isnumeric():
        print('ERROR: Please enter a valid ID')
        ID = input('What is the student ID of the student you seek to update?: ')
    # grab the size of the database
    mycursor.execute("SELECT COUNT(*) FROM Student;")
    rows = mycursor.fetchall()
    # check to make sure it is inside the size of the database
    while int(ID) > int(rows[0][0]) and not ID.isnumeric():
        print('ERROR: Please enter a valid ID')
        ID = input('What is the student ID of the student you seek to update?: ')

    print('What would you like to update on the student record?')
    print('1. Major')
    print('2. Advisor')
    print('3. MobilePhoneNumber')
    choice = input()

    while True:
        if choice == '1':
            major = input('What would you like to change their major to?: ')
            while major.isnumeric() or not major.isalpha():
                print('ERROR: Must be Alphabetical')
                state = input('Enter Major: ')

            mycursor.execute("UPDATE Student Set Major = ? WHERE StudentID = ?;", (major, ID,))
            conn.commit()
            break
        elif choice == '2':
            advisor = input('Who would you like to change their advisor to?: ')
            mycursor.execute("UPDATE Student Set FacultyAdvisor = ? WHERE StudentID = ?;", (advisor, ID,))
            conn.commit()
            break
        elif choice == '3':
            phoneNumber = input('Enter Phone Number: ')
            mycursor.execute("UPDATE Student Set MobilePhoneNumber = ? WHERE StudentID = ?;", (phoneNumber, ID,))
            conn.commit()
            break
        else:
            print("ERROR: Please enter a valid choice")



def deleteStudent():
    ID = input('What is the student ID of the student you seek to delete?: ')
    while not ID.isnumeric():
        print('ERROR: Please enter a valid ID')
        ID = input('What is the student ID of the student you seek to delete?: ')
    # grab the size of the database
    mycursor.execute("SELECT COUNT(*) FROM Student;")
    rows = mycursor.fetchall()
    # check to make sure it is inside the size of the database
    while int(ID) > int(rows[0][0]) and not ID.isnumeric():
        print('ERROR: Please enter a valid ID')
        ID = input('What is the student ID of the student you seek to delete?: ')

    while True:
        choice = input('Are you sure you want to delete this user y/n?')
        if choice == 'y':
            # delete student
            mycursor.execute("UPDATE Student Set isDeleted = ? WHERE StudentID = ?;", (1, ID,))
            conn.commit()
            print('Student Successfully deleted')
            break
        elif choice == 'n':
            break
        else:
            print("ERROR: Please enter y/n")

def studentSearch():
    print('What would you like to search for on the student record?')
    print('1. Major')
    print('2. GPU')
    print('3. City')
    print('4. State')
    print('5. Advisor')
    choice = input()

    while True:
        if choice == '1':
            major = input('Enter a Major: ')
            mycursor.execute("SELECT FirstName, LastName, Address, City, State, ZipCode, MobilePhoneNumber, FacultyAdvisor, Major,"
                             " GPA FROM Student WHERE Major = ? AND isDeleted = 0;", (major,))
            rows = mycursor.fetchall()
            for row in rows:
                print(row)
            break
        elif choice == '2':
            # gpu search
            boolean = True
            gpa = input('Enter GPA: ')
            while boolean:
                try:
                    float(gpa)
                    boolean = False
                except ValueError:
                    print("ERROR: Must be a float")
                    gpa = input('Enter GPA: ')
                    boolean = True
            mycursor.execute("SELECT FirstName, LastName, Address, City, State, ZipCode, MobilePhoneNumber, FacultyAdvisor, Major, "
                             "GPA FROM Student WHERE GPA = ? AND isDeleted = 0;",(gpa,))
            rows = mycursor.fetchall()
            for row in rows:
                print(row)
            break
        elif choice == '3':
            # city search
            city = input('Enter City: ')
            while city.isnumeric():
                print('ERROR: Must be Alphabetical')
                city = input('Enter City: ')
            mycursor.execute("SELECT FirstName, LastName, Address, City, State, ZipCode, MobilePhoneNumber, FacultyAdvisor, Major, "
                             "GPA FROM Student WHERE City = ? AND isDeleted = 0;",(city,))
            rows = mycursor.fetchall()
            for row in rows:
                print(row)
            break
        elif choice == '4':
            state = input('Enter State: ')
            while state.isnumeric() or not state.isalpha():
                print('ERROR: Must be Alphabetical')
                state = input('Enter State: ')
            mycursor.execute("SELECT FirstName, LastName, Address, City, State, ZipCode, MobilePhoneNumber, FacultyAdvisor, Major, "
                             "GPA FROM Student WHERE State = ? AND isDeleted = 0;",(state,))
            rows = mycursor.fetchall()
            for row in rows:
                print(row)
            break
            # state search
        elif choice == '5':
            advisor = input('Input Advisor: ')
            mycursor.execute("SELECT FirstName, LastName, Address, City, State, ZipCode, MobilePhoneNumber, Major, "
                             "GPA FROM Student WHERE FacultyAdvisor = ? AND isDeleted = 0;",(advisor,))
            rows = mycursor.fetchall()
            for row in rows:
                print(row)
            # advisor search
            break
        else:
            print("ERROR: Please enter a valid number")
welcome()

mycursor.close()
