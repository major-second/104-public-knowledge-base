前置：
- [[linux翻墙]]
# `zsh`
- 输入命令
```sh
sudo apt install zsh; \
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"; \
chsh -s /bin/zsh
```
注：这里的`chsh`是不是让你想到[[7-permissions]]的`chmod`？
- 把`~/.bashrc`必要的设置放到`~/.zshrc`
- 安装插件
```sh
. ~/.zshrc; \
sudo apt install autojump; \
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting; \
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions; \
vim ~/.zshrc
```
- 在出来的编辑器里，加插件名`autojump zsh-autosuggestions zsh-syntax-highlighting`（和`git`并列）
  - 顺序：`zsh-syntax-highlighting`必须在最后！
- `. ~/.zshrc`（更新）
## `chsh` Troubleshooting
- 不能用`sudo`，否则`vim /etc/passwd`（参考[[7-permissions]]）就会发现改的是`root`的，不是自己的
  - 虽然`sudo`和不`sudo`都要求输入密码，但是其本质是不同的
  - 不`sudo`的输入密码类似于[[7-permissions]]中说过的`passwd`命令的原理。即用户还是自己（非`root`），“临时”获得了高级权限。
- 需要重新登录，才生效！