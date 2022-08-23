前置：
- [[tensor-calculator]]
- [[device]]（如果需要GPU）

[参考](https://docs.microsoft.com/en-us/learn/modules/intro-machine-learning-pytorch/4-model)
- `from torch import nn`，然后`nn.<类名>(参数)`来造模型
  - 如无参数的`nn.Flatten()`，`nn.ReLU()`
  - 输入简单参数的`nn.Linear(<in>, <out>)`
  - 拼接模块的`nn.Sequential(<直接逗号隔开输入若干个模块>)`
    - 可下标取出子模块，比如`m[0].weight`这种
- 每个模块（module）至少要重载两个函数
  - `__init__`：定义要用哪些“组件”。常见模式`self.flatten = nn.Flatten()`
  - `forward`：定义怎么使用组件计算。常见模式`output = self.<变量名>(input)`
    - 调用时直接`model(data)`即可，不需要`.forward()`
    - 注：很多时候调试时我们都把断点打到`forward`函数第一行，并打开[[launch]]中提到的`justMyCode`，这样效率很高，一下就定位到模型的核心之处
- 注意默认第0维是batch，所以`nn.Softmax()`需要`dim=1`才正确
  - 相比之下，`Linear`默认直接就这么搞了，不需要指定`dim=1`
  - `nn.Flatten`和`flatten`也因此默认不同。前者默认`start_dim=1`，后者默认为`0`
- 参数
  - 自动递归地track
  - `.parameters()`，`.named_parameters()`，可迭代
  - 命名也是自动的。可以自己`print`那些`named_parameters()`中的元素试试