- 前置
  - [[keyword]]
  - [[tasks-py]]
- [[robo]]中`robo new`生成最小例子，不太实用，连[[keyword]]都用不了
- 你可能要结合[[conda-yaml]]，参考[这个](https://github.com/robocorp/template-python)
  - 建立基本结构，比如引入[[conda-yaml]]文件，[[robot-yaml]]文件
  - 补些包（[[conda-yaml]]）
    - 至少`robotframework`包得有吧
    - 注意`toml`和[[conda-yaml]]东西不能冲突
- 虽然参考了[[conda-yaml]]，但这里还是用`robo run`而不是[[rcc]]
- 此时在[[tasks-py]]中即可导入和使用包
  - 一个例子： https://robocorp.com/docs/libraries/rpa-framework/rpa-windows
  - 导入
    ```python
    from RPA.Windows import Windows
    library = Windows()
    ```
  - 使用例子
    - `library.windows_run("calc.exe")`
    - `library.windows_search("outlook")`
# [[vscode]]
- [[vscode-python]]查询api
  - `robo run`运行从而得到`conda`环境
  - 右下角选解释器选该环境
  - ctrl+鼠标定位到`RPA.Windows`这种
  - 出来的文件中找到`_get_libraries`，ctrl+鼠标定位，进去`WindowKeywords`这种，即可查api
- [[debug-console]]等可用。比如
    ```python
    from RPA.Windows import Windows
    library = Windows()
    print(library.keywords.keys())
    print(library.list_windows())
    ```