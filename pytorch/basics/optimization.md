前置
- [[model]]
- [[autograd]]
- [[dataloader]]

内容
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