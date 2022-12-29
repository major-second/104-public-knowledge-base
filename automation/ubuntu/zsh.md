前置：
- [[linux-client]]翻墙
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
  - `export`的[[configure]]
  - [[ros/installation]]中的`source`命令
  - `CUDA`，`conda`设置，`ssh`服务打开等七七八八的东西
- 注意`zsh`平常能提高效率，但有时关键时刻会造成麻烦。有些奇怪错误产生了，可以换回`bash`试试。参见[[non-standard]]
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
## troubleshooting
- 参考[[non-standard]]，zsh很多时候方便，但有时也会造成麻烦
- 可以参考[[6-env]], [[12-condition]], [[shebang]]
  - 使用`#! /bin/bash`或者`if [[ $shell = bash ]]`这种保护你的脚本不出错
## 特性
- `$(`开头的开放区域中可以tab补全，`)`括起来后tab出现结果
- 刚刚的命令中加入了`j`命令快速跳
  - 进过某个文件夹，就可以`j <部分名字>`过去，或`j <部分名字然后Tab>`选择
  - 还有`jc`（子文件夹等），看`man autojump`可看到[[help]]
- 语法高亮`zsh-syntax-highlighting`
  - 正确的绿，错误的红
  - 如果你的命令中包含`cd`，那么可能有些假的错误（红）
    - 甚至导致`alias`也出现假的红
- 自动补全`zsh-autosuggestions`：储存已有命令，`方向键右`补全。注意不是`tab`