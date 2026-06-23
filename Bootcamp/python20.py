n = int(input("Enter a number: "))

if n > 0:
    if n % 2 == 0:
        print("Positive even")
    else:
        print("Positive odd")
elif n < 0:
    print("Negative")
else:
    print("Zero")
    