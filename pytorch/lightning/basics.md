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
    - 具体找`lib\python3.7\site-packages\pytorch_lightning\overrides\base.py`，看到以下代码，就知道这些方法分别在何时被调用
    - ![](lightning-module-methods.png)
  - 这里的一个`LightningModule`相比原始`torch.nn.Module`来说更为宏观
    - 例如auto encoder的整个结构，我们称为一个model
    - forward时只需要过encoder，计算loss需要encoder和decoder
    - 如果是原始的pytorch，肯定要把encoder和decoder分开
- 使用
  - 初始化trainer: 例如官网给出的`trainer = pl.Trainer(gpus=4, precision=16, limit_train_batches=0.5)`，详见[[trainer]]
    - 此处还可以指定`max_epochs`等一系列参数
    - 例如`accelerator='gpu', devices=[0,1]`使用0，1两张卡
    - 当然现在有时多卡还是会有未知麻烦，莫名其妙报错。直接`devices=[0]`比较保险吧！参考[[alternative-method]]
  - 使用trainer拟合（训练）: 例如`trainer.fit(model, train_loader, val_loader)`
  - 测试：[参考](https://pytorch-lightning.readthedocs.io/en/latest/common/evaluation_basic.html#add-a-test-loop)，例如`trainer.test(model, test_loader)`
    - 当然，相应的你的`LightningModule`也需要重载`test_step()`
  - 参考`example.ipynb`的`basics`节，对比使用lightning和不用的写法
    - 原始代码来自[[optimization]]中提到的`pytorch/basics/minimum.ipynb`
  - 存、取、用checkpoint参考[[checkpoint]]