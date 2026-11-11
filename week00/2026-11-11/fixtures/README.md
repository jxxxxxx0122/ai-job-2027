# Day 2 样本数据

| 文件 | 用途 | 注意 |
|---|---|---|
| `sample.log` | 12 行日志，3 行 ERROR、1 行 WARN | 正常 UTF-8 文本 |
| `config.json` | 正常 JSON，用于 04 题成功路径 | UTF-8 |
| `broken.json` | **故意写坏的 JSON**，第 3 行 `"version": ,` 缺值 | 不要修！它就是给 04 题练 `JSONDecodeError` 的材料 |
| `gbk_note.txt` | **GBK 编码**的中文文本 | 用 UTF-8 打开必然乱码或报 `UnicodeDecodeError`，这是 06 题的实验材料 |
| `scores.csv` | 3 人两科成绩，用于加练 7 | UTF-8 |

## PyCharm 打开时的现象

- `broken.json` 会标红「语法错误」—— 这是本题的考点，别点自动修复。
- `gbk_note.txt` 显示乱码 —— 因为 PyCharm 默认按 UTF-8 解码 GBK 文件。不要用状态栏的「Convert」把它转成 UTF-8，那会把实验材料改掉；只需要看的话选「Reload」并把编码临时设为 GBK，或者用命令行：

```bash
python -c "print(open('week00/2026-11-11/fixtures/gbk_note.txt', encoding='gbk').read())"
```
