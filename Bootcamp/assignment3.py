class Person:
    def __init__(self, name):
        self.name = name
    def show_person(self):
        print("Name:", self.name)
class Teacher(Person):
    def __init__(self, name, subjects):
        super().__init__(name)
        self.subjects = subjects
    def teach(self):
        print(self.name, "teaches:", ", ".join(self.subjects))
class AdminStaff(Person):
    def __init__(self, name, designation):
        super().__init__(name)
        self.designation = designation
    def admin_task(self):
        print(self.name, "handles", self.designation, "work")
class TeacherAdmin(Teacher, AdminStaff):
    def __init__(self, name, subjects, designation):
        Person.__init__(self, name)
        self.subjects = subjects
        self.designation = designation
person1 = Person("Rahul")
teacher1 = Teacher("Anita", ["Math", "Science"])
admin1 = AdminStaff("Vikas", "Office Manager")
teacher_admin = TeacherAdmin(
    "Neha",
    ["English", "Computer"],
    "Department Coordinator"
)
print("Person Details")
person1.show_person()
print("\nTeacher Details")
teacher1.show_person()
teacher1.teach()
print("\nAdmin Details")
admin1.show_person()
admin1.admin_task()
print("\nTeacher Admin Details")
teacher_admin.show_person()
teacher_admin.teach()
teacher_admin.admin_task()
print("\nMethod Resolution Order:")
print(TeacherAdmin.mro())