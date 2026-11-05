# 2026-11-05 Day 2 练习
# 给定 nums = list(range(10))，用切片输出五组：整体反转、前 3 个、后 3 个、偶数位、每 3 个取 1 个
nums = list(range(10))

print(f"反转 {nums[::-1]} ; 前3个{nums[:3]} ; 后3个{nums[-3:]} ; 偶数位{nums[::2]} ; 每3取1{nums[::3]}")