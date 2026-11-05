# 2026-11-05 Day 2 练习
# 两门课的选课名单用集合表示，输出：都选的、至少选一门的、只选 Python 的、只选了一门的
python = {'张三', '李四', '王五'}
java = {'李四', '王五', '赵六'}

print("都选:", python & java)
print("至少一门:", python | java)
print("只Python:", python - java)
print("只选一门:", python ^ java)