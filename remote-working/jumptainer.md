- 跳板机原理
  - 外网可以直连跳板机，不经过[[vpn]]
  - 跳板机自己可以通过`10.1`之类的内网ip连接公司或学校内网的机器
  - 这样一来你就可以不开vpn连上内网机器
- 举例：[[client-config]]里写

```text
Host jumptainer
    HostName jumptainer.<某某>.com
    Port <某>
Host innet_server
    HostName 10.<某>.<某>.<某>
    ProxyJump jumptainer
```