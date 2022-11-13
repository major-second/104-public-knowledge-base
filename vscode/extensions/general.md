# 一般流程
- 安装
  - gui：`Ctrl + Shift + X`搜索插件并点击Install安装
  - 命令行：参考[[vscode/command-line]]
- 点击左侧INSTALLED栏目中插件条目
  - ![](extension-item.png)
- 打开其主页
  - 看其中教程学习使用方法
- 做出适当配置
  - 比如[[vscode/settings]]，[[settings-and-configurations]]等提到的方法
- 使用插件
  - 可能是vscode界面（左侧）出现按钮例如[[robocorp/basics/installation]]，[[remote-ssh]]
  - 可能是`Ctrl + Shift + P`的command palette中出现新命令，如[[git-project-manager]]
    - 这时可以结合[[vscode/keyboard-shortcuts]]设置快捷键
  - 可能是右键菜单出现选项，如[[git-history]]
- 管理插件：`Ctrl+Shift+X`出来的界面，可以卸载或禁用等
- 注：有时若干个插件是打成包的，比如`python`，其中包含了[[jupyter-notebook]]
  - 卸载也是一起卸载
# vscode插件和其它软件的关系
- 有时，本身完成实际功能的软件并不是vscode，也不集成在vscode插件中。vscode插件只是调用接口
  - 这里参考系统的“内核”和“外壳”[[shell]]思想
  - e.g. [[paste-images-from-clipboard]] needs `sudo apt install xclip` in Ubuntu.
  - e.g. [[conda/installation]]安装后（或者直接下载安装`python`），vscode的python相关插件才有用
    - **插件本身当然不能集成python解释器**！（你想想插件一共才多大呢）
  - e.g. [[git/init/installation]]安装后，`Ctrl+Shift+G`功能和[[git-history]]插件才能用，也是类似的
  - latex，cpp等也都是这样
  - 特殊情况：对于linux系统，shell的“解释器”（“内核”）当然内置在系统中了，所以[[bash-debug]]拿到就能用
- 有时，[[markdown-preview-enhanced]]这种特别轻量级的东西可以“集成到vscode插件中”，即插即用
# troubleshooting
- [[remote-ssh]]时，远程[[extensions/general]]版本高，本地vscode版本低，可能导致插件用不了，需要更新本地vscode