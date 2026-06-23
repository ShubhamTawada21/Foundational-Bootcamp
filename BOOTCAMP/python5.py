students_db = [
    {"id": "101", "name": "Rahul Sharma", "age": 20, "grade": "A"},
    {"id": "102", "name": "Priya Patel", "age": 21, "grade": "B"},
]

def display_menu():
    print("\n=== STUDENT MANAGEMENT SYSTEM ===")
    print("1. Add New Student")
    print("2. View All Students")
    print("3. Search Student by ID")
    print("4. Delete Student")
    print("5. Exit")
    print("=================================")

def add_student():
    print("\n--- Add New Student ---")
    student_id = input("Enter Student ID: ").strip()

    for student in students_db:
        if student["id"] == student_id:
            print(" Error: A student with this ID already exists!")
            return

    name = input("Enter Student Name: ").strip()
    age = input("Enter Student Age: ").strip()
    grade = input("Enter Student Grade: ").strip()

    new_student = {
        "id": student_id,
        "name": name,
        "age": age,
        "grade": grade.upper(),
    }

    students_db.append(new_student)
    print(f" Student '{name}' added successfully!")


def view_students():
    print("\n--- List of All Students ---")
    if not students_db:
        print("No students found in the system.")
        return
    
    print(f"{'ID':<10} {'Name':<20} {'Age':<10} {'Grade':<10}")
    print("-" * 50)

    for student in students_db:
        print(
            f"{student['id']:<10} {student['name']:<20} {student['age']:<10} {student['grade']:<10}"
        )


def search_student():
    print("\n--- Search Student ---")
    search_id = input("Enter Student ID to search: ").strip()

    for student in students_db:
        if student["id"] == search_id:
            print("\nStudent Found:")
            print(f"ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Grade: {student['grade']}")
            return

    print(" Student not found.")


def delete_student():
    print("\n--- Delete Student ---")
    delete_id = input("Enter Student ID to delete: ").strip()

    for student in students_db:
        if student["id"] == delete_id:
            students_db.remove(student)
            print(f" Student with ID {delete_id} deleted successfully.")
            return

    print(" Student not found.")


# --- Main Program Loop ---
while True:
    display_menu()
    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("\nThank you for using the Student Management System. Goodbye!")
        break
    else:
        print(" Invalid choice! Please enter a number between 1 and 5.")