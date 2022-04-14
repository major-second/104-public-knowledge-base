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
## 上手操作
https://v2raya.org/docs/prologue/quick-start/
浏览器访问`localhost:2017`，然后安装官网提示操作。其中“导入节点”一步需要找实验室管理员（或者自己买）神秘二维码或神秘分享链接

这里启动了只是让2017端口可以翻。但真正要翻，还需要使得你的应用走这个端口。参考[[settings-and-configurations]]. 比如使用`git config`，比如设置环境变量[[6-env]]等