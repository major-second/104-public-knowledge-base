- `pip install keyboard`
- 参考
  - [[keyboard]]
  - [[keyboard-shortcuts]]
  - [[use-keyboard-shortcuts-for-editing]]
  - [[vscode-keyboard-shortcuts]]
  - 可能和[[robocorp-desktop]]功能相同
  - [文档](https://github.com/boppreh/keyboard#api)
- 例子
  - ```python
    import keyboard
    keyboard.send('ctrl + `')
    keyboard.write('python -c \'print("1")\'')
    keyboard.send('enter')
    ```
  - `keyboard.write(content, delay)`
    - 坑：编辑器例如[[vscode]]导致按键和实际输入差别
      - 回车
        - 回车可能不换行而是确认自动补全
        - 自动缩进导致错乱
      - 自动配对字符（如括号）
      - 所以可以考虑[[meta-programming]]，先把麻烦字符换成别的token再换回来