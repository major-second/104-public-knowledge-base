- 前置
  - 过程中需要添加软件[[software-management/source]]
  - 需要[[systemd]]
    - [[sysvinit]]好像不行
- 大概过程是先安装`v2ray`，再安装`v2raya`
  - 参考官网教程https://v2raya.org/docs/prologue/installation/debian/
    - 这是一个[[read-doc]]例子。这里的`wget -qO`和`echo "deb`那两行的网址可能变，所以你如果不记文档网址只记命令，可能给自己找麻烦
```sh
curl -Ls https://mirrors.v2raya.org/go.sh | sudo bash; \
sudo systemctl disable v2ray --now; \
wget -qO - https://apt.v2raya.org/key/public-key.asc | sudo tee /etc/apt/trusted.gpg.d/v2raya.asc; \
echo "deb https://apt.v2raya.org/ v2raya main" | sudo tee /etc/apt/sources.list.d/v2raya.list; \
sudo apt update; \
sudo apt install v2raya; \
sudo systemctl start v2raya.service; \
sudo systemctl enable v2raya.service
```
安装后的具体操作参考[[linux-proxy-client]]，[[settings-and-configurations]]等等
# troubleshooting
- 代理突然出问题用不了（比如[[pip]], [[conda/commands]]等不正常）？可以尝试登录一下配置[[node]]的端口（`2017`）更新，换换[[node]]试试
- 一个有意思的错误
  - v2raya默认使用`2017`配置[[node]]，而使用`20171`作为代理用的端口。请区分好两者
  - 如果你`http_proxy`错误设置成了`localhost:2017`（把一个本来是有GUI用来配置[[node]]的端口当成了代理用的端口），那么报错`We're sorry but v2rayA-GUI doesn't work properly without JavaScript enabled. Please enable it to continue.`
  - 这非常不直观，让人以为是`localhost:2017`本身出了问题。实际上只要把`http_proxy`和`https_proxy`设置成`localhost:20171`即可