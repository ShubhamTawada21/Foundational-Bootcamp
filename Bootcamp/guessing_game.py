SECRET_NUMBER = 42

guess = int(input("Guess the secret number: "))

if guess == SECRET_NUMBER:
    print("Correct!")
else:
    difference = abs(SECRET_NUMBER - guess)
    
    if guess < SECRET_NUMBER:
        print("Too low")
        print(f"You are {difference} below the number")
    else:
        print("Too high")
        print(f"You are {difference} above the number")