# 2026-11-04 Day 1 练习
# 7.判断最大
a = int(input("请输入数字1: "))
b = int(input("请输入数字2: "))
c = int(input("请输入数字3: "))

maxnum = a
if b > maxnum:
    maxnum = b
if c > maxnum:
    maxnum = c

print(maxnum)