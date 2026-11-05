# 2026-11-05 Day 2 练习
# 学生成绩是元组列表，遍历解包，求平均分并找出最高分学生
students = [('张三', 85), ('李四', 92), ('王五', 78)]

total = 0
count = 0
top_name, top_score = None, None

for name, score in students:
    total += score
    count += 1
    if top_score is None or score > top_score:
        top_name, top_score = name, score

if count == 0:
    print("没有学生数据")
else:
    avg = total / count
    print(f"平均 {avg}，最高 {top_name} {top_score}")