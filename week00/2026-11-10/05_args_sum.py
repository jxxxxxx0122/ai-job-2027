# 2026-11-10
# Day1 *args：求和，可跳过负数
def total(*nums, ignore_negative=False):
    result = 0
    for num in nums:
        if ignore_negative and num < 0:
            continue
        result += num
    return result

if __name__ == "__main__":
    print(total(1, 2, 3))
    print(total(1, -2, 3))
    print(total(1, -2, 3, ignore_negative=True))