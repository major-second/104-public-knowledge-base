前置
- [[git-installation]]
- linux需要`apt install openssh-client`
  - windows在安装git时应该默认安装好了（要是没有就自己补）
- 了解[[generate-key-pair]]，[[check-connectivity]], [[ssh/ssh]]

## 概述
- 区别
  - [[clone]] https链接
    - 不需要加ssh密钥[[generate-key-pair]]
    - 但需要[[personal-access-tokens]]
  - ssh相反
    - 具体增加ssh密钥的操作参考
      - [官方教程](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys)
      - 自己使用
        - 可以用[[client-config]]
          - [参考](https://blog.csdn.net/junbujianwpl/article/details/78650105)
          - ```text
            Host github.com
              User git
              Hostname github.com
              IdentityFile ~/.ssh/id_ed25519
            ```
          - 也可以用[[config]]，例如`git config --global core.sshCommand "ssh -i $GIT_SSH_KEYFILE -o StrictHostKeyChecking=no"`
  - url体现：典型如下
     - https: `https://github.com/username/reponame.git`
     - ssh: `git@github.com:username/reponame.git`
- ssh连接可以方便换人，不同人用不同私钥
- 何时必须需要ssh链接？
  - 很多[[submodule]]，不想逐个输入密码时
  - 有时`https`链接玄学[[clone]]，[[push-pull]]不了，那就要用`ssh`链接，作为[[workaround]]
    - [一个例子](https://stackoverflow.com/questions/7489813/github-push-error-rpc-failed-result-22-http-code-413)：当[[submodule]]正常[[push-pull]]，主模块错误码`413`时，可以试试
## 得到文本
查看是否有公钥`ls -al ~/.ssh`
- 有`id_ed25519.pub`的话跳过生成，直接`cat`它
- 否则：linux生成公钥和启动agent（参考[[generate-key-pair]]）
```sh
mkdir ~/.ssh; \
ssh-keygen -t ed25519 -N '' -f ~/.ssh/id_ed25519; \
eval "$(ssh-agent -s)"; \
ssh-add ~/.ssh/id_ed25519; \
cat ~/.ssh/id_ed25519.pub # 最后那里ssh-ed开头的就是要复制的
```
- windows生成公钥
  - 只需刚刚的首行和末行
  - 其中`ssh-keygen`可能带有后缀名`.exe`
  - 即以下（中途可能需要回车和`y`等）
```powershell
cd ~/.ssh; `
ssh-keygen.exe -t ed25519; `
cat ~/.ssh/id_ed25519.pub
```
- 总之复制到密钥文本
## 后续操作
- github - 右上角头像 - Settings - 左侧SSH and GPG keys - New SSH key
- 把内容粘贴进文本框并确认（Title可以自定）
- 确认完密码之后，发现我们多了一个SSH key，之后就可以`git clone`需要`ssh`验证的东西了
  - 可以`ssh -T git@github.com`简单验证是否配置成功
  - [参考](https://segmentfault.com/q/1010000007607194)
## Troubleshooting
- 对于github，需要创建的是`ed25519`密钥，其他密钥不行！
  - [[other-hubs]]可能不同
- 如果做了所有步骤，github访问仍提示无法验证，linux请先检查ssh agent是否打开！
    - 输入`eval "$(ssh-agent -s)"`即可
## [[known-hosts]]
- 除了github信任你，你也要信任github，所以第一次使用ssh会要求你确认
- 想跳过？`ssh -o "StrictHostKeyChecking=no" -T git@github.com`，之后就都不需要了，参考[[known-hosts]]
