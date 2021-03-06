前置：
- [[robot-yaml]]
- [[pip]]
- 会用浏览器或vscode插件查看[[html]]

内容
- 在[[robot-yaml]]提到`tasks - <任务名称> - <command | shell | robotTaskName>`，共三种可能
  - 我们已经知道`shell`就是在shell输入命令
    - 比如`python -c "<python语句>"`，`python -V`等
  - `command`除了能更好处理空格等，其实和`shell`本质一样
  - 那么`robotTaskName`怎么使用呢？
- 简单翻翻[beginners course](https://robocorp.com/docs/courses/beginners-course)，[cheat sheet](https://robocorp.com/docs/languages-and-frameworks/robot-framework/cheat-sheet)，大概了解什么是`.robot`
  - 最简单的只需要
```robotframework
*** Tasks ***
Minimal task
    Log    Done.
```
- 这是`robotframework`语言。基础语法：
  - `robotframework`用$\ge 2$个空格分隔“命令”和“参数”
    - “命令”本身可能含有空格，比如`Wait For Element`
    - “命令”在vscode中可以补全
    - “参数”可能也有空格，比如[[press-keys]]中
  - 在mandatory参数后可能有optional参数，也用$\ge 2$个空格隔开
    - 例如`104-public-knowledge-base\automation\robocorp\example\desktop\turn-on-wi-fi\tasks.robot`中的`timeout=3`可选参数
    - 例如`104-public-knowledge-base\automation\robocorp\example\desktop\turn-off-proxy\tasks.robot`中的`Wait for...`按位置填入了`reason`可选参数
      - 即：填入可选参数不一定要写`key=value`形式
  - `*** Settings ***`模块中，`Library`语句导入Keywords
    - 这个相当于python导入[[import/basics]]时的`from ... import *`所以很容易重名
    - 此时需要写出全名，比如`RPA.Desktop.Click`
  - 更多语法直接看[cheat sheet](https://robocorp.com/docs/languages-and-frameworks/robot-framework/cheat-sheet)，基本现用现查即可
    - 例如使用了`TRY`的`104-public-knowledge-base\automation\robocorp\example\desktop\turn-off-proxy`
- `robotTaskName`的用法：需要修改两个`.yaml`，同时存在`.robot`文件
  - 参考`104-public-knowledge-base\automation\robocorp\example\dot-robot`
  - 也就是在[[robot-yaml]]中提到的`robot.yaml`中`robotTaskName`字段
    - 写`.robot`文件中的`Tasks`字段下的task名称
    - 比如刚刚的`Minimal task`
  - 同时需要在`conda.yaml`中适当加入内容
    - 内容参考`104-public-knowledge-base\automation\robocorp\example\dot-robot`
    - `pip`有包`conda`没有的现象参考[[pip]]
      - 例如2022.6，`conda`的`rpaframework`只有`9.x`而`pip`有`14.x`
- 这样运行之后在`output`文件夹就除了之前的`stdout.log, stderr.log, *.yaml`，还有`*.xml, *.html`
  - 其中`html`可以用浏览器打开
    - 可以本地资源管理器打开
    - 也可以安装vscode`open in browser`插件后`Alt+B`快捷键