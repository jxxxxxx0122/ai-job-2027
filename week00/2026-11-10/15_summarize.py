# 2026-11-10
# Day1 综合：summarize + 辅助函数
def compute_total(records):
    total = 0
    for _, score in records:
        total += score
    return total


def find_best(records):
    best_name, best_score = records[0]
    for name, score in records:
        if score > best_score:
            best_name, best_score = name, score
    return best_name

def summarize(records, reverse=False):
    total = compute_total(records)
    avg = total / len(records)
    best = find_best(records)
    sorted_records = sorted(records, key=lambda x: x[1], reverse=reverse)
    return {
        "total": total,
        "avg": avg,
        "best": best,
        "sorted": sorted_records
    }


if __name__ == '__main__':
    records = [("张三", 85), ("李四", 92), ("王五", 78)]
    result = summarize(records)
    print(result["total"])
    print(result["avg"])
    print(result["best"])
    print(result["sorted"])
