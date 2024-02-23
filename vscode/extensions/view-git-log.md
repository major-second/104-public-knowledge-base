- 前置[[vscode-git]]
# git history
- 查看一个文件或文件夹的历史记录
  - 左边文件栏中右键点击某个文件/文件夹
    - ![](git-history1.png)
  - 点击git: view file history
    - ![](git-history2.png)
  - 文件编辑者和branch一目了然！
- 查看整个库
  - 法一：`Ctrl+Shift+P`搜索`history`
  - 法二：`Ctrl+Shift+G`出来的那个界面（左侧git图标那个界面）每个库标题右边有个“时钟”图标
    - 法二方便选择你要看[[submodule]]中的哪个
# git graph
- 跟[git history](#git-history) 总体类似
- 2023.3时，比它好用bug少
  - 比如[git history](#git-history)有时不reload不更新
  - 比如git graph可以看到没有[[commit]]的本地change等等
# git lens
- 略微臃肿，且可能占用 `ctrl shift g`快捷键，且pro要收费
- 不过功能多