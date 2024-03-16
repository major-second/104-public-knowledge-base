- 使得内网机器具有公网[[ip-address]]可以ssh
- https://blog.csdn.net/liuxingyuzaixian/article/details/128705262
# 第三方
## ngrok
https://dashboard.ngrok.com/signup
github注册
https://dashboard.ngrok.com/get-started/setup/linux
`ngrok tcp 22`即可得到公网[[ip-address]]和port
类似物有很多如`cpolars`等
一般免费版端口是变化的
但 `ngrok http`可能有静态域名，问题是并不用于[[ssh/ssh]]
## [[autossh]]
- 往往需要云服务器
- [[ssh/ssh]]，`-L`，`-R`等参数[[forward-port]]
## 网卡层映射