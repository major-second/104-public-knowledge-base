# 前置
- [[ubuntu-nvidia-drivers]]
- 了解[[6-env]]，[[os-shutil]]等
# 基础讲解
- 如何得到能用cuda的torch并验证
  - 此处不用前置手动安装CUDA！
    - 原因：看[官网](https://pytorch.org/get-started/locally/)，`conda`和`pip`安装`torch`的命令都有直接可装的`cudatoolkit`，这就包含了CUDA
    - 参考[[pytorch/basics/installation]]
  - 如果安装成功，就可以直接用以下语句验证
    - `import torch; print(torch.cuda.is_available()); print(torch.cuda.device_count())`
- 安装torch时同时安装的`cudatoolkit`和其他地方的`cuda`的关系
  - `torch`用的cuda版本和`nvcc -V`，`nvidia-smi`等看到的版本都不一定要相同
  - 甚至你成功能用`torch`的gpu版本了，连`nvcc`这个命令可能都没有
    - `torch`用的是自己集成的`cudatoolkit`而不需要`nvcc`
  - `nvidia-smi`显示的版本是（一般）你能用的cuda版本上限
- 兼容性问题
  - 首先新GPU不能使用老cuda，老torch
    - 如3090不能用cuda10.x
    - 如A100架构是`sm_80`，非常高，没法用版本低的`torch`
    - 否则可能
      - `torch.cuda.is_available()`是`True`
      - 但是尝试随便搞些张量`.cuda()`，加加减减运算，跑起来
      - 就报`RuntimeError: NCCL error in: /pytorch/torch/lib/c10d/ProcessGroupNCCL.cpp:38, unhandled cuda error, NCCL version 2.7.8`，或者架构`sm_??`不匹配这种东西
    - [参考](https://www.jianshu.com/p/978bc51029fa)
  - 其次[[ubuntu-nvidia-drivers]]中`nvidia-smi`显示的版本（一般）是你能用的cuda版本上限，[参考](https://www.jianshu.com/p/eb5335708f2a)，[具体参考nvidia官网文档](https://docs.nvidia.com/deploy/cuda-compatibility/index.html#cuda-intro)
  - 再次，新创立的环境是最保险的
    - 已经装了其它东西的环境可能会干扰[[dependencies]]的求解，导致解出cpu版本的torch（在conda安装确认的界面能看到是否准备装cpu版本的）
    - 有时用[[pip]]和[[find-grep]]结合，`pip list | grep torch`，然后把能看到的torch版本全部卸载，即可正常重装。这就是一个[[refresh]]的例子
  - 这些兼容性问题除了你直接安装引起，还有可能是上层包指定的版本依赖引起的，参考[[version]]中`tape_proteins`的例子
- 一个坑：[[non-standard]]的[[channel]]里可能缺少一些版本，导致只能给你cpu版本的
# 改环境变量，指定用卡
## `.py`中改
- 必须在access相关东西之前，就改[[6-env]]环境变量才行
  - 具体地
    - 刚刚你验证是否安装成功时，跑了`import torch; print(torch.cuda.is_available()); print(torch.cuda.device_count())`
    - 如果这是个交互式窗口，那么再在这里改环境变量也没用了！
  - 重开一个，发现就行了，参考以下效果
```python
import os
os.environ['CUDA_VISIBLE_DEVICES'] = ''
torch.cuda.device_count() # 输出0
```
- 编号从0开始。比如8卡机器，`'4,5,6,7'`就是后面四张卡
## `.sh`中改
- 直接`CUDA_VISIBLE_DEVICES=0 python ...`即可，参考[[6-env]]
# 其它
- 清除不用的显存`torch.cuda.empty_cache()`（较高[[version]]才有）
  - 在你使用[[jupyter-notebook/basics]]时经常需要。否则显存会爆
  - 注意对于模型的输出结果，有时需要`tensor.data`，否则梯度会一直被存着占地方（即使已经没有变量引用它了）
- 具体怎么在torch中使用GPU参考[[device]]