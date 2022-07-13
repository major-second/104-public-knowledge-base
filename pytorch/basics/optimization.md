前置
- [[model]]
- [[autograd]]
- [[dataloader]]

内容
- [参考](https://docs.microsoft.com/en-us/learn/modules/intro-machine-learning-pytorch/6-optimization)
- 我们有了[[model]]和[[dataloader]]
- 初始化：`optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)`
- 核心三个步骤（注意导数必须清零，参考[[autograd]]）

```python
optimizer.zero_grad()
loss.backward()
optimizer.step()
```
- 这样可以优化模型，之后可以[[save]]成`.pth`文件
- 全过程参考：[The full model building process](https://docs.microsoft.com/en-us/learn/modules/intro-machine-learning-pytorch/8-quickstart), [Summary](https://docs.microsoft.com/en-us/learn/modules/intro-machine-learning-pytorch/9-summary)
- 举例：`minimum.ipynb`