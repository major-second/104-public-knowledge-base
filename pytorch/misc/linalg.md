- 前置[[tensor-calculator]]
- 2范数：`torch.linalg.norm`
  - 请特别注意是否平方了！也就是，`norm`结果直接加没有什么意义，应该先平方再相加再开方才能得到有意义的东西
- 最小二乘法线性回归：`torch.linalg.lstsq(x, y)`，用`.solution`取出系数
  - 参考[[4-regression]]
  - 当神经网络输出的最后一层是linear，则可以考虑直接用（最后一层的feature）最小二乘而不是训出来
  - 可以防止一些额外误差，参考[[deep-learning/optimization]]
  - 联系[[lightning/basics]]，就知道怎么训练和验证
    - 训练照常
    - `eval`（`val`或`test`）时
      - `coef = torch.linalg.lstsq(train_h, train_y).solution`
      - `intercept = (train_y - train_h @ coef).mean()`
      - `res = val_h @ coef + intercept - val_y`
      - 得到残差，然后可计算残差平方和等
        - **中过的坑：计算$R^2$**，可能会有$\mathbb E(\frac{a}{b}) \ne \frac{\mathbb E a}{\mathbb E b}$问题。所以不要每次`val_batch`计算一个再平均
    - 注意
      - 千万别用`val_h, val_y`做线性回归，否则就information leak了
      - 思想上是刚刚的几句
        - 但实际上如果你使用`pytorch_lightning`，不应该把它们都写到`validation_step`
        - 而应当在`on_validation_start`这个[[pl-hook]]处计算斜率截距，之后不再重复计算
      - 和[[regression]]计算结果可能稍有差距
- 注：想要bias比较麻烦，需要参考[[multi-ary]]手动操作
```python
X = torch.tensor([[1, 2], [3, 4], [5, 6]])
y = torch.tensor([[7], [8], [9]])
X_bias = torch.cat((X, torch.ones((X.shape[0], 1))), dim=1)
weights, *_ = torch.linalg.lstsq(y, X_bias)
print(f'Weights: {weights[:-1]}')
print(f'Bias: {weights[-1]}')
```
- 无论何种结果得到weight和bias，都可以考虑手动赋值给线性层[[model]]的`weight, bias`属性。即`m.weight = nn.Parameter(weight.reshape(m.weight.shape))`这样