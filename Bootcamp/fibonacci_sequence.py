def fibonacci_series(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

if __name__ == "__main__":
    try:
        count = int(input("Enter the number of Fibonacci terms: "))
        if count <= 0:
            print("Please enter a positive integer.")
        else:
            print("Fibonacci series:", *fibonacci_series(count))
    except ValueError:
        print("Invalid input. Please enter an integer.")
