- 前置
  - [[keyword-in-py]]
  - [[debug-console]]
  - [[api-ui-images]]，这里windows elements相比[[robocorp-desktop]]常用的`image:`，是更好的
- 运行并前置
  ```python
  from RPA.Windows import Windows
  lib_windows = Windows()
  lib_windows.windows_search('calculator')
  calc = lib_windows.control_window('regex:.*Calc.*')
  ```
- [[debug-console]]看`tree`
  - `t = lib_windows.print_tree(calc, return_structure=True)`
  - 此时能看到`path:...|...`这种，可用来临时调试时`get_elements`
  - `calc`也可以改成`path:...`
- 定位元素
    ```python
    try:
        lib_windows.get_element('name:Connect', root_element=cisco, timeout=0.2) # if you used contrl_window before, `root_element` would be optional
    except:
        print("Connect button in Cisco window doesn't exist!")
    ```
    - 其它：例如`'type:Edit'`筛选文本框
- `lib_windows.screenshot(locator, "desktop.png")`
  - 和[[screenshot]]可替代
- `lib_windows.maximize_window(window)`