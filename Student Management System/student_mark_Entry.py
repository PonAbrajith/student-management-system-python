


class Markentry():
    def __init__(self,students):

        self.students=students
    def add_mark(self):    
        student_mark = input("Enter Rollno: ")
        if student_mark in self.students:
         subject_1 = float(input("Enter mark: "))
         subject_2 = float(input("Enter mark: "))
         subject_3 = float(input("Enter mark: "))
         subject_4 = float(input("Enter mark: "))
         subject_5 = float(input("Enter mark: "))
         total = subject_1 + subject_2 + subject_3 + subject_4 + subject_5
         self.students[student_mark]["subject_1"] = subject_1
         self.students[student_mark]["subject_2"] = subject_2
         self.students[student_mark]["subject_3"] = subject_3
         self.students[student_mark]["subject_4"] = subject_4
         self.students[student_mark]["subject_5"] = subject_5
         self.students[student_mark]["total"] = total
         print("Mark added sucessfully")
        else:
           print(f"{student_mark} not founded")

    def display_mark(self):
       for student_mark,details in self.students.items():
        print(f"=============result===================")
        print(f"Roll no:{student_mark}")
        print(f"subject 1 : {details['subject_1']}")
        print(f"subject 2 : {details['subject_2']}")
        print(f"subject 3 : {details['subject_3']}")
        print(f"subject 4 : {details['subject_4']}")
        print(f"subject 5 : {details['subject_5']}")
        print(f"Total : {details['total']}")
        print("=========================================")







         
        