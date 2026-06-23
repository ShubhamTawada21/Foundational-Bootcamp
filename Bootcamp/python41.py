class Employee:
    def __init__(self, name, department="General", bonus=0):
        self.name = name
        self.department = department
        self.bonus = bonus
        self.total_pay = 30000 + bonus

    def annual_summary(self):
        print(f"Employee Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Total Pay: {self.total_pay}")
        print("-" * 30)


emp1 = Employee("Alice", "Engineering", 5000)
emp2 = Employee("Bob", "Marketing")
emp3 = Employee("Charlie")

emp1.annual_summary()
emp2.annual_summary()
emp3.annual_summary()
