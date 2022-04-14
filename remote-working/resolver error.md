vscode连接服务器时报错resolver error<br />
原因是第一次链接时没有自动生成settings.json中的配置
```json
"remote.SSH.remotePlatform": {
      "xxx.xx.xx.xx": "linux"
    },
```
可以自己手动在settings.json中加上，之后链接就可以自动生成了。<br />
参考链接：https://www.cnblogs.com/linux-37ge/p/12639120.html
https://blog.csdn.net/qq_41058526/article/details/105291284
todo: 有疑问。下次见面问
