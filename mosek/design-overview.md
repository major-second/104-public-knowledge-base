- 前置[[python-installation]]
- https://docs.mosek.com/latest/pythonfusion/design.html
> fast and clean prototyping of conic problems without suffering excessive performance degradation
- 注意这里文档并不是一个马上能跑的例子（参考[[read-doc]]）
# 原文
```python
    x = M.variable(n)
    gamma = M.variable()
    alpha = M.parameter()

    M.objective(ObjectiveSense.Maximize, Expr.sub(Expr.dot(mu, x), Expr.mul(alpha, gamma)))

    M.constraint(Expr.sub(Expr.sum(x), w), Domain.equalsTo(0.0))
    M.constraint(Expr.vstack(gamma, Expr.mul(G.transpose(), x)), Domain.inQCone())
    M.constraint(x, Domain.greaterThan(0.0))
```
# 补全后能跑最小示例
```python
import mosek
from mosek.fusion import *

n = 10 # number of variables
mu = [0.5] * n # expected return vector
G = Matrix.dense(n,n,[1.0] * (n*n)) # covariance matrix
w = 1.0 # budget constraint

with Model("portfolio") as M:
    x = M.variable(n) # portfolio weights
    gamma = M.variable() # risk measure
    alpha = M.parameter() # risk aversion parameter

    M.objective(ObjectiveSense.Maximize, Expr.sub(Expr.dot(mu, x), Expr.mul(alpha, gamma))) # maximize return minus risk

    M.constraint(Expr.sub(Expr.sum(x), w), Domain.equalsTo(0.0)) # budget constraint
    M.constraint(Expr.vstack(gamma, Expr.mul(G.transpose(), x)), Domain.inQCone()) # quadratic cone constraint for risk measure
    M.constraint(x, Domain.greaterThan(0.0)) # non-negativity constraint

    alpha.setValue(2.0) # set risk aversion parameter value

    M.solve() # solve the problem

    print("Optimal portfolio weights:")
    print(x.level())
```
- 注意点
  - 参考[[ast]]写数学表达式
  - 常见结构
    - 密矩阵`Matrix.dense(<list>)`
    - 向量直接`list`