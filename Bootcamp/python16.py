total=float(input("Enter total purchase amount: "))

premium_member=input("Are you a premium member? (yes/no): ").lower()

final_price = total

if total > 5000:
    final_price = total - (total * 0.25)
    
    if premium_member == "yes":
        final_price = final_price - (final_price * 0.05)

else:
    final_price = total - (total * 0.05)

print("\nOriginal Price:", total)

print("Price After Discount:", final_price)

