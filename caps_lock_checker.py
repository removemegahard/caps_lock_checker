import tkinter as tk
import ctypes
import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw
import threading
import os
import sys

def resource_path(relative_path):
    """获取资源文件的绝对路径，兼容打包后的程序"""
    try:
        # PyInstaller 创建临时文件夹 _MEIPASS 用来存放打包后的资源文件
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class CapsLockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Caps Lock 状态检测")
        self.root.geometry("300x100")
        self.root.configure(bg='#2b2b2b')
        self.root.overrideredirect(True)  # 移除窗口边框
        self.root.attributes('-alpha', 0.9)  # 设置透明度

        # 设置窗口图标，使用 resource_path 获取图标的绝对路径
        self.root.iconbitmap(resource_path('assets/icon.ico'))

        # 创建并配置显示 Caps Lock 状态的标签
        self.label = tk.Label(root, text="", font=("Helvetica", 16), bg='#2b2b2b', fg='white')
        self.label.pack(pady=20)

        # 初始化 Caps Lock 状态
        self.last_state = self.get_caps_lock_state()
        self.update_caps_lock_status()

        # 显示窗口然后隐藏
        self.show_and_hide()

        # 创建系统托盘图标线程
        self.tray_thread = threading.Thread(target=self.create_tray_icon)
        self.tray_thread.daemon = True  # 使用 daemon 属性来设置守护线程
        self.tray_thread.start()

        # 开始检查 Caps Lock 状态的定时器
        self.check_caps_lock_status()

    def get_caps_lock_state(self):
        """检测 Caps Lock 状态"""
        return ctypes.WinDLL("User32.dll").GetKeyState(0x14) & 0x0001

    def update_caps_lock_status(self):
        """更新 Caps Lock 状态的显示"""
        if self.get_caps_lock_state():
            self.label.config(text="Caps Lock is ON", fg="green")
        else:
            self.label.config(text="Caps Lock is OFF", fg="red")

    def show_and_hide(self, delay=500):
        """显示窗口并在延迟后隐藏"""
        self.root.deiconify()  # 显示窗口
        self.root.after(delay, self.hide_window)

    def hide_window(self):
        """隐藏窗口"""
        self.root.withdraw()

    def check_caps_lock_status(self):
        """定期检查 Caps Lock 状态，如果状态发生变化，则显示窗口并更新状态"""
        current_state = self.get_caps_lock_state()
        if current_state != self.last_state:  # 如果状态变化
            self.last_state = current_state
            self.update_caps_lock_status()
            self.show_and_hide()  # 状态变化时显示窗口几秒钟

        # 每500毫秒检查一次 Caps Lock 状态
        self.root.after(500, self.check_caps_lock_status)

    def create_tray_icon(self):
        """创建系统托盘图标"""
        # 使用 resource_path 获取图标路径
        icon_image = Image.open(resource_path("assets/icon.ico"))

        # 创建托盘图标菜单
        menu = (item('显示', self.show_window), item('退出', self.quit_app))
        tray_icon = pystray.Icon("CapsLockChecker", icon_image, "Caps Lock Checker", menu)
        tray_icon.run()

    def show_window(self, icon=None, item=None):
        """显示主窗口"""
        self.root.deiconify()
        self.root.attributes('-topmost', True)  # 确保窗口显示在最前
        self.root.after(0, lambda: self.root.attributes('-topmost', False))  # 取消最前设置

    def quit_app(self, icon, item):
        """退出应用程序"""
        icon.stop()
        self.root.quit()


# 创建主窗口
root = tk.Tk()

# 创建应用实例
app = CapsLockApp(root)

# 运行主循环
root.mainloop()
