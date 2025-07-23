import os
import platform

# 指定 HTML 文件的路径
html_file = "index1.html"

# 获取当前操作系统
current_os = platform.system()

# 根据操作系统使用不同的命令打开 HTML 文件
if current_os == "Windows":
    os.system(f"start {html_file}")
elif current_os == "Darwin":  # macOS
    os.system(f"open {html_file}")
elif current_os == "Linux":
    os.system(f"xdg-open {html_file}")
else:
    print("Unsupported OS")
