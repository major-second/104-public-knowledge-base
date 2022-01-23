比如在`launch.json`中加入
```json
        {
            "name": "Python: Attach using Process Id",
            "type": "python",
            "request": "attach",
            "processId": "${command:pickProcess}",
        }
```
（如果你把104-public-knowledge-base作为工作目录打开，那么你应该已经可以使用这个库里现成的了，如图）
![](attach-json.png)