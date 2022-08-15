如果普通的ssh连接没事，用同样的[[client-config]]，vscode连接服务器时报错
- 可能是因为第一次连接时没有自动生成[[vscode/settings]]中的`json`配置
  - 参考链接
    - https://www.cnblogs.com/linux-37ge/p/12639120.html
    - https://blog.csdn.net/qq_41058526/article/details/105291284
  - 可以自己手动加上，比如这种
```json
"remote.SSH.remotePlatform": {
      "<ip>": "linux"
    },
```
- 可能是因为server不满足某些[依赖](https://code.visualstudio.com/docs/remote/linux#_remote-host-container-wsl-linux-prerequisites)