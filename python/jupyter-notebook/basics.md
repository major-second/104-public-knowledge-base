# 前置
- [[pip]]
- `pip install ipykernel`补包
  - 注：当然也可以在`conda`环境中`pip install ipykernel`做
# 好处
- 结合了`python`和`markdown`的好处（可以使用多种代码`block`）
  - `markdown` block可以有数学公式、图片等作为“高级[[comment]]”
  - `python` block可以运行`python`代码
- 把`python`代码按照`cell`为单位排列
  - 可以方便模块化
  - 还有一种常见操作：新建一个（临时）`python block`，`print`你想要的东西
    - 该操作类似于一般的调试中的[[debug-console]]，非常方便
- 可远程调试，媲美[[remote-ssh]]
# feature
- 即使代码块都没改变，但运行结果不同了，git也会认为你编辑了`.ipynb`文件
- 运行block时，有一些自动生成的[[command-line-arguments/basics]]命令行参数
- 改变（block中定义的）函数定义要重新运行block才生效
- 关于`Restart`（原始方法运行的快捷键：两次`0`）
  - 会丢失全部变量（但有时这就是我们想要的，因为可能之前变量会一直放着形成干扰，或占用内存、显存）
  - 改变`import`了`.py`文件中东西的定义，则要`Restart`才生效（区别于改变block中定义东西）
- 服务器卡和本地流畅不矛盾。有可能你远程连`jupyter`服务器，服务器卡死了（[[vnc]]或者[[teamviewer]]看桌面，发现没反应），本地编辑却很流畅，但运行不了
- 编辑技巧
  - `Ctrl`按住可以光标选中多个地方，类似于[[vscode/edit]]的`Alt`
  - 更多和[[vscode/edit]]相同的技巧：`Ctrl + 方向键`，选中一串东西按一次`[`加括号等
  - `Tab`补全（如果有多个备选，则`Tab`出下拉菜单，回车选择）
# 原始方法运行
- [参考](https://docs.jupyter.org/en/latest/running.html)
- 命令行`jupyter-notebook <名字>.ipynb`可以在浏览器中打开相应页面
- 注：如果你正在远程，即使用`ssh`中的终端（例如[[remote-ssh]]），则可以看到它会提示`http://localhost:8888/?token=<一串字符>`这种字样
  - 我们只需[[forward-port]]这个端口，然后即可在本地浏览器中粘贴`http://localhost:8888/?token=<一串字符>`进行浏览页面和使用jupyter notebook
- 注：也可以直接`--ip <ip地址> --no-browser`，出现`http://<ip>:<port>/?token=<一串字符>`这种字样，复制到本地的浏览器即可本地调试远程代码
  - 前提是本地要能访问`<ip地址>`，涉及内网时，参考[[vpn]]等
  - 这种方法节省了[[forward-port]]步骤
- `jupyter`运行时终端有`Ctrl+C`自动保护
  - 这为了防止你误以为是复制，结果按下`Ctrl+C`停下server，在停止前强行让你确认！
  - 当然你熟悉了这个feature后，还有其它用途，比如按`Ctrl+C`再按`n`恢复，此时可展现`http://<ip>:<port>/?token=<一串字符>`
- 调试
  - 有[[hotkeys]]
  - 正在运行时左侧有`[*]`记号
  - 运行完左侧数字表示运行顺序
  - 上面有一些常见按钮（如保存、停止、重启等）
  - 不能[[breakpoint]]，所以要参考[[general-principles/debug]]的技巧
# 其它运行方式
- 使用vscode [[jupyter-notebook]]插件调试编辑
  - 相比原始方法，可以打[[breakpoint]]
  - 但多进程（[[multiprocessing/minimum/minimum]]）时无法打
- `jupyter nbconvert --to python <名字>.ipynb`可以把`.ipynb`转化成`.py`文件，之后`python`命令运行即可
  - 但涉及到[[jupyter-notebook/tqdm]]等时可能有麻烦