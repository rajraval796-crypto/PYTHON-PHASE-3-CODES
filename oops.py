# class Demo:
#     def __init__(self):
#         print("HELLO")

#     def hi(self):
#         print("hiiiiii")
        
# a=Demo()
# a.hi()

#------------------------------------------------ code 1 ------------------------------------------

# class University:
#     def __init__(self):
#         print("WELCOME TO THE UNIVERSITY")

#     def faculty(self):
#         print("WELCOME TO THE FACULTY LOBBY")

#     def student(self):
#         print("WELCOME TO THE STUDENT LOBBY")

# x=University()
# x.faculty()
# x.student()

#------------------------------------------------ code 2 ------------------------------------------


class Calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(self):
        print(f" THE ADDITION IS {self.a+self.b}")

    def subtraction(self):
        print(f" THE SUBTRACTION IS {self.a-self.b}")
       
a=Calc(10,20)
a.addition()
a.subtraction()
        
        