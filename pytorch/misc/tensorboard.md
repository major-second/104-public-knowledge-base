前置：
- todo

tensorboard本来是用于tensorflow的可视化，但也可以用于pytorch
[官方教程](https://pytorch.org/tutorials/recipes/recipes/tensorboard_with_pytorch.html)
代码中参考这个来写
```python
import torch
from torch.utils.tensorboard import SummaryWriter
writer = SummaryWriter()
writer.add_scalar("Loss/train", loss, epoch)
writer.flush()
writer.close()
```
- 完成`.py`文件中代码书写之后，运行`.py`文件，并另开一个终端
  - 到有`eventtf`那些文件的目录
  - `tensorboard --logdir . --port <端口>`
  - 注：如果要远程看，还需要`--bind_all`参数（注意是下划线不是横杠）
- 然后远程看：浏览器输入`<ip>:<端口>`
  - 注：在（云服务器）宿主`B`使用`ssh -L`连接docker容器`C`，把`C`中端口转发[[forward-port]]到宿主`B`时，本地`A`一般不能直接通过`<宿主Bip>:<端口>`访问`C`的端口。这和docker配置有关
  - 但是可以`A`直接[[ssh连接docker容器]]`C`并使用`ssh -L`转发端口到`A`
- 用完即时清空文件，并停下`tensorboard`命令，免得下次用造成混乱
- issue: 如果装了多个版本可能报错duplicate啥的，参考[这个](https://stackoverflow.com/questions/57228487/valueerror-duplicate-plugins-for-name-projector)解决
- #vscode 集成：`Ctrl + Shift + P`然后`Python: Launch TensorBoard`
  - 可以自动搜索所有子文件夹中的记录，并启动网页
  - 前置：用vscode [[python]]插件，右下角先选好有`tensorboard`包的环境
  - 而且如果你版本不对，vscode还会自动给你装新版
- 网页中操作
  - 可以自动以一定时间间隔reload
  - `Alt`+滚轮缩放，`Alt`+拖拽移动
  - 普通拖个框：看框里的