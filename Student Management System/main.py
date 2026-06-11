from student_Enrollment import StudentEnroll
from student_mark_Entry import Markentry


enroll = StudentEnroll()

mark = Markentry(enroll.students)

while True:

    print("\n===== STUDENT MANAGEMENT =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Add Marks")
    print("5. Display Marks")
    print("6. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
     enroll.addstudents()

    elif choice == 2:
            enroll.display_students()

    elif choice == 3:
            enroll.search_student()

    elif choice == 4:
            mark.add_mark()

    elif choice == 5:
            mark.display_mark()

    elif choice == 6:
            print("Thank You")
            break