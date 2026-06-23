total = 0

while True:
    user_input = input("Enter numbers separated by commas: ")

    if "," not in user_input:
        print("Non-comma value entered. Exiting...")
        break

    numbers = user_input.split(",")

    even_found = False

    for num in numbers:
        num = int(num.strip())
        total += num

        if num % 2 == 0:
            even_found = True

    print("Sum =", total)

    if even_found:
        print("An even number was found in the sequence.")
        