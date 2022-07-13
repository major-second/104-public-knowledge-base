前置
- [[optimization]]
- [[tensorboard]]
- `pip install pytorch-lightning`

内容
- [参考](https://www.pytorchlightning.ai/)，里面有一个用MNIST训练auto encoder的例子
- [[dataloader]]不变
- [[model]]改成继承`pl.LightningModule`
  - 回忆：继承`nn.Module`需要重载`__init__()`, `forward()`
  - 现在它的官方示例还继承了`configure_optimizers()`, `training_step()`, `validation_step()`
  - 这里的一个`LightningModule`相比原始`torch.nn.Module`来说更为宏观
    - 例如auto encoder的整个结构，我们称为一个model
    - forward时只需要过encoder，计算loss需要encoder和decoder
    - 如果是原始的pytorch，肯定要把encoder和decoder分开
- 使用
  - 初始化trainer: 例如`trainer = pl.Trainer(gpus=4, precision=16, limit_train_batches=0.5)`，详见[[trainer]]
    - 此处还可以指定`max_epochs`等一系列参数
  - 使用trainer: 例如`trainer.fit(model, train_loader, val_loader)`
  - 参考`example.ipynb`的`basics`节，对比使用lightning和不用的写法
    - 原始代码来自[[optimization]]中提到的`pytorch/basics/minimum.ipynb`
  - [[tensorboard]]需要的信息、checkpoint等都会被自动存到`lightning_logs`文件夹
    - tensorboard会自动记录`train_loss`, `val_loss`等