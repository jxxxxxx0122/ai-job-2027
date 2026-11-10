# 2026-11-10
# Day1 函数基础：统计元音个数
def count_vowels(s):
    count = 0
    for char in s:
        if char in 'aeiouAEIOU':
            count += 1
    return count

if __name__ == '__main__':
    print(count_vowels('hello WoRLD'))