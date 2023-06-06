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