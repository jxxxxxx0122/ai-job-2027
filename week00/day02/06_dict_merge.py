# 2026-11-05 Day 2 练习
# 合并两个字典，重复的键把值相加
def parse_dict(s):
    d = {}
    s = s.strip()
    if not s:
        return d
    for pair in s.split(","):
        if not pair.strip():
            continue
        if ":" not in pair:
            print(f"忽略非法项{pair}")
            continue
        key, value = pair.split(":", 1)
        raw = value.strip()
        try:
            num = int(raw)          # 先试整数
        except ValueError:
            try:
                num = float(raw)    # 再试小数
            except ValueError:
                print(f"忽略非数字值: {pair}")
                continue
        d[key.strip()] = num
    return d

d1 = parse_dict(input("第一个字典:"))
d2 = parse_dict(input("第二个字典:"))

merged = dict(d1)
for k,v in d2.items():
    merged[k] = merged.get(k, 0) + v
print("合并结果:",merged)