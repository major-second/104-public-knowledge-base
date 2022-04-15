vscode连接服务器时报错，可能是因为第一次连接时没有自动生成`settings.json`[[vscode/settings]]中的配置
```json
"remote.SSH.remotePlatform": {
      "xxx.xx.xx.xx": "linux"
    },
```
可以自己手动在settings.json中加上
参考链接：https://www.cnblogs.com/linux-37ge/p/12639120.html
https://blog.csdn.net/qq_41058526/article/details/105291284