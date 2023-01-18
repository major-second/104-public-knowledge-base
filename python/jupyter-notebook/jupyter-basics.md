# 前置
- [[pip]]
  - `pip install ipykernel`补包
  - 注：当然可以在`conda`环境中`pip install ipykernel`
# 好处
- 比较根本的一条：可以把东西读进内存，灵活进行下游处理。这是相比`.py`的根本区别！
  - 不过当然可能长期占用内存，注意[[memory]]占用
  - 节省[[about-submit]]资源，特别是[[i-o]]
- 结合了`python`和`markdown`的好处，提升[[readability]]. 可以使用多种代码`block`
  - `markdown` block
    - 可以有数学公式、图片等作为“高级[[comment]]”
    - `markdown`标题可以作为目录层级管理等
      - 特别是有[[nbextension]]时功能更加强大
  - `python` block可以运行`python`代码
    - 按照`cell`为单位排列，可以方便模块化
      - 不同`cell`间继承变量，不用反复读入！
    - 还有一种常见操作：新建一个（临时）`python block`，`print`你想要的东西
      - 该操作类似于一般的调试中的[[debug-console]]，非常方便
    - 一颗语法糖：最后一个表达式不会被丢弃，而是被`print`出
      - 例如cell中有两行
        - `print(1)`
        - `2`
      - 那么`1`和`2`都会被输出
- 可远程调试，媲美[[remote-ssh]]
  - 服务器和本地[[independent]]
    - 本地突然断电，服务器也没事
  - 当然服务器卡和本地流畅不矛盾
    - 有可能你远程连`jupyter`服务器，服务器卡死了
    - [[teamviewer]]看桌面，发现没反应
    - 本地编辑却很流畅，但运行不了
# feature
- 即使代码块都没改变，但运行结果不同了，git也会认为你编辑了`.ipynb`文件
- 运行block时，有一些自动生成的[[command-line-arguments/basics]]命令行参数
- 网页版中，对于`.py`也可以使用分块调试，快捷键等，非常方便调试`.py`文件
## 关于刷新[[refresh]]
- 改变（block中定义的）函数定义要重新运行相应block才生效
- 关于`Restart`
  - 原始方法[[run-jupyter]]时的快捷键：两次`0`
  - 会丢失全部变量
    - 但有时这就是我们想要的，因为可能之前变量会一直放着形成干扰，或占用内存、显存
  - 改变`import`了`.py`文件中东西的定义，则要`Restart`才生效
    - 这区别于改变block中定义东西，只需重新运行相应block
## 进程
- 主体网页中，左侧笔记本为绿色的，每个对应[[4-more-commands]] `ps -ef | grep ipykernel`能看到的一个进程，对应正在运行的一个笔记本
  - 当然，你如果在笔记本内部又有多进程[[multiprocessing-minimum]]等，就又会fork出子进程的子进程，在[[4-more-commands]]中可以看到
- 这样的进程中，内存里[[general-principles/cache]]有变量值
  - 新cell中可以取出变量值，相当于[[debug-console]]操作
  - 停止运行该进程（`Running` tag处关闭或者`kill`等）自然就会丢失变量，释放内存显存等