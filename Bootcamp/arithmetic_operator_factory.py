def make_operator(op):
    operators = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y if y != 0 else "Error: Division by zero"
    }
    return operators.get(op, lambda x, y: "Invalid Operator")

add = make_operator("+")
subtract = make_operator("-")
multiply = make_operator("*")
divide = make_operator("/")

num1, num2 = 10, 5
print(f"Addition ({num1} + {num2}):", add(num1, num2))
print(f"Subtraction ({num1} - {num2}):", subtract(num1, num2))
print(f"Multiplication ({num1} * {num2}):", multiply(num1, num2))
print(f"Division ({num1} / {num2}):", divide(num1, num2))