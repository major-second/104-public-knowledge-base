文件路径：`~/.condarc`
- 刚下载conda时没有
- 任何时候`conda config`了就自动创建
  - 比如用`conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/`增加channel，参考[[pytorch/basics/installation]]
  - 结果：
    - `channels:`
      - `https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/`
      - `defaults`
  - 使用[[yaml]]语法
- 也可以手动创建并设置内容
- 典型例子：设置代理
```yaml
proxy_servers:
 http: http://127.0.0.1:端口
 https: http://127.0.0.1:端口
```