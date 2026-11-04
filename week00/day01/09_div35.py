# 2026-11-04 Day 1 练习
# 9.同时整除
list = []
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        list.append(i)

print(list)