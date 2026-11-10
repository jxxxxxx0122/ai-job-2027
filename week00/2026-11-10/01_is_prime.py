# 2026-11-10
# Day1 函数基础：is_prime + 打印1-50质数
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    for i in range(1, 51):
        if is_prime(i):
            print(i,end=" ")
    print()