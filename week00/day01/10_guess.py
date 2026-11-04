# 2026-11-04 Day 1 练习
# 10.猜数字
target = 42
tries = 0
max_tries = 5

while tries < max_tries:
    guess = int(input(f"第{tries+1}次猜, 请输入一个数字: "))
    tries += 1

    if guess == target:
        print(f"恭喜你, 猜对了！用了{tries}次")
        break
    elif guess > target:
        print(f"大了, 还有{max_tries-tries}次")
    else:
        print(f"小了, 还有{max_tries-tries}次")
else:
    print(f"游戏结束, 答案是{target}")