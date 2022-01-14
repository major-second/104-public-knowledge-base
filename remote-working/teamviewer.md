## 下载安装
teamviewer可以在远程主机没有公网ip时也能远程操控
[下载](https://www.teamviewer.com/en/download/linux/)，用`sudo apt install ./<文件名>.deb`即可安装（或：`sudo apt install <拖动.deb文件到终端>`）
注：截至2022.1.14，`sudo apt install <文件名>.deb`或者`sudo apt install teamviewer*`都是不行的。
使用前可能需要注册一个账号，还需要邮箱和手机，略烦
## 远程ssh打开
首先`ssh`上远程机器
```sh
# 停止teamviewer
sudo teamviewer --daemon stop
# 重启teamviewer
sudo teamviewer --daemon start
# 打印id（用于远程连接）
sudo teamviewer --info print id
# 设置密码
sudo teamviewer --passwd <password>
# 设置开机启动
sudo systemctl enable teamviewerd.service
```
待补全