前置：
- [[tensor-calculator]]
- 有GPU（才能体会至少有两个不同设备）

对于张量，`.device`就可看到设备在哪，`.to(device)`转换设备
对于model比如`nn.Linear`之类的，看`weight`之类的attribute就知道模型在哪
设备不同的张量进行计算，肯定会报错