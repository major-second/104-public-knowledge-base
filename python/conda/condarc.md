`~/.condarc`：刚下载conda时没有。任何时候`conda config`了（比如用`conda config --add`增加channel等）就创建（也可以手动创建）
使用yaml标记语言
典型：设置代理
```yaml
proxy_servers:
 http: http://127.0.0.1:端口
 https: http://127.0.0.1:端口
```