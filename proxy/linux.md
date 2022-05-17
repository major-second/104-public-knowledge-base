首先安装[[v2raya]]
- 然后看[官网](https://v2raya.org/docs/prologue/quick-start/)，按提示操作导入[[node]]（需要访问`2017`端口）
  - 如果你正在给远程服务器配置代理，可能会遇到浏览器无法访问`<服务器ip地址>:2017`的问题，应该是被服务器的防火墙拦住了。可以把远程的2017端口转发到本地（[[forward-port]]），以绕过防火墙
  - 给本地配置，那就直接浏览器访问`localhost:2017`
- 关于账户密码
  - 第一次需要设置账户密码
  - 之后如果忘记密码可以
    - 先参考[[systemd]]`sudo systemctl stop v2raya`
    - 再使用`sudo v2raya --reset-password`命令来重置
- 之后参考[[settings-and-configurations]]才能真正让软件（shell或者其它应用）走代理