- 前置
  - [[vpn]], [[ssh/ssh]], [[pubkey-authentication]]等
# 理论
- 网络七层结构
  - [[vpn]] work比[[proxy/basics]]底层
  - `ping`检查较底层，`telnet`，`ssh`更高层
  - 底层`ping`不通高层往往更加不通（不考虑[[proxy/basics]]等），底层`ping`通了高层未必通（[[pubkey-authentication]]等）
- 常见机器种类
  - 直接连（公用ip），例如金山云之类的服务器商托管
    - 公用ip比较贵！少见！
    - 很多时候是反向[[forward-port]]后，[[ssh/ssh]]非`22`端口（`-p`参数）
  - 连[[vpn]]才能连，确保安全性，但`ip`本身不是内网网段ip而是公用的
  - 连[[vpn]]才能连，确保安全性，`ip`本身也是内网的比如`10.1.某某`
  - 实践中内网`10.1.某某` ip可能会变，需要人去物理机上`ifconfig`等看到
# 实战check连接
https://blog.csdn.net/guweiyu_thinker/article/details/79391495
可以`ping`, `telnet`, `ssh`都试试
- 例子1：`ssh -T git@github.com`可以看你的[[https-ssh]]有没有问题
  - 有一次这个没问题但[[push-pull]]有问题，结果是代理出问题了
- 例子2：`ping`可以但`telnet <ip> 22`不行，发现是被学校防火墙拦了
  - [参考](https://bobcares.com/blog/telnet-connection-refused-by-remote-host/)
- 例子3
  - `telnet <ip> 2017`（[[v2raya]]登录界面）可以看到输出
  - `telnet <ip>`（即默认`23`端口）可以登录
  - `telnet <ip> 22`不行
  - 实际上是没装`openssh-server`，参考[[server-config]]
- 例子4：`ping`对方不行，`ping`学校内网其它机器可以，发现对方关了/内网ip变了