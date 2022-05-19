Anaconda是包和环境管理器，利于制造出互不干扰的`python`程序运行环境。且内置常用科学包。
## Windows
- [官网](https://www.anaconda.com/)下载
- 安装（过程中可能涉及[[windows/env-var]]的更改。是否要改就根据你的想法和需要）
- 开始菜单搜索`Anaconda Prompt`，里面就可以用[[commands]]
  - 当然为了方便，可以把快捷方式发送到桌面
  - 这个`Prompt`能用conda的[[commands]]和`cd`、`python`，但不能`ls`等，所以说和linux终端还是不同
  - 当然和[[powershell]]也不同。因为如果你没加[[windows/env-var]]之类的，那么powershell没法`conda`（但powershell可以`ls`）
## Linux
- [官网](https://www.anaconda.com/)下载（可能浏览器下也可能找到对应链接后`wget`下载
  - 总之得到某个`.sh`
- 运行该`.sh`脚本，参考[[11-basic-scripting-partA]]
  - 即给`777`权限后直接`./某某.sh`，或者`bash 某某.sh`
- 过程中根据提示操作。其中如果`init`处选了`y`，那么你`cat ~/.bashrc`结尾就能看到添加的一些语句
  - 哦，你用的[[zsh]]就去看`~/.zshrc`
  - 如果你要两者都用，之后需要`conda init <SHELL>`，参考[[docker/conda]]中的操作
- `conda --version`检查安装结果