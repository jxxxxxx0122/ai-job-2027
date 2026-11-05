# 按字典的值升序排序，输出 (键, 值) 列表（可用 sorted(..., key=lambda kv: kv[1])，lambda 明天正式讲）
d = {'apples': 3, 'banana': 1, 'cherry': 2}

result = sorted(d.items(), key = lambda kv:kv[1])
print(result)