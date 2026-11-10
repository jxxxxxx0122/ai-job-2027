# 2026-11-10
# Day1 高阶函数：apply
def apply(func, value):
    return func(value)

if __name__ == '__main__':
    print(apply(lambda x: x*x,5))
    print(apply(len,"hello"))