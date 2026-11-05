# 2026-11-05 Day 2 练习
# 字典反转（值变键）。先假设值唯一；再做进阶版：值重复时收成列表
# 基础版
d = {'a':1, 'b':2}
inv = {v: k for k, v in d.items()}
print(inv)

# 进阶版
d2 = {'a':1, 'b':1, 'c':2}
inv2 = {}
for k, v in d2.items():
    if v in inv2:
        inv2[v].append(k)
    else:
        inv2[v] = [k]
print(inv2)