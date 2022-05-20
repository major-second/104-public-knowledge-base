开始菜单或vscode下方都有powershell
相当于linux的终端。可以执行命令。不过时至2022还没linux的命令行好用（不客气地说，win命令行，就是垃圾）
核心
- `help <命令>`，`gal <命令>`看命令的基本信息
  - 比如`rm`其实是`Remove-Item`，`ls`其实是`Get-ChildItem`
  - 可以看出Powershell的命名格式：大写单词，`-`连接动词和名词
  - `gal`自身是`Get-Alias`，2333
- 很多命令是为了让linux的人好用所以做了alias
  - 你可以`gal`一下`mv cp ls rm cat diff`等