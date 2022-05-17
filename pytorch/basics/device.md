前置：
- [[tensor-calculator]]
- 有GPU（才能体会至少有两个不同设备）

- 常见做法：`device = 'cuda' if torch.cuda.is_available() else 'cpu'`，之后使用`device`变量。参考[[torch-cuda]]
- 对于张量，`.to(device)`转换设备
  - `.device`就可看到设备在哪
- 对于model（继承`Module`），也可以`.to(device)`转换设备
  - 看`weight`之类的attribute就知道模型在哪
- 设备不同的两个张量进行计算，肯定会报错