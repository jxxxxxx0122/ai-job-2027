# 2026-11-10
# Day1 默认参数：make_tag
def make_tag(text, tag="p"):
    return f"<{tag}>{text}</{tag}>"

if __name__ == '__main__':
    print(make_tag("hi"))
    print(make_tag("hi", "h1"))
    print(make_tag("hi", tag="h2"))