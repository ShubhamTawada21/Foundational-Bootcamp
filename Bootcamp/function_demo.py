def student_report(name, marks):
    print("\n----- Student Report -----")
    print(f"Name  : {name}")
    print(f"Marks : {marks}")
    print("--------------------------")


def add_bonus(marks):
    marks = marks + 5
    print(f"Inside Function Marks : {marks}")
    return marks


def sum_marks(n):
    if n <= 1:
        return n
    else:
        return n + sum_marks(n - 1)


def square(x):
    return x * x


def cube(x):
    return x**3


def apply_operation(func, value):
    return func(value)


def main():
    student_name = input("Enter Student Name: ")
    student_marks = int(input("Enter Marks: "))

    student_report(student_name, student_marks)

    add_bonus(student_marks)
    print(f"Outside Function Marks: {student_marks}")

    num_for_sum = int(input("\nEnter a number for recursive sum: "))
    recursive_result = sum_marks(num_for_sum)
    print(f"Recursive Sum = {recursive_result}")

    print("\nChoose Operation:")
    print(" 1. Square")
    print(" 2. Cube")

    choice = int(input("Enter Choice: "))
    number_to_operate = int(input("Enter Number: "))

    if choice == 1:
        chosen_function = square
    elif choice == 2:
        chosen_function = cube
    else:
        print("Invalid Choice!")
        return

    result = apply_operation(chosen_function, number_to_operate)
    print(f"\nResult = {result}")


if __name__ == "__main__":
    main()