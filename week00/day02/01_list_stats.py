# 输入一行空格分隔的整数，输出列表、长度、和、最大值、最小值。不许用 sum / max / min，全部手写循环
line = input("请输入数字:")
nums = [int(x) for x in line.split()]

length = 0
total = 0
maxnum = nums[0]
minnum = nums[0]

for num in nums:
    length += 1
    total += num
    if num > maxnum:
        maxnum = num
    if num < minnum:
        minnum = num

print(f"列表{nums}、长度{length}、和{total}、最大值{maxnum}、最小值{minnum}")