# 2026-11-04 Day 1 练习
# 4.闰年平年判断
year = int(input("请输入年份: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year}年是闰年")
else:
    print(f"{year}年是平年")