- vscode集成了终端（可能是windows的[[powershell/basics]]或者linux的shell），参考[[keyboard-shortcuts]]<code>Ctrl+&#96;</code>快捷打开
- 可以`+`增加window或两个框（split）按钮增加pane，这点像[[tmux]]，只不过它不能退出后还运行
- 和普通桌面终端区别
  - 可能会缺少权限。所以一个命令如果在这里跑不通，就去桌面的终端试试，参考[[7-permissions]]
  - 可能没法显示东西
- `Ctrl+左键点击`终端显示的路径字符串，可以在编辑器中打开
  - 因此可以结合`$(pwd)`等东西便捷地使用，到处打开编辑东西
- <code>Ctrl+Shift+&#96;</code>新终端，`Ctrl+Shift+5`split
  - 5这个是不是想到[[tmux]]的`Ctrl+B Shift+5`