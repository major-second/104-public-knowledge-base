类比[[docker/env-var]]，[[6-env]]等
# 临时设置
- [[powershell-var]]
- 比如程序中途的`$env:path = `
# 持久设置
- 需求例子
    - [[robocorp]]中的`rcc.exe`
    - [[wsa]]中的`adb.exe`
    - [[vscode]]
    - [[cursor-ide]]
- [[settings-and-configurations]]
  - [[GUI]]
    - 原生：开始菜单搜索`env`，找到`Edit*env*`选项，然后用GUI可以方便地设置环境变量
    - [[powertoys]]包装了一层
    - 软件安装过程中：[[conda-installation]]可以选择安装过程中手动加
  - [[cli]]
    - `setx /?` [[help]]
    - `setx PATH "$env:path;/test"` default: by user
    - `setx PATH "$env:path;/test" /M` machine-wide
    - [[non-standard]]: [[cursor-ide]]的[[terminal]]需要彻底关掉cursor再打开作为[[refresh]]才有用（reload都不行）
# path
- `path`变量新增路径，使得程序可以在[[powershell]]中直接使用，不需敲绝对路径
- 注意[[ps-general-var]]提到的必须用`$home`不能用`~`
## 安装时自动设置path
- 有些程序安装时有选项可以自动加入安装路径或相关路径到`env:path`，从而之后可以方便使用
  - [windows的python](https://www.python.org/downloads/windows/)
    - 安装时可以选择加入，这样之后在[[powershell]]中可以使用`python`命令
    - 一个坑：新加入的`path`必须排序足够前，否则出现[这个问题](https://cloud.tencent.com/developer/article/1652685)，仍然无法使用
  - [[conda-installation]]可以自动加