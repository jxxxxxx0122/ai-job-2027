# 2026-11-10
# 可变默认参数的坑

# ----------- 默认参数只在函数定义时求值一次，列表是可变对象，所以三次调用共用同一个列表

# ---- 坑版
def add_item_bad(item, lst=[]):
    lst.append(item)
    return lst

# ---- 正确版
def add_item_good(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

if __name__ == '__main__':
    print(add_item_bad("a"))
    print(add_item_bad("b"))
    print(add_item_bad("c"))

    print(add_item_good("a"))
    print(add_item_good("b"))
    print(add_item_good("c"))