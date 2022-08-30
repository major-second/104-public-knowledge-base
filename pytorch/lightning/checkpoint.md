- 前置：[[lightning/basics]], [[log]]（[[log]]里就有checkpoints）
- 参考[官网文档](https://pytorch-lightning.readthedocs.io/en/latest/common/checkpointing.html)
## 使用checkpoint
- 首先根据[[log]]里的路径，指定一个字符串，再用你自己的类`load_from_checkpoint`，下面是官网示例
    - `checkpoint = "./lightning_logs/version_0/checkpoints/epoch=0-step=100.ckpt"`
    - `autoencoder = LitAutoEncoder.load_from_checkpoint(checkpoint, encoder=encoder, decoder=decoder)`
    - 注意：除了第一个参数`checkpoint`（路径），还需要补充所有`LitAutoEncoder`这个类的`__init__`所需要的参数
    - 当然：`<类>.`和`<对象>.`都行
- 然后把这个`LightningModule`里需要`eval`的那部分`eval()`，即可使用。参考[[lightning/basics]]
    - `encoder = autoencoder.encoder`
    - `encoder.eval()`
    - `fake_image_batch = Tensor(4, 28 * 28)`
    - `embeddings = encoder(fake_image_batch)`
- 当然，这样的model也可以继续进`trainer.test`和`trainer.fit`
## 设定何时保存
- 主要[参考](https://pytorch-lightning.readthedocs.io/en/latest/common/checkpointing_intermediate.html)
- 使用的是`ModelCheckpoint`类
  - 例如：定期存，并且保留所有（而不是只取`top_k`）
```python
>>> from pytorch_lightning import Trainer
>>> from pytorch_lightning.callbacks import ModelCheckpoint
>>> checkpoint_callback = ModelCheckpoint(every_n_epochs=<你想要的N>, save_top_k=-1)
>>> trainer = Trainer(callbacks=[checkpoint_callback])
```