[toc]
- 参考[[compatibility]], [[general-software-technical/upgrade]]
# semantic-versioning
- 一种版本号的规范
# 版本号
## 查看版本号
- 命令行：往往是`--version, -V, -version`等
  - 如`ffmpeg -version`
  - `python -V`
  - 特殊：`uname -a`看linux系统版本
- [[apt-version]]管理
  - `apt list <包名>`看已经装的
  - `apt-cache madison <包名>`看可用的
- `python`包经常有`__version__`属性，如`torch.__version__`
- 有时可以使用[[pip]]这种包管理器查看所有包信息，自然也包括版本
  - 注意结合[[find-grep]]使用，如`pip list | grep torch`
- 注：有时可以配好一份环境作为参考，之后出问题了就回这台好的环境，查看版本号
  - 刚刚所说的[[apt-version]]管理就派上用场了
  - 例如[[moveit-installation]], [[franka-ros-interface]]用到
## 常识
- 经常是`数字.数字.数字`等几层的形式
  - 前面是大版本号，后面是小版本号。数字越大时间越靠后
  - `3.2`肯定比`3.10`靠前
  - 也就是不能简单对字符串按字典序排序！
  - `major.minor.patch`
  - [参考](https://code.visualstudio.com/api/working-with-extensions/publishing-extension#prerelease-extensions)
    - 这是[[my-own-vscode-extension]]中的
- 大版本号自然往往都是大改
  - 比如`python3`相对`python2`，`tf2`相对`tf1`这种，完全就当成两个东西来看比较好2333
  - 往往不能向后兼容[[compatibility#backward]]
- 有时不用数字做版本号
  - 比如[[ros/installation]]，用`a`开始的字母做版本号，越靠后的版本字母越靠后
  - 比如[[numpy-basics]]除了表层的数字版本号，还有一个靠底层的`0xf, 0x10`等十六进制的版本号，这个和数字版本号不一一对应。[[pytorch/basics/installation]]时可能需要这个版本号满足一定条件，进而依赖于一定版本的numpy
- 安装软件，`git clone`等等时往往都要看清楚版本号
  - 例如[[aruco]]，在`git clone`时要`-b`选择正确分支
- 表述版本号
  - 很多地方用`>=`，`==`，`=`等运算符表示版本号
    - 比如`>=`表示数字更大（“之后”）
    - [[conda-installation]]用`=`表示确定某个版本，[[pip]]用`==`
  - 参考[[poetry-dependency-specification]]有更多
- 一般版本号高性能好，功能多，参考[[general-software-technical/upgrade]]，但不是永远版本越高越好
## 数字以外各种标记
- `lts`长期支持
- `dev`开发中
  - 可能不稳定
  - 好处：多很多“开发用”的东西，比如源码，头文件等
  - 有时即使你不是在开发，在需要源码、头文件、额外组件等时也需要安装`dev`版本
- `64`或`32`对应64或32位系统
  - 有时和操作系统名称结合，如`win32`版
  - `amd64`只是说架构是AMD发明，并没有说intel的芯片就用不了
- 操作系统名：`win, linux, mac`等
- `portable`可以到处移动，而不是“安装了就动不了”
- 商业软件：例如`perfessional`，`extreme`，`community`等区分等级
  - 如[[aida64]]
  - 不同等级序列号不能混用
    - 比如[[vmware]]
  - 有时，有序列号可以升级到高等级
    - 如[[windows/upgrade]]
  - 高级版本当然有高级功能，比如[[pycharm/installation]]，社区版对[[jupyter-basics]]只读
  - 更多参考[[pricing]]
- 有时出现有趣现象：标记变成本体
  - 例如[[clash]]中的`for windows`已经变成本体的一部分了，出现了![](../toolbox/linux/clash-for-windows-linux.png)这种
# 版本依赖
## 原因实例
- trivial修改
  - [[moveit-real-robot]]提到的更新时，有个文件名改变，从`panda_control_moveit_rviz.launch`变成`franka_control.launch`，功能不变
  - [[pl-logs]]中提到不同版本默认路径可能是`lightning_logs`或`default`
  - [[franka-ros-interface]]（爱好者自己写的包，不维护了），`.launch`文件中出现多余参数，接口不匹配
## 上层依赖底层
- 常见现象：上层依赖底层
  - 想装新的上层，必须要新的底层
  - 底层太旧，上层就只能旧
- 举例：
  - [[pip]]中提到：本地（非虚拟环境）用的是`python3.6`（太低）导致无法装[[pip]]版本`22`，导致无法装`tensorflow2.9`（“连锁导致”）
    - 想要装该高版本`tensorflow`就必须`python3 -m pip`而不是`pip3`
    - 也就是必须用虚拟环境中的`pip`而不是本地`pip`
  - vscode相关
    - [[remote-ssh]]时，远程[[vscode-extensions]]版本高，本地vscode版本低，可能导致插件用不了。需要更新本地vscode
    - [[launch]] python时，如果`python`版本过低，就用不了版本高的[[vscode-python]]
    - [[moveit-installation]]中，上层moveit等版本更新连带导致需要安装更高版本的[[franka-ros]]才行
      - 原因：其实是trivial的。一些路径修改导致不匹配不兼容
  - [[hand-eye-calibration]]中提到的：如果你opencv版本过低，或[[moveit-real-robot]]版本过低那么只能[[checkout]]到[[hand-eye-calibration]]（上层）的一个旧版本
- 也有可能要求旧底层，底层太新反而不行（如新版有太严的安全限制，太新的功能等）
  - [nitrome games合集](https://archive.org/details/all_nitrome_games)，他的README里提到有的游戏只能用老旧的Flash Player 13才能打开
- “更新[[general-software-technical/upgrade]]导致用不了”：参考[[general-software-technical/upgrade]]
## 推论
- 上层版本越高，需求的底层版本也越高
- 所以在两头确定时，中间可行的版本可能就只有一个范围。不能太高也不能太低
- 比如[[torch-cuda]]中提到硬件太新导致有下界（3090 GPU就不能使用`cuda 10.x`），而[[ubuntu-nvidia-drivers]]太旧又导致有上界
## 无法求解依赖？
- 各级依赖之间往往有许多复杂约束，如果求解器性能不好，可能陷入死局，本来可以解的也变得不能解了（扩展阅读：[[5-constraint-satisfaction]]）
  - 所以有可能人工求解一下，然后确定几个重要节点，以帮助求解器解决
  - 碰到过的例子：`mmaction`（高级）依赖于`sklearn`（低级），`sklearn`依赖于python版本。`pip`自动求解出`sklearn`版本`1.1.1`，结果不行。于是手动在安装`mmaction`之前`pip install sklearn==1.0.2`，之后即可正常安装高层的`mmaction`
- 适当放宽
  - 有些时候原始的库会指定很多版本约束，但实际上能跑的范围比它的要宽，你就可以手动放宽
  - 有些时候适当舍弃部分功能/微调部分代码即可大幅放宽约束，那就自己动动手吧（很多时候无非就是把`deprecated`的去掉而已）
  - 举例
    - `tape_proteins=0.5`这个包要求`pytorch=1.10.2`，这种严格要求甚至在部分显卡型号（参考[[torch-cuda]]）上会导致解出cpu版本的torch，但实际上，根本不一定要是这个版本
      - 所以可以用[[temp-solution]]，[[workaround]]思想，先装cpu torch把`tape_proteins`的检测应付掉，再`pip`装一个gpu的torch（过程中会卸载旧的torch）
    - [[zsh]]相比bash有需要[[escape]] `[`，写成`\[`的特性，但你别忘了bash中直接`\[`也是trivial的转义，还是`[`本身，所以只要把`[`写成`\[`就行
- 可能被已有的东西干扰，在新环境就能很好求解，参考[[torch-cuda]]在非全新conda环境装`torch`可能导致解出cpu版本，重装[[refresh]]可能解决
- 可能直接换个求解器（包管理器）就解决了。比如[[conda-installation]]不行就换成[[pip]]