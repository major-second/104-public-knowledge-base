首先打开代理，比如[[linux]]，[[windows]]
但打开之后还需要配置才能让应用实际走代理，而不是走直连
参考[[vscode/proxy]]，[[settings-and-configurations]]，[[zoom]]等等都有提到
# 系统设定、浏览器走代理
- 浏览器preference等地方可能使用系统设定，也可能手动设置浏览器走的代理
- 总之一般就是设置ip和端口号
- 那系统设定呢？
  - 比如ubuntu的九宫格-齿轮（Settings）
  - Win10的开始菜单搜索proxy
# 环境变量、linux终端走代理
在`~/.bashrc`（当然如果用[[zsh]]就是`~/.zshrc`）中加上
```sh
export https_proxy="localhost:<端口号>"
export http_proxy="localhost:<端口号>"
```
然后重启终端或`source ~/.bashrc`一下，就好了
（也就是[[6-env]]中说的的添加环境变量）
环境变量和ubuntu的设置是两回事
# pip走代理
`pip`自动读取环境变量中的代理设置
但要求`~/.bashrc`里的`$http_proxy`等等变量以`http://`开头，而不是上节那样（如果不这样，会报错，且在报错信息中可以看到应该怎么改）
# 验证结果
- 终端
  - `curl cip.cc`看结果
  - `curl ipinfo.io`看结果
  - `curl www.google.com | grep .toString`看结果
- 浏览器浏览
  - `cip.cc`看结果
  - `ipinfo.io`看结果
  - `www.google.com`看能不能上
- `cip.cc`好处是中文且墙内较快
- `cip.cc`有时用不了，就试试`ipinfo.io`呗