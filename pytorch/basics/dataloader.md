前置：
- [[dataset]]

> While training a model, we typically want to pass samples in "minibatches", reshuffle the data at every epoch to reduce model overfitting, and use Python's multiprocessing to speed up data retrieval.

- 获得
  - `from torch.utils.data import DataLoader`
  - `train_dataloader = DataLoader(training_data, batch_size=4, shuffle=True)`
- 使用
  - `for i in train_dataloader`
    - `Dataloader`对象是iterable，但不是iterator，参考[[iterable-iterator]]
  - 当然也可以`next(iter(train_dataloader))`（转换成iterator）
  - 第0维是batch_size，后面大小该是啥就是啥（对应`Dataset`对象的大小）