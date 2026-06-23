income = float(input("Enter your monthly income: "))
emi = float(input("Enter your existing EMI: "))

if income < 30000:
    print("Not eligible for loan. Reason: Income too low.")
else:
    emi_limit = 0.4 * income
    
    if emi >= emi_limit:
        print("Not eligible for loan. Reason: High debt burden.")
    else:
        print("Eligible for loan.")