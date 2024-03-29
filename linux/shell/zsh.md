前置：
- [[linux-proxy-client]]翻墙
# `zsh`
- 输入命令
```sh
sudo apt install -y git && \
sudo apt install -y zsh && \
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```
现在已经到`zsh`里面了
- 然后
```sh
sudo apt install -y autojump; \
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting; \
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions; \
sed -i 's/(git)/(git autojump zsh-autosuggestions zsh-syntax-highlighting)/g' ~/.zshrc; \
. ~/.zshrc
```
- 对于服务器或docker容器，需要先`apt install -y sudo git`这俩
- `sed`一行中，`zsh-syntax-highlighting`必须在最后！
- 跑完上述命令，最后要把`~/.bashrc`必要的设置放到`~/.zshrc`（并更新），比如
  - `export`的[[configure-proxy]]
  - [[ros/installation]]中的`source`命令
  - `CUDA`，`conda`设置，`ssh`服务打开等七七八八的东西
- 如果想要[[silent]]（即全程在`bash`完成`zsh`安装），需要
  - `sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended`
  - 参考这个`https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh`本身的注释
## `chsh`
- `chsh -s /bin/zsh`可以手动改默认`zsh`
  - 这里的`chsh`是不是让你想到[[7-permissions]]的`chmod`？
  - 注：当然，刚刚安装时本来也有一个可以选择默认`zsh`的询问
- 这里不能用`sudo`，否则`vim /etc/passwd`（参考[[7-permissions]]）就会发现改的是`root`的shell，不是自己的
  - 虽然`sudo`和不`sudo`的`chsh`都要求输入密码，但是其本质是不同的
  - 不`sudo`的输入密码类似于[[7-permissions]]中说过的`passwd`命令的原理。即用户还是自己（非`root`），“临时”获得了高级权限。
- `chsh`设定需要重新登录，才生效！
## 和`bash`区别
- 参考：[[6-env]], [[12-condition]], [[shebang]], [[escape]]
- 参考[[non-standard]]，zsh很多时候方便，但有时也会造成麻烦
  - 有些奇怪错误产生了，可以换回`bash`试试。因为基本上`bash`还是一般标准
  - 脚本中，可使用`#! /bin/bash`指定（[[shebang]]）
  - 没有[[shebang]]的可以`bash <名字>.sh`强制
- 怎么知道自己用的是bash还是zsh？
  - `$SHELL`不行。你zsh中再bash就知道错
  - `$0`只在交互中可以，跑脚本不行
    - 参考[[shell-type]]
  - `ps`可以看到，但也是交互中可以，跑脚本很麻烦
- 所以可以使用一些特性
  - 可以用数组特性区分zsh和bash：在你**确定只用这两种时**，可以`a=(1); if test ${a[1]}; then export SH_NAME=zsh; else export SH_NAME=bash; fi`
  - [[17-function]]中是否必须加分号：`bash -c "function run { echo test  }; run"; echo $?; bash -c "function run { echo test; }; run"; echo $?; zsh -c "function run { echo test   }; run"; echo $?`
  - `function test-loop { for i in {$1..8}; do echo $i; done; }; test-loop 1`运行结果不同
- 其它特性
  - 直接粘贴多行，`bash`会自动运行前面的，且把一些行可能直接解释为密码等输入而非命令，参考[[copy-paste]]
  - `rm`中带有`*`会让你确认
    - 可以`setopt RMstarsilent`去除
    - 更多选项[参考](https://zsh.sourceforge.io/Doc/Release/Options.html)
## 优良特性
- `$(`开头的开放区域中可以tab补全，`)`括起来后tab出现结果
- 刚刚的命令中，安装了`autojump`，所以可以`j`命令快速跳
  - **进过某个文件夹**，之后就可以`j <部分名字>`过去，或`j <部分名字然后Tab>`选择
  - 还有`jc`（子文件夹等），看`man autojump`可看到[[help]]
- 语法高亮`zsh-syntax-highlighting`
  - 正确的绿，错误的红
  - 如果你的命令中包含`cd`，那么可能有些假的错误（红）
    - 甚至导致`alias`也出现假的红
- 自动补全`zsh-autosuggestions`
  - 储存已有命令，`方向键右`补全
  - 注意不是`tab`补全。两种补全含义不同
  - `$HISTFILE`找到其使用的历史记录地址