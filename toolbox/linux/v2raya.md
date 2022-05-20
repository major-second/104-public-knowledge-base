大概过程是先安装`v2ray`，再安装`v2raya`. 过程中需要[[source]]提到的添加源
参考官网教程https://v2raya.org/docs/prologue/installation/debian/
参考[[systemd]]
```sh
curl -Ls https://mirrors.v2raya.org/go.sh | sudo bash
sudo systemctl disable v2ray --now
wget -qO - https://apt.v2raya.mzz.pub/key/public-key.asc | sudo apt-key add -
echo "deb https://apt.v2raya.mzz.pub/ v2raya main" | sudo tee /etc/apt/sources.list.d/v2raya.list
sudo apt update
sudo apt install v2raya
sudo systemctl start v2raya.service
sudo systemctl enable v2raya.service
```
安装后的具体操作参考[[linux]]，[[settings-and-configurations]]等等
- 一个有意思的错误
  - v2raya默认使用`2017`配置[[node]]，而使用`20171`作为代理用的端口。请区分好两者
  - 如果你`http_proxy`错误设置成了`localhost:2017`（把一个本来是有GUI用来配置[[node]]的端口当成了代理用的端口），那么报错`We're sorry but v2rayA-GUI doesn't work properly without JavaScript enabled. Please enable it to continue.`
  - 这非常不直观，让人以为是`localhost:2017`本身出了问题