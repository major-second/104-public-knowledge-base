首先打开代理，比如[[linux]]，[[windows]]
但打开之后还需要配置才能让应用实际走代理，而不是走直连
参考[[vscode/proxy]]，[[settings-and-configurations]]，[[zoom]]等等都有提到
# linux终端走代理
在`~/.bashrc`（当然如果用[[zsh]]就是`~/.zshrc`）中加上
```sh
export https_proxy="localhost:<端口号>"
export http_proxy="localhost:<端口号>"
```
然后重启终端或`source ~/.bashrc`一下，就好了
（也就是[[6-env]]中说的的添加环境变量）
# pip走代理
`pip`自动读取系统的代理设置
但要求`~/.bashrc`里的`$http_proxy`等等变量以`http://`开头，而不是上节那样（如果不这样，会报错，且在报错信息中可以看到应该怎么改）