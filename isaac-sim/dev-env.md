---
title: isaac sim的开发环境
type: tools
---

[toc]
# isaac sim的开发环境
前置：
- [[isaac-sim/basics]]
- [[anaconda]]
- 只能用bash，不能用[[zsh]]，否则会观察到环境变量导入得不对（跟源码处一些`BASH`字样看起来显然有关）

Linux version 5.4.0-84-generic (buildd@lcy01-amd64-007) (gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1~18.04))
有 #时效性 。随着Isaac更新，一些细节可能会发生变化
本篇体验 #isaac-sim 是使用GPU加速的先进的 #模拟器 ，方便做 #机器人 任务和 #RL .
配置和isaac sim相关的 #python #vscode #anaconda 环境，之后即可方便写、调试python脚本
## python环境
[python环境](https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/install_python.html)
- 注： #时效性
  - 上面链接其中说的“安装目录”（Isaac Sim root folder），默认为`~/.local/share/ov/pkg/isaac_sim-2021.2.1`，不同版本当然不同
  - 安装目录和`python.sh`的相对目录关系不同版本当然也可能不同
  - 并且具有`setup某某.sh`功能的脚本的路径和文件名都会不同
  - 所以更新isaac可能要更新`~/.bashrc`
## vscode环境
[vscode环境](https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/install_python.html#visual-studio-code-support)
- 在刚刚说的“安装目录”下尝试`ls .vscode`，应该是能看到一些配置文件的。直接vscode打开安装目录，就能用上它们
- 为了打开隐藏文件夹（`.`开头），需要在vscode打开文件夹的界面右键，选择显示隐藏文件![](dev-env/vscode-hidden.png)
- 为了使用`(Linux) isaac-sim`，在vscode中需要安装`C/C++ Extension Pack`，vscode才能识别`launch.json`中的`cppdbg`
  - 然而目前，这样打开还不能识别assets，说明仍不成熟。还是老老实实launcher启动（参考[[installation]]）吧
## anaconda环境
[anaconda环境](https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/install_python.html#advanced-running-with-anaconda)
- 仍然来到“安装目录”，然后按官网指示输入命令，创建`conda`环境（当然，可以先`conda env list`确认没有已经名为`isaac-sim`的环境）
可以输入一次以下命令，从这之后就可以`isaac-sim-py`这条命令**一键“作准备”**（类似于其它环境的`conda activate <环境名>`）
```sh
cd ~/.local/share/ov/pkg/isaac_sim-2021.2.1; \
conda env create -f environment.yml; \
conda activate isaac-sim; \
echo "
# alias for isaac-sim env
alias isaac-sim-py='\
conda activate isaac-sim; \
source ~/.local/share/ov/pkg/isaac_sim-2021.2.1/setup_conda_env.sh'
" >> ~/.bashrc; \
. ~/.bashrc
```
- 特别注意文件名是`setup_conda_env.sh`不是`setup_python_env.sh`（我被坑了一次）
- 如果没权限，参考[[7-permissions]]给权限
- 看脚本源码，`setup_conda_env.sh`脚本里定义了很多环境变量。所以`echo $<变量名>`可以看出成功了没有
  - 所以说如果反复运行`isaac-sim-py`可能导致`$PYTHONPATH`巨长，导致一些问题（比如`python`命令执行不了）
  - 即：反复运行没有 #幂等性
- 只要成功启动并配置`conda`环境，就可以用`python`而非`python.sh`来启动`python`脚本
  - 验证：交互式`python`环境中可以`import omni.isaac.kit`
  - 且输入`omni.isaac.kit`，可输出其所在路径，验证看是否正常
- 搞完基础conda环境之后，可以再装其它包，直接和普通的装包操作相同即可，参见[[anaconda]]