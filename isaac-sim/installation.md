---
title: isaac sim主体安装
type: tools
---

[toc]
# isaac sim主体安装
前置：
- 有 #NVIDIA #GPU 和驱动
- 有NVIDIA账号
- 良好的网络环境（如果中国大陆可能需要[[linux翻墙]]）

==本篇撰写时间为2021.11.20
Linux version 5.4.0-84-generic (buildd@lcy01-amd64-007) (gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1~18.04))
有 #时效性 。随着Isaac更新，一些细节可能会发生变化==
本篇安装 #isaac-sim 是使用GPU加速的先进的 #模拟器 ，方便做 #机器人 任务和 #RL .
本篇没有加上sample assets. 下一篇加。
## 确认满足需求
https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/requirements.html
确认硬件和驱动要求（注：`nvidia-smi`查看显卡相关信息）
太老的显卡装不了。配置不够装不了（很多笔记本都不行）。对Ubuntu系统版本也有要求。
注意：==2021.11.20==推荐驱动版本460倒并不是必须的。至少我用470版本可以装。
这里**官方教程的“栈深度”有点深**（为了装Isaac要装Nucleus，进而要先装Launcher，然后装Launcher又要登录，登录又要邮箱确认……）容易把配环境的人劝退……
### 11.28更新
Isaac现已从之前本文描述的2021.1.1更新至2021.2.0版本。之前本文的许多链接和文字将在新版本失效。
官方文档也更新了。非常令人高兴的是**栈不再那么深**了。
下面这个是最新的有关install的有效链接。
https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/install_basic.html
已经装了旧版本的可以在下图这里升级。
![](installation/update-isaac.png)
2021.2.0推荐的驱动版本是470
注：上图"Settings"处还有卸载按钮
![](installation/uninstall.png)
### 2022.1.14更新
现在已经有2021.2.1了
## Omniverse Launcher安装
- https://www.nvidia.com/en-us/omniverse/
    - 点击![](installation/download-omniverse.png)
    - 出来问卷，简单填一下。
    - 点击下图的Download here for `Linux`
  ![](installation/download-omniverse-linux.png)
- 下载到`.AppImage`
![](installation/appimage.png)
    - 在其所在文件夹打开终端，`chmod a+x omniverse`然后`Tab`补全，回车，赋予其运行权限。
    - 双击它打开
    - 登录NVIDIA账号（如果是新装的电脑，对以前登录过的账号，可能有Security Challenge，需要邮箱验证。注意在邮箱中查看骚扰邮件和垃圾邮件避免错过）![](installation/login-security.png)
    - 登录之后同意一个协议（需要下拉才能按continue）![](installation/agreement.png)
    - 之后一路continue
### 2022.1.14更新
 omniverse launcher下载页面的beta字样现在已经没了
 现在安装launcher时会默认“捆绑”上CACHE了。我们需要这个捆绑，否则等下手动安装也行
## Launcher中安装组件
- 到EXCHANGE选项卡，安装CACHE
![](installation/install-cache.png)
注：这些安装的prepare过程有时挺久的，视网络情况而定。需要耐心。多试几次吧。
注：本节三个组件可以**一起按安装，让它排队**。这么做有个关键好处：“趁着现在网络状态好赶紧全搞定”。
![](installation/downloading.png)
- 到NUCLEUS选项卡，按
https://docs.omniverse.nvidia.com/prod_nucleus/prod_nucleus/installation/workstation.html#installing-using-omniverse-launcher
安装NUCLEUS.
（过程中需要注册一个管理账号。请记住）
验证安装成功：按官网的做法即可。例如访问
http://localhost:8080/
并用账号密码都为admin登录。
- 到EXCHANGE选项卡，安装ISAAC SIM
安装结果
![](installation/installation-result.png)
此时可以launch isaac，但是缺assets
### 2022.1.8更新
新的安装nucleus教程链接
https://docs.omniverse.nvidia.com/prod_nucleus/prod_nucleus/workstation/installation.html
## 自我总结问答
0. Q: AppImage和Docker Image有什么异同？
A: 核心思想都是独立成体系和外界隔离。对外界“不敏感”，副作用小。
AppImage实际上更像docker的“容器”概念