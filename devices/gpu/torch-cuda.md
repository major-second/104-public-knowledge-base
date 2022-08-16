- 前置
  - [[ubuntu-nvidia-drivers]]
  - [[pytorch/basics/installation]]
  - 了解[[6-env]]，[[os-shutil]]等
- 基础用法
    - [[pytorch/basics/installation]]时可加入`cudatoolkit`，所以无需额外装cuda，就可以直接
```python
import torch
torch.cuda.is_available()
torch.cuda.device_count()
```
- 注：所以`torch`用的cuda版本和`nvcc -V`，`nvidia-smi`等看到的版本都不一定相同
  - 甚至你`nvcc`这个命令可能都没有
  - 也就是，`cudatoolkit=<版本>`不一定要符合你`nvidia-smi`看到的cuda版本，只需要小于等于它即可，[参考](https://www.jianshu.com/p/eb5335708f2a)
  - 当然，也有其它的兼容性问题，例如较新的3090 GPU就不能使用`cuda 10.x`
# 改环境变量，指定用卡
- 必须在access相关东西之前，就改环境变量才行
  - 具体地：刚刚跑过那几条的`python`交互式窗口不行！
  - 重开一个，发现就行了
```python
import os
os.environ['CUDA_VISIBLE_DEVICES'] = ''
torch.cuda.device_count() # 输出0
```
- 编号从0开始，比如8卡机器，`'4,5,6,7'`就是后面四张卡
# 其它
- 清除不用的显存`torch.cuda.empty_cache()`