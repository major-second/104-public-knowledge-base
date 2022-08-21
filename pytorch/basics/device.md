前置
- [[tensor-calculator]]
- 有GPU（才能体会至少有两个不同设备，CPU和GPU）
  - 此时也参考[[torch-cuda]]

内容
- 常见做法：`device = 'cuda' if torch.cuda.is_available() else 'cpu'`，之后使用`device`变量
- 对于张量
  - `.to(device)`转换设备
  - `.cuda()`直接转换到GPU，`()`里可以写数字编号也可以不写
  - `.device`可看到设备在哪（参考[[tensor-calculator]]）
- 对于model（继承`Module`）
  - 也可以`.to(device)`转换设备
  - 看`weight`之类的attribute，找其中tensor的`.device`就知道模型是否在GPU
- 设备不同的两个张量进行计算，肯定会报错