# 一元
- 某个像素/通道自己的重要性是多少
- 例如
  - 对通道[SE](https://blog.csdn.net/niuxuerui11/article/details/120403318)
  - 对通道+对像素[CBAM](https://blog.csdn.net/Roaddd/article/details/114646354)
  - 实现上，往往都是张量整体乘以某个（更低维的）张量，并自动broadcast
  - 与[[resnet]]比较：一个是乘，一个是加，但都是对于原始数据的某种“调整”而不是直接取代数据！
  - 实操：例如 [torch的SE](https://pytorch.org/vision/stable/generated/torchvision.ops.SqueezeExcitation.html)
# 二元
- 成对的，两两之间重要性多少
- [[transformer]]是其中非常有名的应用