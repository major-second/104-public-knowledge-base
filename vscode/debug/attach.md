前置：
- 参考[[4-more-commands]]了解进程、进程号的基本知识。
- vscode中的python调试，例如[[launch]]
- [参考资料github issue](https://github.com/microsoft/debugpy/issues/102)
下面是一些常见问题
  - `sudo apt install gdb`
  - [[yama-ptrace-scope]]

# 对python进程的attach
在`launch.json`中加入
```json
        {
            "name": "Python: Attach using Process Id",
            "type": "python",
            "request": "attach",
            "processId": "${command:pickProcess}",
        }
```
（如果你**把104-public-knowledge-base作为工作目录**打开，那么你应该已经可以使用这个库里现成的了，如图）
![](attach-json.png)
- 直接`python`本目录下的`sample.py`，然后
  - 新开个终端`ps -ef | grep ...`到进程号
    - 参见[[4-more-commands]]和[[11-basic-scripting-partB]]
  - 或者把输入命令从`python <文件名>`改为`python <文件名> &`，直接输出进程号，然后让他后台运行
- 现在保持`sample.py`运行，同时`F5`运行debugger，连接到指定进程。此时可以打断点等
- 如果你打好断点，那么一`F5`他就停在断点处
  - 并且有时会终端输出`The threading module was not imported by user code in the main thread. The debugger will attempt to work around https://bugs.python.org/issue37416.`
  - 所以说出现问题可以看看https://bugs.python.org/issue37416