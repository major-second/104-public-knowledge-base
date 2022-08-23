## 前置
- [[dataset]]

> While training a model, we typically want to pass samples in "minibatches", reshuffle the data at every epoch to reduce model overfitting, and use Python's multiprocessing to speed up data retrieval.

## 获得
- `from torch.utils.data import DataLoader`
- `train_dataloader = DataLoader(training_data, batch_size=4, shuffle=True)`
## 使用
- `for i in train_dataloader`
  - `Dataloader`对象是iterable，但不是iterator，参考[[iterable-iterator]]
- 当然也可以`next(iter(train_dataloader))`（转换成iterator）
- 得到结果的第0维是batch_size，后面大小该是啥就是啥
  - 例如`Dataset`中$x_i$大小是`[2,3,4]`，batch size是32，那么此时取出的$x_i$大小就是`[32,2,3,4]`（即32条$x_i$）
- `num_workers`参数：[参考](https://blog.csdn.net/qq_24407657/article/details/103992170)，一般是自己电脑CPU核心数
  - [[resource-management/commands]]可以看核心数