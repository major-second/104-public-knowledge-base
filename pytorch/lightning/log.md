- 参考[官方文档](https://pytorch-lightning.readthedocs.io/en/stable/extensions/logging.html)
  - 默认使用`TensorBoardLogger`类
  - 默认路径是`lightning_logs`文件夹
  - 里面有[[tensorboard]]需要的信息、[[checkpoint]]等
- 自己定制文件夹：例子
```python
from pytorch_lightning import loggers as pl_loggers
tb_logger = pl_loggers.TensorBoardLogger(save_dir="logs/")
trainer = Trainer(logger=tb_logger)
```