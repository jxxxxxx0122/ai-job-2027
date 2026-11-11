# 2026-11-10
# Day1 拆函数：parse_ints / stats / main
import sys


def parse_ints(line):
    return [int(x) for x in line.split()]

def stats(nums):
    total = 0
    maximum = nums[0]
    minimum = nums[0]
    for n in nums:
        total += n
        if n > maximum:
            maximum = n
        if n < minimum:
            minimum = n
    return total, maximum, minimum

def main():
    line = input("请输入空格分隔的整数: ")
    nums = parse_ints(line)

    if not nums:
        print("没有输入数字")
        return

    total, maximum, minimum = stats(nums)
    print(f"列表：{nums}")
    print(f"长度：{len(nums)}")
    print(f"和：{total}")
    print(f"最大值：{maximum}")
    print(f"最小值：{minimum}")

if __name__ == '__main__':
    main()