# 2026-11-10
# Day1 **kwargs：逐行打印键值
def build_profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

if __name__ == '__main__':
    build_profile(name="张三", age=20)
    print("---")
    build_profile(city="北京", job="学生", level="本科")