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