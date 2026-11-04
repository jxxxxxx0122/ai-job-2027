# 2026-11-04 Day 1 练习
# 8.阶乘
n = int(input("请输入一个整数: "))
result = 1
i = 1

while i <= n:
    result *= i
    i += 1

print(f"{n}! = {result}")