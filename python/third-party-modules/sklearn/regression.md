- 线性回归，参考[[4-regression]]，[[unary]]
```python
from sklearn import linear_model
model = linear_model.LinearRegression()
X1 = [[1], [2], [3], [4], [5]] # 注：必须是二维数组
X2 = [[1, 10], [2, -10], [3, 10], [4, -10], [5, 0]]
y = [6, 6, 8, 8, 9]
model.fit(X1, y)
print(model.intercept_)
print(model.coef_)
print(model.score(X1, y))
model.fit(X2, y)
print(model.intercept_)
print(model.coef_)
print(model.score(X2, y))
```
- 即使只有一个feature（一元回归），也需要二维数组。通过[[numpy/reshape]]，[[pytorch/misc/reshape]]等可解决
- 注意$R^2$作为metric，不但可用于训练集，还可用于对“测试集”评估！其含义参考[[unary]]
  - 测试时$R^2$可能为负数，参考[[unary]]
- 更多feature可用，分数$R^2$起码不会变差，符合直觉，参考[[multi-ary]]