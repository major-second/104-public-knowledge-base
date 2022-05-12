前置：
- [[ubuntu-nvidia-drivers]]
- [[pytorch/installation]]
- 了解[[6-env]]，[[os]]

[[pytorch/installation]]时自动加入`cudatoolkit`，所以可以直接
```python
import torch
torch.cuda.is_available()
torch.cuda.device_count()
```
尝试改环境变量，指定用卡
（必须重开！必须在access相关东西之前就改环境变量才行。刚刚跑过那几条的`python`交互式窗口不行！）
```python
import os
os.environ['CUDA_VISIBLE_DEVICES'] = ''
torch.cuda.device_count() # 输出0
```