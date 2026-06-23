first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

if first_number > second_number:
    print(first_number, "is maximum")
elif second_number > first_number:
    print(second_number, "is maximum")
else:
    print("Both numbers are equal")
