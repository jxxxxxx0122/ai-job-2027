# 2026-11-05 Day 2 练习
# 列表去重并保持原顺序。不许直接 list(set(...))（会乱序）
data = [3,1,3,2,1,4]
result = []
seen = set()

for x in data:
    if x not in seen:
        seen.add(x)
        result.append(x)

print(result)