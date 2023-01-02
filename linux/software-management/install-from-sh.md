直接通过`.sh`安装，过程中可能有各种下载之类的，被打包成一起的了，傻瓜式
- 前置[[curl]]
- 那么自然可能有其它过程中原本的问题。比如没有[[proxy/basics]]上不了网……
# 常见方式
- `sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"`，来自[[zsh]]
- `wget https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh; bash ./Ana*.sh`，来自[[conda/installation]]
  - 方便加参数比如`-b`，比较直观
  - 当然`sh -c`那种其实也有`sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended`，不过不太直观
- `curl -Ls https://mirrors.v2raya.org/go.sh | sudo bash`，来自[[v2raya]]
- 各种方式互为[[workaround]]
  - 例如第一种[[escape]]最烦哈哈
  - 第二种`wget`没法识别`ALL_PROXY`，必须用`http_proxy`和`https_proxy`（而且区分大小写！）