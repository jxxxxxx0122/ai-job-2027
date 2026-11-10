# 2026-11-10
# Day1 lambda + sorted 按分数降序
student = [('张三',85),('李四',92),('王五',78)]

result = sorted(student,key=lambda x:x[1],reverse=True)
print(result)