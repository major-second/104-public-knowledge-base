`~/.ssh/config`文件。[[vscode]] 等应用可以读取它
格式参考：
```text
Host <自定义名称>
    HostName <ip>
    Port <端口>
    User root
    PasswordAuthentication yes
    # 注：用密钥登录需要指定IdentityFile <密钥路径>
```
注释`# ...`必须单独成行。如果没有做到，那么`ssh`连接会报错