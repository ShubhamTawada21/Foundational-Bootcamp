import random

count = 0

while True:
    num = random.randint(1, 10)
    count += 1
    print("Generated:", num)

    if num > 7:
        break

print("Total numbers generated:", count)