对于张量（参考[[tensor-calculator]]），`.device`就可看到设备在哪，`.to(device)`转换设备
对于model比如`nn.Linear`之类的，看`weight`之类的attribute就知道模型在哪
设备不同肯定会报错