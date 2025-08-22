from database import create_table
from student_manager import add_user, add_stds, view_users, view_stds, search_user, delete_user

def menu():
    print("\n==== Student Manager ====")
    print("1. Add User")
    print("2. Add Student")
    print("3. View User")
    print("4. View student")
    print("5. View all students and users")
    print("6. Exit")

def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-5): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)

        elif choice == '2':
            name = input("Enter student name: ")
            address = input("Enter student address: ")
            add_stds(name, address)

        elif choice == '3':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '4':
            students = view_stds()
            for user in students:
                print(user)
        elif choice == '5':
            users = view_users()
            for user in users:
                print("Users: ", user)

            students = view_stds()
            for user in students:
                print("Students: ", user)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
