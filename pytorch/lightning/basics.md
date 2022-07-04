前置
- [[optimization]]
- `pip install pytorch-lightning`

内容
- [参考](https://www.pytorchlightning.ai/)
- [[dataloader]]不变
- [[model]]改成继承`pl.LightningModule`
  - 回忆：继承`nn.Module`需要重载`__init__()`, `forward()`
  - 现在它的官方示例还继承了`configure_optimizers()`, `training_step()`, `validation_step()`
- 使用
  - `trainer = pl.Trainer(gpus=4, precision=16, limit_train_batches=0.5)`，详见[[trainer]]
  - `trainer.fit(model, train_loader, val_loader)`