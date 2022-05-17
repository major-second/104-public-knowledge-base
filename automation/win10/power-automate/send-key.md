前置：
- 参考[[built-in-keyboard-shortcuts-editting]]，[[built-in-keyboard-shortcuts-windows]]，[[built-in-keyboard-shortcuts-fn]]等快捷键
- 了解[[keyboard-shortcuts]]等

## 用途
- 键盘相比鼠标很多时候都更容易[[generalization]]
- 输入终端命令
- 快捷键操作（如vscode [[keyboard-shortcuts]]）
- 有些切换终端环境导致无法写到一个脚本的，可以用send keys模拟
  - 切换[[zsh]]
  - 切换[[tmux]]
## 语法
- `{Control}{Shift}({P})`
  - 注意花括号，`Control`不是`Ctrl`，字母也要加花括号
- `{Control}{Oemtilde}`（即：有些特殊键有特殊名称）
- [参考](https://docs.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/mouseandkeyboard#sendkeys)
> To use a key as a modifier, use the curly brackets notation for both keys: e.g. for Ctrl + A, use {Control}({A})

- 当然平时数字模拟输入命令倒是不需要花括号