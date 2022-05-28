- linux直接`apt install git`即可。以下windows
- 下载：
https://git-scm.com/downloads
- 注意[[git-history]]以及`Ctrl+Shift+G`等vscode功能都需要先安装git才能用。相当于vscode只是一个表层接口（“shell”？），参考[[extensions/general]]
- 安装时选项很多，但是全默认即可
  - 此时环境变量[[windows/env-var]]可能没正常设置，那么手动设置才能让powershell使用`git`命令
  - `git clone`等需要和远程连接时，还有一大堆坑，比如[[hosts]]，[[https-ssh]]，[[personal-access-tokens]]
    - 注意`git`和`github`的边界。参考[[other-hubs]]