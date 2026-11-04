# 2026-11-04 Day 1
# 环境自检：确认 Python + Git 可用，能跑通第一个脚本
import sys
import platform

# Windows 控制台默认用 GBK，中文会乱码；强制 stdout 用 UTF-8
sys.stdout.reconfigure(encoding="utf-8")

print("hello, ai-job-2027")
print(f"Python {platform.python_version()} on {platform.system()}")
print(f"解释器路径: {sys.executable}")
