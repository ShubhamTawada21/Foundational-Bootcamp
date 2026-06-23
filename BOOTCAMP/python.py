num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input("Enter fourth number: "))
num5 = float(input("Enter fifth number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    result = num1 + num2 + num3 + num4 + num5
    print("Result:", result)

elif operator == "-":
    result = num1 - num2 - num3 - num4 - num5
    print("Result:", result)

elif operator == "*":
    result = num1 * num2 * num3 * num4 * num5
    print("Result:", result)

elif operator == "/":

    if num2 == 0:
        print("Error: Cannot divide by zero!")
    else:
        result = num1 / num2 / num3 / num4 / num5
        print("Result:", result)

else:
    print("Invalid operator! Please use +, -, *, or /")
