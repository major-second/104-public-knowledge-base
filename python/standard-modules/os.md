`import os`，和操作系统相关
- 如[[6-env]]，可以用`os.environ["KEY"] = value`修改
  - 等价于运行python脚本前先（shell脚本运行）`export KEY=value`
  - 应用：[[torch-cuda]]中指定可见哪些显卡
- 如[[minimum]]中`os.getpid()`和`os.getppid()`查看进程号、父进程号