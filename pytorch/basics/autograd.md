前置
- [[tensor-calculator]]

内容
- 上回讲到前向传播，这次说反向传播
- [参考微软教程](https://docs.microsoft.com/en-us/learn/modules/intro-machine-learning-pytorch/5-autograd)，说得很清楚
- 注意张量需要加关键字参数`requires_grad=True`，或者in-place进行`a.requires_grad_(True)`
  - 否则：`a=torch.randn(3,1); b=torch.randn(1,3); c=b@a; c.backward()`报错`RuntimeError: element 0 of tensors does not require grad and does not have a grad_fn`
- 最简单示例：`a=torch.tensor([[1.,2]], requires_grad=True); b=torch.tensor([[3.],[4]], requires_grad=True); c=a*a*a@b; c.backward(); print(a.grad)`
  - 输出`tensor([[ 9., 48.]])`
  - 形状是`a`的形状
  - 其中$9= 3x^2|_{x=1}*3, 48 = 3x^2|_{x=2}*4$
- 计算图和导数
  - 计算图中只能获得叶子节点的导数
  - 且默认如果没有`retain_graph=True`，则对一张图只能获取一次导数
    - `a=torch.tensor([[1.,2]], requires_grad=True); b=torch.tensor([[3.],[4]], requires_grad=True); c=a*a*a@b; c.backward(); c.backward(); print(a.grad)`不行
  - pytorch是动态图，每次`backward()`会新建计算图。所以运行过程中可以改变图
  - 更深入理解上面两点：虽然一张图一次导数，但可以多张图。可以多次调用`.backward()`
    - `a=torch.tensor([[1.,2]], requires_grad=True); b=torch.tensor([[3.],[4]], requires_grad=True); c=a*a*a@b; c.backward(); c=a*a*a@b; c.backward(); print(a.grad)`就会**积累**2次导数，得到结果`tensor([[18., 96.]])`
    - 如果需要清零，需要`optimizer.zero_grad()`
      - 在这节课你还不会[[optimization]]就急着想清零？可以`a.grad.zero_()`
- 如果只需正向[[tensor-calculator]]无需反向，可以在`with torch.no_grad():`辖域内写代码
  - 有时用于冻结网络的一部分
  - 有时用于验证、测试时加快运行速度
- 注：直接重载`.backward()`没用，[参考](https://cloud.tencent.com/developer/article/1134257)