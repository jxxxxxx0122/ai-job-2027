# 2026-11-11
# Day2 文件读写: write_lines
def write_lines(path, lines, append=False):
    mode = "a" if append else "w"
    with open(path, mode, encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")


def read_back(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    path = "D:/code/ai-job-2027/week00/2026-11-11/fixtures/out.txt"

    write_lines(path, ["a", "b"])
    print(read_back(path))            # a\nb\n

    write_lines(path, ["c"], append=True)
    print(read_back(path))            # a\nb\nc\n