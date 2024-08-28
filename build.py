import subprocess
import os,sys

# 确保在正确的目录下运行
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)
#确定分隔符
if sys.platform == "win32":
    data_separator = ";" 
else:
    data_separator = ":"

# PyInstaller 打包命令
command = [
    'pyinstaller',
    '--onefile',          # 打包成一个独立的可执行文件
    '--windowed',         # 不显示控制台窗口
    f'--add-data=assets/icon.ico{data_separator}assets',  # 添加图标资源文件
    '--icon=assets/icon.ico',  # 指定应用图标（可选）
    'caps_lock_checker.py'     # 主脚本
]

# 运行打包命令
try:
    subprocess.run(command, check=True)
    print("打包成功！可执行文件位于 dist/ 目录下。")
except subprocess.CalledProcessError as e:
    print("打包失败：", e)
