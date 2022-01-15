```sh
sudo apt install zsh; \
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```
把`~/.bashrc`必要的设置放到`~/.zshrc`
`zsh`
```sh
. ~/.zshrc; \
sudo apt install autojump; \
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting; \
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions; \
vim ~/.zshrc
```
加插件名`autojump zsh-autosuggestions zsh-syntax-highlighting`
`. ~/.zshrc`