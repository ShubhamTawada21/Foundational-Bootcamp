def recursive_example(n):
    if n <= 0:
        return
    print(n)
    recursive_example(n - 1)

if __name__ == "__main__":
    recursive_example(7)
