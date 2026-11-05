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

avg = total / count
print(f"平均 {avg}，最高 {top_name} {top_score}")