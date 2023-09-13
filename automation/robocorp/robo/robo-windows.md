- 前置
  - [[keyword-in-py]]
  - [[debug-console]]
- 运行并前置
  ```python
  from RPA.Windows import Windows
  lib_windows = Windows()
  lib_windows.windows_search('calculator')
  calc = lib_windows.control_window('regex:.*Calc.*')
  ```
- [[debug-console]]看`tree`
  - `t = lib_windows.print_tree(calc, return_structure=True)`
- 定位元素
    ```python
    try:
        lib_windows.get_element('name:Connect', root_element=cisco, timeout=0.2) # if you used contrl_window before, `root_element` would be optional
    except:
        print("Connect button in Cisco window doesn't exist!")
    ```