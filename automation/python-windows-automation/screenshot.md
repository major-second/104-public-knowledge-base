- 前置
    - [[pygetwindow]]
    - [[pyautogui]]

```python
import pygetwindow
import pyautogui
import time

def capture_window_by_name(window_name, save_path):
    window = pygetwindow.getWindowsWithTitle(window_name)[0]
    screenshot = pyautogui.screenshot(region=(window.left, window.top, window.width, window.height))
    screenshot.save(save_path)

window_name = "Task Manager"
save_path = f"./screenshot_{time.time()}.png"
capture_window_by_name(window_name, save_path)
```