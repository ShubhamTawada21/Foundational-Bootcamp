user_input = input("Enter an integer: ")

try:
    number = int(user_input)

    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")
except ValueError:
    print("Please enter a valid integer.")
   