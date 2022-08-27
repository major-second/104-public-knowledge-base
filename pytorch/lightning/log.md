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
- log数字的方法
  - 一种是`validation_step, test_step`等`self.log`，然后自动被aggregate
  - 在`on_validation_end, on_test_end`等不能`self.log`，只能`self.logger.experiment.add_scalar`
    - 这就是[[leaky-abstraction]]：抽象使得失去灵活性，所以必须直击底层