'''
Write a program to build a simple Student Management System using Object Oriented Programming in Python which can perform the following operations:
accept-This method takes details from the user like name, roll number, and marks for two different subjects. 
display-This method displays the details of every student.
search-This method searches for a particular student from the list of students. This method will ask the user for roll number and then search according to the roll number
delete-This method deletes the record of a particular student with a matching roll number.
update-This method updates the roll number of the student. This method will ask for the old roll number and new roll number. It will replace the old roll number with a new roll number.
The following instructions need to be considered while making a program.
1.	Give class name as Student
2.	Include methods name as accept, display, search, delete and update. (1 mark for each correct method to be formed).
3.	Also form constructor with __init__ () method (2 marks for forming constructor).
4.	2 marks for correct object prepared like after deletion of one roll no of student it should update the list with new roll no. and should display it.
The example is just for understanding but logic should be for any n number of students.For Example:
List of Students
Name   :  A
RollNo :  1
Marks1 :  100
Marks2 :  100
Name   :  B
RollNo :  2
Marks1 :  90
Marks2 :  90

'''
class Student:
    def __init__(self,name=""):
        self.name=name
        self.rollno=0
        self.m1=0
        self.m2=0
        self.student_list=[]
    def accept(self):
        name=input("ENTER NAME:")
        rollno=int(input("ENTER ROLL NO:"))
        m1=int(input("ENTER MARKS FOR SUBJECT 1:"))
        m2=int(input("ENTER MARKS FOR SUBJECT 2:"))
        self.student_list.append({
            "name": name,
            "RollNo":rollno,
            "Marks1":m1,
            "Marks2":m2
        })

    def display(self):
        if self.student_list:
            print("LIST OF STUDENTS")
            for i in self.student_list:
                print("NAME:",i["name"])
                print("ROLLNO:",i["RollNo"])
                print("MARKS1:",i["Marks1"])
                print("MARKS2:",i["Marks2"])
        else:
            print("student not found")

    def search(self):
        tr=int(input("ENTER ROLL NO TO SEARCH:"))
        for i in self.student_list:
            if i["RollNo"]==tr:
                print("NAME:",i["name"])
                print("ROLLNO:",i["RollNo"])
                print("MARKS1:",i["Marks1"])
                print("MARKS2:",i["Marks2"])
                return
        print("student not found")
    def delete(self):
        tr=int(input("ENTER ROLL NO TO SEARCH:"))
        for i in self.student_list:
            if i["RollNo"]==tr:
                self.student_list.remove(i)
                self.display()
                return
            
        print("student not found")

    def update(self):
        old=int(input("ENTER OLD ROLL NO:"))
        new=int(input("ENTER NEW ROLL NO:"))
        for i in self.student_list:
            if i["RollNo"]==old:
                i["RollNo"]=new
                print("UPDATED SUCCESSFULLY!")
                self.display()
                return
            
        print("student not found")
            

a=Student()
while True:
    print("\n1.Accept  2.Display  3.Search  4.Delete  5.Update  6.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        a.accept()
    elif ch == 2:
        a.display()
    elif ch == 3:
        a.search()
    elif ch == 4:
        a.delete()
    elif ch == 5:
        a.update()
    elif ch == 6:
        break



# class Student:
#     def __init__(self, name="", rollno=0, marks1=0, marks2=0):
#         self.name = name
#         self.rollno = rollno
#         self.marks1 = marks1
#         self.marks2 = marks2
#         self.students = []

#     def accept(self):
#         name = input("Enter Name: ")
#         rollno = int(input("Enter Roll Number: "))
#         marks1 = int(input("Enter Marks 1: "))
#         marks2 = int(input("Enter Marks 2: "))
#         self.students.append({
#             "name": name,
#             "rollno": rollno,
#             "marks1": marks1,
#             "marks2": marks2
#         })

#     def display(self):
#         if not self.students:
#             print("No records found.")
#             return
#         print("List of Students")
#         for s in self.students:
#             print("Name   : ", s["name"])
#             print("RollNo : ", s["rollno"])
#             print("Marks1 : ", s["marks1"])
#             print("Marks2 : ", s["marks2"])

#     def search(self):
#         roll = int(input("Enter Roll Number to search: "))
#         for s in self.students:
#             if s["rollno"] == roll:
#                 print("Name   : ", s["name"])
#                 print("RollNo : ", s["rollno"])
#                 print("Marks1 : ", s["marks1"])
#                 print("Marks2 : ", s["marks2"])
#                 return
#         print("Student not found.")

#     def delete(self):
#         roll = int(input("Enter Roll Number to delete: "))
#         for s in self.students:
#             if s["rollno"] == roll:
#                 self.students.remove(s)
#                 print("Record deleted.")
#                 self.display()
#                 return
#         print("Student not found.")

#     def update(self):
#         old_roll = int(input("Enter Old Roll Number: "))
#         new_roll = int(input("Enter New Roll Number: "))
#         for s in self.students:
#             if s["rollno"] == old_roll:
#                 s["rollno"] = new_roll
#                 print("Roll number updated.")
#                 self.display()
#                 return
#         print("Student not found.")


# obj = Student()
# while True:
    # print("\n1.Accept  2.Display  3.Search  4.Delete  5.Update  6.Exit")
    # ch = int(input("Enter choice: "))
    # if ch == 1:
    #     obj.accept()
    # elif ch == 2:
    #     obj.display()
    # elif ch == 3:
    #     obj.search()
    # elif ch == 4:
    #     obj.delete()
    # elif ch == 5:
    #     obj.update()
    # elif ch == 6:
    #     break