# 前置
- [[model]]
- [[autograd]]
- [[dataloader]]
# 内容
- [参考](https://docs.microsoft.com/en-us/learn/modules/intro-machine-learning-pytorch/6-optimization)
- 我们有了[[model]]和[[dataloader]]
- 初始化：`optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)`
- 核心三个步骤
  - 注意旧导数必须清零，参考[[autograd]]
  - 注意在执行这三步之前当然要先计算出`loss`（是标量）
  - 常见模式
    - 在初始化时，`loss_fn = nn.<类名>()`
    - 之后每次，`loss = loss_fn(inputs)`
    - 参考`minimum.ipynb`

```python
optimizer.zero_grad() # 清零旧导数
loss.backward() # 记录新导数
optimizer.step() # 使用新导数进行一步优化
```
- 这样可以优化模型，之后可以[[save]]成`.pth`文件
- 全过程参考：[The full model building process](https://docs.microsoft.com/en-us/learn/modules/intro-machine-learning-pytorch/8-quickstart), [Summary](https://docs.microsoft.com/en-us/learn/modules/intro-machine-learning-pytorch/9-summary)
- 举例：`minimum.ipynb`
# 如何选用
- Adaptive optimizer可以防止梯度爆炸导致[[nan]]问题等。相比之下，`SGD`容易出现[[nan]]问题
  - 解决方法[参考](https://stackoverflow.com/questions/65654279/nan-values-with-sgd-optimizer-in-keras-for-regression-nn#:~:text=The%20NaNs%20in%20the%20loss%20function%20is%20mostly,long%20as%20you%20don%27t%20have%20a%20specific%20reason.)
  - 比如正则化、normalize输入值（参考[[feature-engineering]]和[[normalization]]）、加大batchsize等方法
- 但会引入额外误差，比如`minimum.ipynb`中特别简单的玩具问题（线性函数），`Adam`会带来很大的额外误差