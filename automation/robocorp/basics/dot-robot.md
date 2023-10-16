- 前置
  - [[robocorp-conda-yaml]]
  - [[pip]]
  - 会用浏览器或vscode插件查看[[html]]
- 在[[robot-yaml]]提到`tasks - <任务名称> - <command | shell | robotTaskName>`，共三种可能
  - 我们已经知道`shell`就是在shell输入命令
    - 比如`python -c "<python语句>"`，`python -V`等
  - `command`除了能更好处理空格等，其实和`shell`本质差不多
  - 那么`robotTaskName`怎么使用呢？
- 简单翻翻[beginners course](https://robocorp.com/docs/courses/beginners-course)，[cheat sheet](https://robocorp.com/docs/languages-and-frameworks/robot-framework/cheat-sheet)，大概了解什么是`.robot`
  - 最简单的只需要
    ```robotframework
    *** Tasks ***
    Minimal task
        Log    Done.
    ```
  - [参考例子](../example/dot-robot/tasks.robot)
- 这是`robotframework`语言
  - 基础语法
    - 命令和参数
      - 用$\ge 2$个空格分隔“命令”(keyword) 和“参数”
        - 原因
          - “命令”本身可能含有空格，比如`Wait For Element`
          - “参数”可能也有空格
      - “命令”在vscode中可以补全
    - 在mandatory参数后可能有optional参数，也用$\ge 2$个空格隔开
      - 可能
        - 形如`timeout=3`，即`key=value`
        - 按位置填入，而不是`key=value`形式
      - 类似于python可选参数、关键字参数
    - `*** Settings ***`模块中，`Library`语句导入Keywords
      - 这个相当于python导入[[python-import]]时的`from ... import *`所以很容易重名
        - 此时需要写出全名，比如`RPA.Desktop.Click`
    - 直接看[cheat sheet](https://robocorp.com/docs/languages-and-frameworks/robot-framework/cheat-sheet)，基本现用现查即可
  - 除了基础语法，当然还需要[[keyword]]
- 修改其它文件
    1. 在[[robot-yaml]]中提到的`robot.yaml`中`robotTaskName`字段
      - 写`.robot`文件中的`Tasks`字段下的task名称
        - 比如刚刚的`Minimal task`
    2. 同时需要在[[robocorp-conda-yaml]]中适当加入内容（补包）
      - 可能有`pip`有包`conda`没有的现象参考[[pip]]
        - 例如2022.6，`conda`的`rpaframework`只有`9.x`而`pip`有`14.x`
- 这样运行之后结果
  - 在`output`文件夹就除了之前的`stdout.log, stderr.log, *.yaml`，还有`*.xml, *.html`
    - 其中`html`可以[[chrome]]或[[vscode-browser-extensions]]打开