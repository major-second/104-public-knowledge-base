## 下载安装
teamviewer可以在远程主机没有公网ip时也能远程操控
[下载](https://www.teamviewer.com/en/download/linux/)，用`sudo apt install ./<文件名>.deb`即可安装（或：`sudo apt install <拖动.deb文件到终端>`）
注：截至2022.1.14，`sudo apt install <文件名>.deb`或者`sudo apt install teamviewer*`都是不行的。
使用前可能需要注册一个账号，还需要邮箱和手机，略烦
## 提速
![](speed.png)
连接上去之后，上方`View`处改分辨率，并设置“速度优先”
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
## 坑
- 想远程连，设的分辨率很低，则现场看，界面显示可能不全（特别地，登录窗口都有可能看不到）。不过远程看正常
在现场使用的人可以鼠标移到“边上”，让他过去即可。像一些战略游戏一样。
- teamviewer不会传递`Ctrl + Shift + T`，`Ctrl + Shift + Del`等快捷键
## 建议
- 再怎么样，远程还是有点卡，不建议用远程桌面写代码。
    - 建议只用`teamviewer`作监视
      - 比如有GUI的[[pybullet]]状态
    - 多用终端，[[forward-port]]和[[jupyter-notebook/basics]]等等做[[workaround]]，减少使用远程桌面
    - 用vscode
      - [[remote-ssh]]过去调非常方便
      - 也可以在那边终端启动一个进程之后[[attach]]
- 适应卡
  - 盲打
  - 习惯敲键盘出东西有延迟
  - 终端中，推荐[[zsh]]中自动补全插件等
  - 习惯鼠标点击后有延迟
  - 减少鼠标拖动操作
  - 减少连续操作