- 前置
  - [[start-join]]
- 对于不想等的进程，可以
  - ```python
    p2.join()
    if p1.is_alive():
        p1.terminate()
    ```
  - 相当于用`p2`停止信号“代理”`p1`

- 应用：[[ctypes]]中
  ```python
  def open_message_box(message):
      ctypes.windll.user32.MessageBoxW(0, message, "Reminder", 1)

  def close_message_box():
      sleep(2)
      ctypes.windll.user32.PostMessageW(0, 0x0010, 0, 0)

  def pop_message(message):
      p1 = Process(target=open_message_box, args=(message,))
      p2 = Process(target=close_message_box)

      p1.start()
      p2.start()

      p2.join()
      if p1.is_alive():
          p1.terminate()
  ```