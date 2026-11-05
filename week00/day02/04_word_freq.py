# 2026-11-05 Day 2 练习
# 统计一个句子中每个单词出现的次数，结果放字典
sentence = input("请输入句子: ")

freq = {}

for word in sentence.lower().split():
    freq[word] = freq.get(word, 0) + 1

print(freq)