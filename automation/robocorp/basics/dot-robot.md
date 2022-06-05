前置：
- [[robot-yaml]]
- [[pip]]

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
- 这是`robotframework`. 为了使用`.robot`和`robotTaskName`字段，需要在[[robot-yaml]]中提到的`conda.yaml`中适当加入内容
  - 内容参考`104-public-knowledge-base\automation\robocorp\example\dot-robot`
  - `pip`有`conda`没有的现象参考[[pip]]
- `robotTaskName`的用法，参考`104-public-knowledge-base\automation\robocorp\example\dot-robot`
  - 也就是在`robot.yaml`中`robotTaskName`字段
  - 写`.robot`文件中的`Tasks`字段下的task名称
  - 比如刚刚的`Minimal task`