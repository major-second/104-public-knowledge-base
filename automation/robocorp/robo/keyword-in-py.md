- 前置
  - [[keyword]]
  - [[tasks-py]]
- [[robo]]中`robo new`生成最小例子，不太实用，连[[keyword]]都用不了
- 你可能要
  - 参考[这个](https://github.com/robocorp/template-python)
  - 引入[[robocorp-conda-yaml]]文件，[[robot-yaml]]文件
    - 注意原来生成的`toml`和[[robocorp-conda-yaml]]东西不能冲突
    - 例如
      - `pyproject.toml`
        ```toml
        [tool.robo]
        name = "Blank"
        description = "An empty automation project"
        python = "3.9.13"

        [tool.robo.dependencies]
        robocorp-tasks="1.0.0"
        rpaframework="24.0.0"
        ```
      - `conda.yaml`
        ```yaml 
        channels:
          - conda-forge
        dependencies:
          - python=3.9.13                 # https://pyreadiness.org/3.9
          - pip=22.1.2                    # https://pip.pypa.io/en/stable/news
          - pip:
            - rpaframework==24.0.0        # https://rpaframework.org/releasenotes.html
        ```
  - 补些包（参考[[robocorp-conda-yaml]]）
    - 至少`robotframework`包得有吧
- 虽然参考了[[robocorp-conda-yaml]]，但这里还是用`robo run`而不是[[rcc]]
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
- [[vscode-python]]
  - `robo run`运行从而得到`conda`环境
  - 右下角选解释器选该环境
  - 查询api
    - ctrl+鼠标定位到`RPA.Windows`这种
    - 出来的文件中找到`_get_libraries`，ctrl+鼠标定位，进去`WindowKeywords`这种，即可查api
  - [[debug-console]]
    - 可用，且非常方便
    - [[robocorp-windows]]用例：
      ```python
      from RPA.Windows import Windows
      library = Windows()
      print(library.keywords.keys())
      print(library.list_windows())
      ```
    - 注：如果`robocorp`包没有，可以`try`跳过