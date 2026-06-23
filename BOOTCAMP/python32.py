def student_report(name, marks):
    print("\n----- Student Report -----")
    print("Name :", name)
    print("Marks :", marks)


def add_bonus(marks):
    marks = marks + 5
    print("Inside Function Marks :", marks)


def sum_marks(n):
    if n == 1:
        return 1
    return n + sum_marks(n - 1)


def square(x):
    return x * x


def cube(x):
    return x * x * x


def apply_operation(func, value):
    return func(value)


name = input("Enter Student Name: ")
marks = int(input("Enter Marks: "))

student_report(name, marks)

add_bonus(marks)
print("Outside Function Marks:", marks)

n = int(input("\nEnter a number for recursive sum: "))
print("Recursive Sum =", sum_marks(n))

print("\nChoose Operation:")
print("1. Square")
print("2. Cube")

choice = int(input("Enter choice: "))
num = int(input("Enter a number: "))

if choice == 1:
    operation = square
elif choice == 2:
    operation = cube
else:
    print("Invalid Choice")
    exit()

result = apply_operation(operation, num)
print("Result =", result)