- 前置：[[model]], [[transform]]
- 原理上，是为了保证进激活函数前满足有一定分布，所以一般在线性层（卷积层）后，激活函数前
- batchnorm的原理导致网络在训练时和测试时行为有根本不同，需要`.train()`和`.eval()`
  - 这个可以自动递归进行
  - 比如[[checkpoint]]中测试前`.eval()`一下某个model，就自动递归`.eval()`其attributes
- 实操中有不同维数的batchnorm
  - `1d`例子：`t = Tensor([[1,2,1], [2,4,0]]); print(nn.BatchNorm1d(3)(t))`
  - 结果
```text
tensor([[-1.0000, -1.0000,  1.0000],
        [ 1.0000,  1.0000, -1.0000]], grad_fn=<NativeBatchNormBackward>)
```