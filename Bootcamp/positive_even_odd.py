num = int(input("Enter a number: "))

if num > 0:
    print("The number is Positive")

    if num % 2 == 0:
        print("The number is Even")
    else:
        print("The number is Odd")

elif num < 0:
    print("The number is Negative")

else:
    print("The number is Zero")