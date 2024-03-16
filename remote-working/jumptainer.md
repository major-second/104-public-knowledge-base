- 跳板机原理
  - 外网可以直连跳板机（跳板机有公网ip），不需经过[[vpn]]
  - 跳板机自己可以通过`10.1`之类的内网ip连接公司或学校内网的机器
  - 这样一来你就可以不开vpn连上内网机器
- 场景1：管理员配好了，你只需要用
  - [[client-config]]里一个局部如下
  - 具体怎么写联系管理员
    ```text
    Host jumptainer
        HostName jumptainer.<某某>.com
        Port <某某>
    Host innet_server
        HostName 10.<某>.<某>.<某>
        ProxyJump jumptainer
    ```
- 场景2：自己有权限，自己配，参考[[autossh]] [[forward-port]]
  - 跳板机需要
    - 打开防火墙 例如
      - 云服务厂商网页控制台例如 aws instance所属的security group等
      - `iptables`等
    - 设置[[server-config]]
      - `.d`作用参考[[settings-and-configurations]]
      - ```
        $ cat /etc/ssh/sshd_config.d/reverse-proxy.conf 
        GatewayPorts yes
        AllowTcpForwarding yes
        ```
      - 重启服务 `sudo service sshd restart`
  - 内网机器能连接跳板机，然后
    - `apt-get install autossh`安装[[autossh]]
    - 运行并加入`~/.bashrc, ~/.zshrc`等使得以后都自动运行：`autossh -M 4010 -NfR 2422:localhost:22 跳板机user@跳板机ip`
      - 参数含义参考[[autossh]], [[ssh/ssh]]
      - 可以结合另一个[[tmux]]窗口 `watch 'lsof -i:4010'`查看端口情况
    - 这是个远程[[forward-port]]
  - 从而以后其他地方`ssh -p 2422 内网机器user@跳板机ip`即可