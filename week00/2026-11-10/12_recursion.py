# 2026-11-10
# Day1 递归：factorial / fib 递归版 + 循环版
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_loop(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    print(factorial(5))
    print(fib_recursive(10))
    print(fib_loop(10))
