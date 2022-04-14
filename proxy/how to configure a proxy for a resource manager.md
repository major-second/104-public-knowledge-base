首先安装`v2raya`这个工具，参考[[v2raya]]<br />
然后在官网“https://v2raya.org/docs/prologue/quick-start/
按提示操作<br />
其中可能会遇到浏览器无法访问localhost:2017的问题，应该是被防火墙拦住了，可以在vscode下面的终端的`终端`后面的`端口`里面，点击`在浏览器中打开`以绕过防火墙。<br />
可以以管理员身份自己起名字和密码，如果忘记密码可以使用`sudo v2raya --reset-password`命令来重置<br />
其中“导入节点”一步需要找实验室管理员（或者自己买）神秘二维码或神秘分享链接<br />
之后把代理用到服务器上的一种方法是，在~/.bashrc中加上
```sh
export https_proxy="localhost:20171"
export http_proxy="localhost:20171"
```
然后source一下，就好了。
