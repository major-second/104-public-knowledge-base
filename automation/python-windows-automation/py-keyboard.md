- `pip install keyboard`
- 参考
  - [[keyboard]]
  - [[keyboard-shortcuts]]
  - [[use-keyboard-shortcuts-for-editing]]
  - [[vscode-keyboard-shortcuts]]
- 例子
  - ```python
    import keyboard
    keyboard.press_and_release('ctrl + `')
    keyboard.write('python -c \'print("1")\'')
    keyboard.press_and_release('enter')
    ```
  - `keyboard.write(content, delay)`
    - 坑：编辑器例如[[vscode]]导致按键和实际输入差别
      - 回车可能不换行而是确认自动补全
      - 自动缩进导致错乱
    - 所以可以考虑[[meta-programming]]，先把回车和tab换成别的token再换回来