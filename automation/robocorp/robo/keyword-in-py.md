- 前置
  - [[keyword]]
  - [[tasks-py]]
  - [[robocorp-conda-yaml]]（也就是[[create-env-from-yaml]]）
  - [[toml]]
- [[robo]]中`robo new`生成最小例子，不太实用，连[[keyword]]都用不了
- 可能解决方法
  - 参考[这个](https://github.com/robocorp/template-python)
  - 引入
    - [[robocorp-conda-yaml]]文件
      - 这个[[robocorp-conda-yaml]]当然同时作为[[create-env-from-yaml]]自己调试用
    - [[robot-yaml]]文件
  - 同时修改原来[[robo]]生成的[[toml]]
    - 注意和[[robocorp-conda-yaml]]应当一致
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
  - 以上各个文件中，都补些必要包
    - 参考[[robocorp-conda-yaml]]
    - 至少`robotframework`包得有吧
    - 再补其它的包，也往往需要在两边都对应加
      - [[create-python-package-for-pip]]
        - 目前没找到，这可能是[[robo]]缺陷
- 虽然这里参考了[[robocorp-conda-yaml]]，但这里还是用`robo run`而不是[[rcc]]
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
# [[vscode-python]]
  - `robo run`运行从而得到`conda`环境
  - 右下角选解释器选该环境
  - 查询[[api]]
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