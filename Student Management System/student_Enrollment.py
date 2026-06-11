class StudentEnroll:
    def __init__(self):
        self.students={}
        
     
    def addstudents(self):
      n = int(input("Total number students: "))
      for i in range(n):
        rollno = input("Enter Roll no: ")
        name = str(input("Name: "))
        course = str(input("course: "))
        section = str(input("section: "))


        self.students[rollno] ={
            "name":name,
            "course":course,
            "section":section

        }
        
    def display_students(self):
       
         for rollno,details in self.students.items():
                print("\n=========student Detail==========")
                print(f"Name: {details['name']}")
                print(f"Rollno: {rollno}")
                print(f"course : {details['course']}")
                print(f"section : {details['section']}")
                print("====================================")
    def search_student(self):
            print("========Search student==========")
            search = input("Search student: ")
            if search in self.students:
                details = self.students[search]
                print("\n=========student Detail==========")
                print(f"Name: {details['name']}")
                print(f"Rollno: {search}")
                print(f"course : {details['course']}")
                print(f"section : {details['section']}")
                print("====================================")
            else:
                print(f"{search} not found.")
    def remove_student(self):
         print("=======Remove student=======")
         remove = input("Remove student: ")
         if remove in self.students:
              del self.students[remove]
         else:
              print(f"{remove} not found.")
    def update_student(self):
     print("=======remove student===========")
     rollno = input("Enter Roll No: ")

     if rollno in self.students:

        print("1. Name")
        print("2. Course")
        print("3. Section")

        choice = int(input("What do you want to update? "))

        if choice == 1:
            self.students[rollno]["name"] = input("New Name: ")

        elif choice == 2:
            self.students[rollno]["course"] = input("New Course: ")

        elif choice == 3:
            self.students[rollno]["section"] = input("New Section: ")

        print("Updated Successfully")

     else:
        print("Student Not Found")
         
              

         
         
         





