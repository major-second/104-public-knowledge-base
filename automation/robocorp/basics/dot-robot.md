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
- 这是[[robotframework-lang]]
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