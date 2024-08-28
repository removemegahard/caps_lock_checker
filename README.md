# Caps Lock Checker

## 简介

Caps Lock Checker 是一个简单的桌面应用程序，用于实时检测和显示 Caps Lock 键的开启状态。它使用 Python 的 Tkinter 库创建一个图形用户界面 (GUI)，并结合 Windows API 来获取 Caps Lock 的当前状态。

## 功能

- 实时检测并显示 Caps Lock 的状态。
- 在用户按下 Caps Lock 键时立即更新显示。
- 绿色指示 Caps Lock 已开启，红色指示 Caps Lock 已关闭。

## 安装

### 系统要求

- **操作系统**: Windows
- **Python**: 3.7 及以上

### 克隆仓库

首先，克隆此项目到本地机器：

```bash
git clone https://github.com/yourusername/caps_lock_checker.git
cd caps_lock_checker
```

### 安装依赖

使用以下命令安装项目所需的依赖项：

<pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><div class="flex items-center"><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" class="icon-sm"><path fill="currentColor" fill-rule="evenodd" d="M7 5a3 3 0 0 1 3-3h9a3 3 0 0 1 3 3v9a3 3 0 0 1-3 3h-2v2a3 3 0 0 1-3 3H5a3 3 0 0 1-3-3v-9a3 3 0 0 1 3-3h2zm2 2h5a3 3 0 0 1 3 3v5h2a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1h-9a1 1 0 0 0-1 1zM5 9a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h9a1 1 0 0 0 1-1v-9a1 1 0 0 0-1-1z" clip-rule="evenodd"></path></svg>复制代码</button></span></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">pip install -r requirements.txt
</code></div></div></pre>

### 运行程序

安装完成后，可以通过以下命令运行程序：

<pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><div class="flex items-center"><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" class="icon-sm"><path fill="currentColor" fill-rule="evenodd" d="M7 5a3 3 0 0 1 3-3h9a3 3 0 0 1 3 3v9a3 3 0 0 1-3 3h-2v2a3 3 0 0 1-3 3H5a3 3 0 0 1-3-3v-9a3 3 0 0 1 3-3h2zm2 2h5a3 3 0 0 1 3 3v5h2a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1h-9a1 1 0 0 0-1 1zM5 9a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h9a1 1 0 0 0 1-1v-9a1 1 0 0 0-1-1z" clip-rule="evenodd"></path></svg>复制代码</button></span></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">python caps_lock_checker.py
</code></div></div></pre>

程序启动后，会显示一个窗口，实时显示 Caps Lock 的状态。

### 打包程序

下载源代码后，在目录下运行下列命令，可直接打包文件

```python
python build.py
```

## 使用说明

1. 启动 Caps Lock Checker 程序。
2. 程序窗口将实时显示当前 Caps Lock 的状态。
3. 按下 Caps Lock 键时，状态会立即更新。

## 文件结构

<pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>plaintext</span><div class="flex items-center"><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" class="icon-sm"><path fill="currentColor" fill-rule="evenodd" d="M7 5a3 3 0 0 1 3-3h9a3 3 0 0 1 3 3v9a3 3 0 0 1-3 3h-2v2a3 3 0 0 1-3 3H5a3 3 0 0 1-3-3v-9a3 3 0 0 1 3-3h2zm2 2h5a3 3 0 0 1 3 3v5h2a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1h-9a1 1 0 0 0-1 1zM5 9a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h9a1 1 0 0 0 1-1v-9a1 1 0 0 0-1-1z" clip-rule="evenodd"></path></svg>复制代码</button></span></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-plaintext">caps_lock_checker/
│
├── caps_lock_checker.py       # 主应用程序代码
├── README.md                  # 项目说明文档
├── requirements.txt           # 依赖项列表
├── assets/                    # 存放图片、图标等资源文件
│   └── screenshot.png         # 应用程序截图
│   └── icon.png               # 应用程序图标（示例）
├── config/                    # 配置文件目录（如果有配置需求）
│   └── config.yaml            # 示例配置文件
├── tests/                     # 单元测试目录
│   └── test_caps_lock.py      # 测试用例
└── setup.py                   # 安装脚本
</code></div></div></pre>

## 贡献

我们欢迎社区的贡献！如果你有任何改进建议、功能请求或发现了错误，欢迎提交 Issue 或 Pull Request。

### 提交代码

1. Fork 此仓库。
2. 创建你的功能分支 (`git checkout -b feature/AmazingFeature`)。
3. 提交你的更改 (`git commit -m 'Add some AmazingFeature'`)。
4. 推送到分支 (`git push origin feature/AmazingFeature`)。
5. 打开一个 Pull Request。

## 许可

此项目基于 MIT 许可证。详细信息请参阅 [LICENSE]() 文件。

## 联系方式

如有任何问题或建议，请通过以下方式联系我：

* **Email** : removemegahard[@outlook.com](removemegahard)
* **GitHub** : [removemegahard (github.com)](https://github.com/removemegahard)

---

**鸣谢**

* 感谢 [Tkinter](https://docs.python.org/3/library/tkinter.html) 和 [ctypes](https://docs.python.org/3/library/ctypes.html) 提供的强大功能，使这个项目成为可能。
