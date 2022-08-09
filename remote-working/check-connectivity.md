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