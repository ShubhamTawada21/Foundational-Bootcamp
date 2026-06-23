num = 80

user_input = int(input("Enter a number: "))

while user_input != num:
    user_input = int(input("Wrong! Try again: "))

print("You entered 80. Condition matched!")