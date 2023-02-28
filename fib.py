def fib(n: int) -> int:
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()
    return 1


if __name__ == "__main__":
    fib(10000)
