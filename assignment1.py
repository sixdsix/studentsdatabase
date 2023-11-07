# This is a sample Python script.
import sqlite3
import csv

conn = sqlite3.connect('/Users/nathanmiller/Documents/CPSC_Courses/CPSC_408/Assignment1/students.sqlite') # establish connection to db
mycursor = conn.cursor() # the cursor allows python to execute SQL statements

with open('/Users/nathanmiller/Documents/CPSC_Courses/CPSC_408/Assignment1/students.csv') as csv_file:
    freader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for row in freader:
        if line_count == 0:
            line_count+=1
        else:
            mycursor.execute("INSERT INTO Student('FirstName', 'LastName', 'Address', 'City', 'State', 'ZipCode', 'MobilePhoneNumber', 'Major', 'GPA', 'isDeleted') VALUES (?,?,?,?,?,?,?,?,?,?)", (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],0,))


conn.commit()
mycursor.close()


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
