# 2026-11-10
# Day1 返回多个值
def manual_divmod(a, b):
    if b == 0:
        return (None, None)
    return (a//b, a % b)

if __name__ == "__main__":
    print(manual_divmod(7, 2))
    print(manual_divmod(7, 0))
    q, r = manual_divmod(7, 2)
    print(q, r)