- 前置
  - [[dataset]]
- [参考](https://blog.csdn.net/qq_43391414/article/details/120462055)
  - [[warning]]有助于理解其中所说“在此处避免报错没用”
  - 但是有时我们确实需要避免报错。比如每个data instance携带有一些变长的，不过神经网络的数据时
- 有时不想改这个，又想让它临时不报错的丑陋解决方案
  - 手动[[manipulation]]中，`torch.cat`适当的全0张量（即手动padding）
  - 或调包padding，如`torch.nn.utils.rnn.pad_sequence`，输入张量列表。注意结果可能需要转置`.transpose(0, 1)`这种