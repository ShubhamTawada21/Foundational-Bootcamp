from functools import reduce

numbers = list(range(1, 21))

result = reduce(
    lambda x, y: x + y, 
    map(lambda x: x**2, filter(lambda x: x % 2 != 0, numbers))
)

print(f"The sum of the squares of odd numbers from 1 to 20 is: {result}")