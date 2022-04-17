# 了解底层原始操作是有必要的
- 很多人争议说要不要用命令行，还是只用IDE就够了。个人认为命令行的基础操作要有了解。在此基础上，在适用的时候可以用IDE节省时间
- 总之你完全不了解命令行的原始操作，肯定不行。原始操作需要有所理解，但包你也得会调，这样效率才最高
- 比如上层整合可能有的时候不把底层的错误传递出来
  - vscode的[[remote-ssh]]插件在远程公钥变了的时候不把错误传递出来，这时你就得知道底层命令`ssh`，才能发现错误所在
  - vscode的[[git-history]]插件在有untracked文件冲突时checkout没反应且不报错。这是你就得知道底层命令`git`，才能发现错误所在
  - [[ssh-config]]中提到注释必须单独成行。如果没有做到，那么直接`ssh`连接会报错，但vscode会吃掉报错信息
  - 比如[[assets]]中的这个
![](assets.png)
- 比如上层整合可能引入额外的错误
  - 比如2022.1.17，vscode默认集成终端中跑[[rl-example]]就是不行。直接`Ctrl + Alt + T`的就是可以。可能和权限有关
  - `pickle`可以，`torch`不行：https://github.com/dmlc/dgl/issues/458
  - 比如vscode的[[remote-ssh]]时，对面服务器的要求可能不满足（https://code.visualstudio.com/docs/remote/linux#_remote-host-container-wsl-linux-prerequisites
）
但此时直接命令行`ssh`可以登录，然后`sudo apt install`对应包就行了
（但这里要小心，因为升级`gcc`版本等可能有[[upgrade]]所描述的问题。总之升级到最新不一定是可行的！）
- 比如上层封装太死，不灵活
  - 比如证明[[相合性]]在无法使用强大数律时，拆一层包装直接用[[borel-cantelli]]