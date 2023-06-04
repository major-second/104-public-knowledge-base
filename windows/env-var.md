类比[[docker/env-var]]，[[6-env]]等
# 临时设置
- [[powershell-var]]
# 持久设置
- 开始菜单搜索`env`，找到`Edit*env*`选项，然后用GUI可以方便地设置环境变量
  - [[robocorp/basics/installation]]中的`rcc.exe`
  - [[wsa]]中的`adb.exe`
  - [[conda-installation]]可以选择手动加
# path
- `path`变量新增路径，使得程序可以在[[powershell-basics]]中直接使用，不需敲绝对路径
## 安装时自动设置path
- 有些程序安装时有选项可以自动加入安装路径或相关路径到`env:path`，从而之后可以方便使用
  - [windows的python](https://www.python.org/downloads/windows/)
    - 安装时可以选择加入，这样之后在[[powershell-basics]]中可以使用`python`命令
    - 一个坑：新加入的`path`必须排序足够前，否则出现[这个问题](https://cloud.tencent.com/developer/article/1652685)，仍然无法使用
  - [[conda-installation]]可以自动加