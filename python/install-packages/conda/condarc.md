- 文件路径：`~/.condarc`
  - 刚下载conda时没有
  - 任何时候`conda config`了就自动创建
## 使用命令
- 比如用`conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/`
  - 增加[[channel]]
  - 参考[[pytorch/basics/installation]]
- 结果：
  - `channels:`
    - `https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/`
    - `defaults`
- 注：如果你想只用清华，确保速度（或者有些场合只有清华在白名单），可以把最后一行删掉
## 手动创建并手动输入内容
- 参考[[settings-and-configurations]]，手动输入和命令的作用是一样的
- 参考[[yaml]]语法
- 典型例子：设置代理
```yaml
proxy_servers:
 http: http://127.0.0.1:端口
 https: http://127.0.0.1:端口
```
- 或：使用清华源[[channel]]
```yaml
channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
show_channel_urls: true
```