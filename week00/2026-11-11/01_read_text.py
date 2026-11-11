# 2026-11-11
# Day2 文件读写：read_file
def read_file(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"文件不存在 {path}")
        return None

if __name__ == "__main__":
    content = read_file("D:/code/ai-job-2027/week00/2026-11-11/fixtures/config.json")
    print(content)
    print(content is not None)

    content2 = read_file("D:/code/ai-job-2027/week00/2026-11-11/fixtures/nope.txt")
    print(content2)