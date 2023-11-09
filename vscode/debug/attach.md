- 前置条件：
  - 参考[[4-more-commands]]以了解进程和进程号的基本知识。
  - 了解VSCode中的Python调试，例如[[launch]]。
  - [参考资料github issue](https://github.com/microsoft/debugpy/issues/102)。
  - [[gdb]]

  - 常见问题：安全设置导致用不了
    - 可能参考[[yama-ptrace-scope]]。

# 对Python进程的attach
在`launch.json`中添加以下配置：
```json
        {
            "name": "Python: Attach using Process Id",
            "type": "python",
            "request": "attach",
            "processId": "${command:pickProcess}",
        }
```
- 这里未展示的其他可用选项，如`justMyCode`，请参考[[launch]]。
- 如果你**将104-public-knowledge-base作为工作目录**打开，那么你应该已经可以使用这个库里现成的`.json`文件了，如图：
![](attach-json.png)
- 直接运行`python`本目录下的`sample.py`，然后：
  - 新开一个终端，使用`ps -ef | grep ...`获取进程号。
    - 参见[[4-more-commands]]和[[11-basic-scripting-partB]]。
  - 或者将输入命令从`python <文件名>`改为`python <文件名> &`，直接输出进程号，然后让它在后台运行。
- 现在保持`sample.py`运行，同时按`F5`运行debugger，连接到指定进程。此时可以设置断点等。
- 如果你设置了断点，那么按`F5`后，程序将在断点处停止。
  - 有时会在终端输出`The threading module was not imported by user code in the main thread. The debugger will attempt to work around https://bugs.python.org/issue37416.`
  - 所以，如果出现问题，可以参考https://bugs.python.org/issue37416
- 进阶应用：如果你的Python程序本身有子进程，可以一边使用`watch 'ps -ef ...'`，一边运行脚本，当看到想要的进程时，就开始attach。