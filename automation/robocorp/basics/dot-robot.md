前置：
- [[robot-yaml]]
- [[pip]]
- 会用浏览器或vscode插件查看[[html]]

内容
- 在[[robot-yaml]]提到`tasks - <任务名称> - <command | shell | robotTaskName>`
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
- 这是`robotframework`语言
  - 为了在[[robot-yaml]]中使用`robotTaskName`字段，使用`.robot`，需要在[[robot-yaml]]中提到的`conda.yaml`中适当加入内容
    - 内容参考`104-public-knowledge-base\automation\robocorp\example\dot-robot`
    - `pip`有包`conda`没有的现象参考[[pip]]
      - 例如2022.6，`conda`的`rpaframework`只有`9.x`而`pip`有`14.x`
  - `robotframework`用$\ge 2$个空格分隔“命令”和“参数”
    - “命令”本身可能含有空格，比如`Wait For Element`
    - “命令”在vscode中可以补全
- `robotTaskName`的用法，参考`104-public-knowledge-base\automation\robocorp\example\dot-robot`
  - 也就是在`robot.yaml`中`robotTaskName`字段
  - 写`.robot`文件中的`Tasks`字段下的task名称
  - 比如刚刚的`Minimal task`
- 这样运行之后在`output`文件夹就除了之前的`stdout.log, stderr.log, *.yaml`，还有`*.xml, *.html`
  - 其中`html`可以用浏览器打开
    - 可以本地资源管理器打开
    - 也可以安装vscode`open in browser`插件后`Alt+B`快捷键