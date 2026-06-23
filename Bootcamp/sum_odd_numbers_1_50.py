sum_odd = 0
num = 1

while num <= 50:
    if num % 2 != 0:
        sum_odd += num
    num += 1

print("Sum of all odd numbers between 1 and 50:", sum_odd)