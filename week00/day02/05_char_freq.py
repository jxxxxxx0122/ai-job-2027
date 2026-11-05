# 2026-11-05 Day 2 练习
# 统计字符串每个字符出现的次数，忽略空格，按次数降序输出 (字符, 次数) 列表；次数相同按字母升序
s = input("请输入字符串: ")

freq = {}

for ch in s:
    if ch == " ":
        continue
    freq[ch] = freq.get(ch, 0) + 1

items = list(freq.items())
items.sort(key=lambda kv: (-kv[1],kv[0]))

print(items)