- `pip install pygetwindow`
- 典型
  - `window = pygetwindow.getWindowsWithTitle(window_name)[0]`
  - `pygetwindow.Win32Window.activate(window)`
    - 等价于`window.activate()`
    - 可能和[[vscode-python]]不兼容
  - `pygetwindow.Win32Window.maximize(window)`
    - 等价于`window.maximize()`