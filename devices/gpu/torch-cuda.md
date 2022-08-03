- 前置
  - [[ubuntu-nvidia-drivers]]
  - [[pytorch/basics/installation]]
  - 了解[[6-env]]，[[os-shutil]]等
- 基础用法
    - [[pytorch/basics/installation]]时可加入`cudatoolkit`，所以无需额外装cuda，可以直接
```python
import torch
torch.cuda.is_available()
torch.cuda.device_count()
```
- 注：所以`torch`用的cuda版本和`nvcc -V`不一定相同
  - 甚至你`nvcc`这个命令可能都没有
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