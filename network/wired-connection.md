对于[[connect-base]]这种需要用网线连接的设备
- 确认对方的IP地址（一般是内网地址）。例如[[connect-base]]的视频教程里说franka机械臂底座是`192.168.0.1`
- 到本机的有线网设置，手动设置自己的ip地址为同一网段，例如![](wired-connection.png)
- 即可正常连接`192.168.0.1`
- 当然有时重新开关ubuntu的有线网，或者插拔之后，DHCP就可以自动分配一个合适的ip地址则无需手动
- Sometimes rebooting solves the problem of connection...
  - 总之，出问题时可以试试[[refresh]]