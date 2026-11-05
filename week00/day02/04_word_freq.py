# 统计一个句子中每个单词出现的次数，结果放字典
sentence = input("请输入句子: ")

freq = {}

for char in sentence.lower().split():
    freq[char] = freq.get(char, 0) + 1

print(freq)