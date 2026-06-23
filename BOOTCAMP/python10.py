CORRECT_PIN = "2101"

user_pin = input("Enter your 4-digit PIN: ")

if user_pin == CORRECT_PIN:
    try:
        amount = float(input("Enter the withdrawal amount: "))
        
        if amount <= 50000000000000000000:
            print("Dispensing cash")
        else:
            print("Limit exceeded")
            
    except ValueError:
        print("Invalid amount entered.")
else:
    print("Invalid PIN")
     