total = float(input("Enter cart total: "))
is_premium = input("Are you a premium member? (yes/no): ").lower() == "yes"

if total > 500:
    discount_rate = 0.15
    if is_premium:
        discount_rate += 0.15
else:
    discount_rate = 0.15

discount_amount = total * discount_rate
final_price = total - discount_amount

print(f"Original Price: {total}")
print(f"Discount: {discount_amount}")
print(f"Final Price: {final_price}")
