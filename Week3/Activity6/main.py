from database import create_table
from yoobee_manage import add_student, add_lecturer, add_class, delete_students, view_student

def menu():
    print("\n==== Yoobee Manager ====")
    print("1. Add Student")
    print("2. Add lecturer")
    print("3. Add class")
    print("4. View Students")
    print("5. Delete Students by ID")
    print("6. Exit")

def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option(1-5): ")
        if choice == "1":
            name = input("Please enter student name: ")
            address = input("Please enter student address: ")
            email = input("Please enter student email: ")
            add_student(name, address, email)

        elif choice == "2":
            name = input("Please enter lecturer name: ")
            email = input("Enter email: ")
            department = input("Enter department")
            add_lecturer(name, email, department)
        elif choice == "3":
            class_room = input("Please enter room no.: ")
            add_class(class_room)
        elif choice =="4":
            students = view_student()
            for user in students:
                print(user)

        elif choice =="5":
            std_id = int(input("Enter the student id to delete: "))
            delete_students(std_id)
        elif choice == "6":
            print("Good Bye")
            break 
        else:
            print("Invalid choice, try again!")



if __name__=="__main__":
    main()