- 相当于[[package-managers-source]]，就是去哪里下载
- 配置方法参考[[condarc]]
- 应用
  - 换成国内源如清华源
    - 提速
    - 有时不用国内源连接不稳定导致`OpenSSL`错误等
  - [[pyrosetta/installation]]，有时里面可能有用户名，密码这种东西，用于作为credential
- 风险：[[non-standard]]的源可能导致缺少最新版本，例如`https://mirrors.bfsu.edu.cn`源在2022-8了还只有`torch 1.10`，还是cpu版本的，你`conda install pytorch`如果不加`-c pytorch`竟然默认安装cpu版本的