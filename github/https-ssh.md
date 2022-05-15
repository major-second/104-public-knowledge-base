前置
- [[git/installation]]
- linux需要`apt install openssh-client`
  - windows在安装git时应该默认安装好了（要是没有就自己补）

## 概述
`git clone`https链接不需要加ssh密钥
ssh链接需要
`--recursive`地`git clone`子模块时，默认用ssh链接！所以需要添加密钥
具体操作：参考[官方教程](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys)
## 得到文本
查看是否有公钥`ls -al ~/.ssh`
- 有`id_ed25519.pub`的话跳过生成，直接`cat`它
- 否则：linux生成公钥和启动agent（参考[[generate-key-pair]]）
```sh
ssh-keygen -t ed25519; \
eval "$(ssh-agent -s)"; \
ssh-add ~/.ssh/id_ed25519; \
cat ~/.ssh/id_ed25519.pub # 最后那里ssh-ed开头的就是要复制的
```
- windows生成公钥：只需刚刚的首行和末行
- 总之复制到密钥文本
## 后续操作
- github - 右上角头像 - Settings - 左侧SSH and GPG keys - New SSH key
- 把内容粘贴进文本框并确认（Title可以自定）
- 确认完密码之后，发现我们多了一个SSH key，之后就可以`git clone`需要`ssh`验证的东西了
  - 可以`ssh git@github.com`简单验证
## Troubleshooting
- 对于github，需要创建的是`ed25519`密钥，其他密钥不行！
  - [[other-hubs]]可能不同
- 如果做了所有步骤，github访问仍提示无法验证，linux请先检查ssh agent是否打开！
    - 输入`eval "$(ssh-agent -s)"`即可