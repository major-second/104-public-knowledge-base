- 前置
  - [[models/basics]]
  - [[linear-transform]]
  - [[normalization]]
# internal-covariate-shift
- 前置[[domain-gap#covariate-shift]]
- 此处含义：某层输入的分布不稳定，在变
# 原理
- 是为了保证进激活函数前满足有一定分布，所以一般在线性层（卷积层）后，激活函数前
- batchnorm的原理导致网络在训练时和测试时行为有根本不同，需要`.train()`和`.eval()`
  - 这个可以自动递归进行
  - 比如[[checkpoint]]中测试前`.eval()`一下某个model，就自动递归`.eval()`其attributes
# 步骤
## Standardization
- [[normalization#减去均值]]
- [[normalization#除以标准差]]
## Scale and Drift
# 参数
- parameters本身：$\mu,\sigma$
- affine如果为True，增加[[batchnorm#Scale and Drift]]，否则没有
- [超参数参考](https://blog.csdn.net/weixin_39228381/article/details/107896863)，例如
  - momentum机制
  - 防止[[trivial-mistakes-in-algo#zero division]]的epsilon
# 实操
- 有不同维数的batchnorm
  - `1d`例子：`t = Tensor([[1,2,1], [2,4,0]]); print(nn.BatchNorm1d(3)(t))`
  - 结果
```text
tensor([[-1.0000, -1.0000,  1.0000],
        [ 1.0000,  1.0000, -1.0000]], grad_fn=<NativeBatchNormBackward>)
```
- [参考文档](https://pytorch.org/docs/stable/generated/torch.nn.BatchNorm1d.html)
  - 即对于`1d`，输入tensor可能是2d的`N, C`也可能是3d的`N, C, L`
  - 如果是2d，则对每个channel，对所有`N`做norm
  - 如果是3d，则对每个channel，对所有`N, L`做norm
    - 这里认为不同时刻的分布之间有联系
    - 所以你要是原本的`L`不表示时间维，而是各自的feature，把BatchNorm1d当成了[[1x1conv]]使用，就必须`Flatten()`！
# 其它
- 一个有意思的问题：一般都是线性，bn，激活函数。但对于简单的[[mlp]]，切记最后一层直接线性就行，不要再加bn和激活函数了
  - 否则现象可能是训练不正常，loss无法正常下降，因为结果强行做了batchnorm