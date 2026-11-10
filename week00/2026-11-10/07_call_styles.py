# 2026-11-10
# Day1 三种调用方式
def describe(name, age, city="未知"):
    print(f"{name} {age}岁, 来自{city}")

if __name__ == '__main__':
    describe("张三",20, "西安")
    describe(name="张三", age=20, city="西安")
    describe("张三", age=20, city="西安")