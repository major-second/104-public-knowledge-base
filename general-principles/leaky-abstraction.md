[leaky abstraction现象](https://en.wikipedia.org/wiki/Leaky_abstraction)，维基上不少例子
在许多学科都有（数学较少），计算机工程中尤其常见
- 例如很多人争议说要不要用命令行，还是只用IDE就够了
  - 根据leaky abstraction原则，命令行的基础操作要有了解
  - 在此基础上，在适用的时候可以用IDE节省时间
- 你完全不了解原始操作，肯定不行。原始操作需要有所理解，但高级包你也得会调，这样效率才最高
  - [[11-planning]]的第四节与这非常相关
- 比如上层整合可能有的时候不把底层的错误传递出来（或者传递不清晰），需要直击底层才能找到错误所在
  - vscode的[[remote-ssh]]插件在远程公钥变了的时候不把错误传递出来，这时你就得知道底层命令`ssh`，才能发现错误所在
  - vscode的[[git-history]]插件在有untracked文件冲突时checkout没反应且不报错。这是你就得知道底层命令`git checkout`，尝试一下，才能发现错误所在
  - vscode的git功能遇到[[submodule]]作为changes出现conflict时
    - ![](submodule-changes-conflict.png)
    - gui无法正常stage和commit
    - 必须手动命令行`git add <submodule文件夹名>`
  - [[client-config]]中提到注释必须单独成行。如果没有做到，那么直接`ssh`连接会报错，但vscode会吃掉报错信息
  - [[assets]]中的这个![](assets.png)
  - [[moveit-real-robot]]的命令不能运行，要[[fci]]里的底层命令才能传递出真正的错误原因
  - [[aruco]]中`clone`错分支导致运行时会process died，然后没任何日志，你要是不会底层操作就只能仔细检查，猜哪里出错。猜到是分支错算你厉害
  - [[franka-ros-interface]]是非官方库，没有特别好的维护。[[troubleshooting]]说的gripper disconnected需要插拔网线的错误没法传出来（即明明失败还返回`True`）
- 拓展：可能从上到下逐级看（或级太多时二分看），精确看到底是哪一级出错
  - 比如[[moveit-real-robot]]，[[fci]]的`communication_test`，直接`ping`就是三级
  - 比如[[check-connectivity]]
- 比如上层整合可能引入额外的错误
  - 比如2022.1.17，vscode默认集成终端中跑[[rl-example]]就是不行。直接`Ctrl + Alt + T`的就是可以。可能和权限有关
  - 有的对象`pickle`可以，`torch`的[[save]]不行：https://github.com/dmlc/dgl/issues/458
  - 比如vscode的[[remote-ssh]]时，对面服务器的要求可能不满足（https://code.visualstudio.com/docs/remote/linux#_remote-host-container-wsl-linux-prerequisites
）
但此时直接命令行`ssh`可以登录，然后`sudo apt install`对应包就行了
（但这里要小心，因为升级`gcc`版本等可能有[[software-management/upgrade]]所描述的问题。总之升级到最新不一定是可行的！）
- 比如上层封装太死，不灵活
  - 比如证明[[相合性]]在无法使用强大数律时，拆一层包装直接用[[borel-cantelli]]
  - 比如面试：“python是传值还是传引用”
    - 实际上，难以用二元对立简单概括python行为。因为python传引用但是赋值是重新绑定
    - 不能用简单的term来概括！
  - 比如[[import]]中提到的[[omegaconf/basic]]和其上下级的关系
  - 比如[[robocorp/basics/installation]]中提到`rcc.exe`和vscode集成的关系（集成的必须用`conda.yaml`配置环境）
- 有时上层抽象不如你想象的clean
  - [[risk]]提到了直接删除第二系统的分区是不行的
  - [[partition]]中，直接移动系统盘分区是不行的
  - 刚刚的这些操作甚至有可能导致你[[u-disk-boot]]里的ubuntu都坏掉，必须格掉重写