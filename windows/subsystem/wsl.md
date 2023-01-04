- 前置
  - 管理员[[administrator]] powershell
  - [[7-permissions]]
- [参考](https://learn.microsoft.com/zh-cn/windows/wsl/install)
- 管理员[[administrator]] powershell
  - linux系统的[[CRUD]]
  - 不同时期可能不同。时至2022.12
  - 增：`wsl --install`
    - 直接出现列表
    - 然后选择一个distro即可
    - 例如`wsl --install -d Ubuntu-20.04`
    - 再加`--quiet --user myuser --password mypassword`：[[silent]]（不过明文写出了密码，不推荐）
  - 删：`wsl --unregister Ubuntu-20.04`即可
  - 查：`wsl --list`
  - 其实现在的是WSL2，一些地方和WSL不同，比如网络模式不是直接用主机网络，也就不能直接使用`127.0.0.1:<端口>`的代理
  - 可能需要更新一个内核，[参考](https://learn.microsoft.com/zh-cn/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package)
  - 如果没有`--user, --password`，则出现新窗口，显示`Enter new UNIX username:`等，参考[[7-permissions]]
- 此时可以尝试运行各种命令了
  - 比如`sudo apt update`
    - 然后装软件，例如linux的[[git/init/installation]]（`sudo apt install git`）
    - [[v2raya]]这种则需要[[wsl-systemd]]
  - 比如使用windows的代理
    - [参考](https://zhuanlan.zhihu.com/p/153124468)
      - 核心代码`host_ip=$(cat /etc/resolv.conf |grep "nameserver" |cut -f 2 -d " ")`，然后端口该是啥是啥
      - [[configure]]有讲
    - 注意需要[[configure]]监听`0.0.0.0`
      - 而且有些客户端如geph还需要[[refresh]]重连（有些却不需要）
    - 然后当然就可以[[zsh]]等
  - [[conda/installation]]
- 之后入口
  - 开始菜单可能有
    - 比如`Ubuntu`等字样
  - vscode，例如[[wsl-develop]]
  - [[wsl-command]]
    - 在[[powershell/basics]]中运行
    - 可以高度自动化，[[silent]]