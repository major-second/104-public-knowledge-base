## 前置
- [[dataset]]

> While training a model, we typically want to pass samples in "minibatches", reshuffle the data at every epoch to reduce model overfitting, and use Python's multiprocessing to speed up data retrieval.

## 获得
- `from torch.utils.data import DataLoader`
- `train_dataloader = DataLoader(training_data, batch_size=4, shuffle=True)`
- 常用参数
  - `num_workers`参数：[参考](https://blog.csdn.net/qq_24407657/article/details/103992170)，一般是自己电脑CPU核心数，决定并行程度
    - [[resource-management/commands]]可以看核心数
  - `shuffle`：如果不设定`True`，就每次依次读入的顺序相同
    - 训练时如果这样可能导致过拟合
  - `pin_memory`：内存足够时空间换时间
## 使用
- 可以`for i in train_dataloader`，每次取出一个`batch`
  - `Dataloader`对象是iterable，但不是iterator，参考[[iterable-iterator]]
  - 实际中很多时候可以`for x, y in train_dataloader`，自动拆包
- 当然也可以`next(iter(train_dataloader))`
  - 即先转换成iterator，就可以`next`
- 得到结果的第0维（一般）是batch_size（但不能整除时最后一个可能不是），后面大小该是啥就是啥
  - 例如`Dataset`中$x_i$大小是`[2,3,4]`，batch size是32，那么此时取出的$x_i$大小（一般）就是`[32,2,3,4]`（即32条$x_i$）