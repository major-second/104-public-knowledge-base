前置：
- [[linux翻墙]]（否则`githubusercontent`用不了）
# `zsh`
0. 输入命令
```sh
apt install -y sudo git && \
sudo apt install -y zsh && \
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```
现在已经到`zsh`里面了
```sh
sudo apt install -y autojump; \
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting; \
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions; \
sed -i 's/(git)/(git autojump zsh-autosuggestions zsh-syntax-highlighting)/g' ~/.zshrc; \
. ~/.zshrc
```
- 对于服务器或docker容器，需要先`apt install -y sudo git`这俩
- `sed`一行中，`zsh-syntax-highlighting`必须在最后！
- 跑完上述命令，最后要把`~/.bashrc`必要的设置放到`~/.zshrc`（并更新），比如`export`，比如`CUDA`，`conda`设置，`ssh`服务打开等七七八八
- 注意`zsh`平常能提高效率，但有时关键时刻会造成麻烦。有些奇怪错误产生了，可以换回`bash`试试。参见[[non-standard]]
## `chsh`
- `chsh -s /bin/zsh`可以手动改默认`zsh`
  - 这里的`chsh`是不是让你想到[[7-permissions]]的`chmod`？
  - 注：当然，刚刚运行命令之后本来也有一个可以选择默认`zsh`的询问
- 这里不能用`sudo`，否则`vim /etc/passwd`（参考[[7-permissions]]）就会发现改的是`root`的，不是自己的
  - 虽然`sudo`和不`sudo`都要求输入密码，但是其本质是不同的
  - 不`sudo`的输入密码类似于[[7-permissions]]中说过的`passwd`命令的原理。即用户还是自己（非`root`），“临时”获得了高级权限。
- `chsh`设定需要重新登录，才生效！