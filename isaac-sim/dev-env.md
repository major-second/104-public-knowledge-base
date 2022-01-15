---
title: isaac sim的开发环境
type: tools
---

[toc]
# isaac sim的开发环境
前置：
- [[isaac-sim/basics]]
- [[anaconda]]

==本篇撰写时间为2021.11.23
Linux version 5.4.0-84-generic (buildd@lcy01-amd64-007) (gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1~18.04))
有 #时效性 。随着Isaac更新，一些细节可能会发生变化==
本篇体验 #isaac-sim 是使用GPU加速的先进的 #模拟器 ，方便做 #机器人 任务和 #RL .
配置和isaac sim相关的 #python #vscode #anaconda 环境，之后即可方便写、调试python脚本
- [python环境](https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/install_python.html)
    - 注： #时效性 其中说的“安装目录”（Isaac Sim root folder），默认为`~/.local/share/ov/pkg/isaac_sim-2021.2.1`，不同版本当然不同。安装目录和`python.sh`的相对关系不同版本当然也可能不同。
- [vscode环境](https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/install_python.html#visual-studio-code-support)
    - 在刚刚说的“安装目录”下尝试`ls .vscode`，应该是能看到一些配置文件的。所以直接vscode打开安装目录就好
    - 为了打开隐藏文件夹（`.`开头），需要在vscode打开文件夹的界面右键，选择显示隐藏文件![](dev-env/vscode-hidden.png)
- [anaconda配置python环境](https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/install_python.html#advanced-running-with-anaconda)