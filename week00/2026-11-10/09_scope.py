# 2026-11-10
# Day1 作用域：错误版 vs global 正确版
counter = 0

def increase_bad():
    counter += 1

def decrease_good():
    global counter
    counter += 1

if __name__ == '__main__':
    # print(increase_bad())
    # # UnboundLocalError: cannot access local variable 'counter' where it is not associated with a value
    decrease_good()
    print(counter)
    decrease_good()
    print(counter)