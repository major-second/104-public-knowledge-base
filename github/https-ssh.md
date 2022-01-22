https链接不需要加ssh密钥
ssh链接需要
`--recursive`地`git clone`子模块时，默认用ssh！所以需要添加密钥
具体操作：参考[官方教程](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys)
- 准备和查看是否有公钥
```sh
apt update; \
apt install openssh-client; \
apt install git; \
ls -al ~/.ssh
```
有的话跳过生成，直接`cat`，否则
```sh
ssh-keygen -t ed25519; \
eval "$(ssh-agent -s)"; \
ssh-add ~/.ssh/id_ed25519; \
cat ~/.ssh/id_ed25519.pub # 最后那里ssh-ed开头的就是要复制的
```
- 总之复制到密钥文本
- github - 右上角头像 - Settings - 左侧SSH and GPG keys - New SSH key
- 把内容粘贴进文本框并确认（Title可以自定）
- 确认完密码之后，发现我们多了一个SSH key，之后就可以`git clone`需要`ssh`验证的东西了