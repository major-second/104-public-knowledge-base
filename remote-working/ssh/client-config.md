`~/.ssh/config`文件
# 基础
[[vscode]] 等应用可以读取它
格式参考：
```text
Host <自定义名称>
    HostName <ip>
    Port <端口>
    User root
    PasswordAuthentication yes
    # 注：用密钥登录需要指定IdentityFile <密钥路径>
```
# 注意
注释`# ...`必须单独成行。如果没有做到，那么`ssh`连接会报错
# 其他用法
## alias
- 类似[[aliases]]
- 利用刚刚[[client-config#基础]]中的
- 使得可以直接`ssh <自定义名称>`
## 设置默认端口和key
- `Host`和`HostName`相同，都是[[ip-address]]或域名
- 则可用于
  - `ssh <user>@<ip>`直接成功
  - git [[remote]]设置后，不需要[[config]] `core.sshCommand`等