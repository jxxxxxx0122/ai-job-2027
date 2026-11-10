# 2026-11-10
# Day1 拆函数：九九乘法表
def print_table(n):
    for i in range(1, n+1):
        row = []
        for j in range(1, 1+i):
            row.append(f"{j}x{i}={i * j}")
        print("\t".join(row))

if __name__ == '__main__':
    print_table(9)