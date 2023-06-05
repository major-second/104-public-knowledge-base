# 基础
## `python`语句做准备
tensorboard本来是用于tensorflow的可视化，但也可以用于pytorch
[官方教程](https://pytorch.org/tutorials/recipes/recipes/tensorboard_with_pytorch.html)
python代码中参考这个来写，以存储数据，之后可以终端命令使用或者其它方式使用
```python
import torch
from torch.utils.tensorboard import SummaryWriter
writer = SummaryWriter()
writer.add_scalar("Loss/train", loss, epoch)
writer.flush()
writer.close()
```
## 终端运行命令使用
- 完成`.py`文件中代码书写之后，运行`.py`文件，并
  - **另开一个终端**
  - 到有`eventtf`那些文件的目录
  - `tensorboard --logdir . --port <端口>`
  - 注：如果要远程看，还需要`--bind_all`参数（注意是下划线不是横杠）
- 然后远程看：浏览器输入`<ip>:<端口>`
  - 注：在（云服务器）宿主`B`使用`ssh -L`连接docker容器`C`，把`C`中端口转发（参考[[ssh/ssh]]）到宿主`B`时，本地`A`一般不能直接通过`<宿主Bip>:<端口>`访问`C`的端口。这和docker配置有关
  - 但是可以`A`直接[[docker/ssh]]`C`并使用`ssh -L`转发端口到`A`，参考[[ssh/ssh]]
- 用完即时清空文件，并停下`tensorboard`命令，免得下次用造成混乱
- issue: 如果装了多个版本可能报错duplicate啥的，参考[这个](https://stackoverflow.com/questions/57228487/valueerror-duplicate-plugins-for-name-projector)解决
- vscode集成：`Ctrl + Shift + P`然后`Python: Launch TensorBoard`
  - 可以自动搜索所有子文件夹中的记录，并启动网页
  - 前置：用[[vscode-python]]插件，并右下角先选好有`tensorboard`包的解释器
  - 注：此处如果你版本太低会有[[warning]]，但可以尝试不管
# 网页中的操作
- 右上角设置
  - 可以自动以一定时间间隔reload
  - 可以设置“平滑”程度
- 对于卡片（card）
  - 普通地鼠标拖个框：看框里的
    - 进阶：拖横线/竖线改长宽比，结合`Alt`滚轮实现自如切换scale
  - `Alt`+滚轮：缩放
  - `Alt`+鼠标拖拽：移动
  - 对于每个card，可以考虑pin到上面这样方便对比
- 左侧filter
  - 可以打勾选择看不同的run（用不同颜色表示）
  - 还可以用[[regex]]过滤
  - 两者还能结合使用！
- 鼠标指向线，会高亮
  - 太多线？缩放只留一部分即可