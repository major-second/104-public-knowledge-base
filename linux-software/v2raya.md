大概过程是先安装`v2ray`，再安装`v2raya`. 过程中需要[[source]]提到的添加源
参考官网教程https://v2raya.org/docs/prologue/installation/debian/
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