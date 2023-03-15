- 前置
  - [[3-3-3-markowitz]]
  - [[design-overview]]用来看例程
- 参考
  - https://docs.mosek.com/9.3/pythonfusion/case-studies-portfolio.html#
- 基本遵从[[3-3-3-markowitz]]解说，加了一些细节
  - 是否能做空决定是否有$x_j\ge 0$约束
  - [[cholesky]]分解是写成[[3-2-conic-quadratic-modeling]]的一种选择，但不唯一，别的可能更快
- conic是quadratic[[general-principles/special-case]]，所以更快更稳定更多优点，现在既然能conic就conic
  - 比如数值稳定性，用标准差而非二次scale的[[cov]]等等
## 例程
```python
def BasicMarkowitz(n,mu,GT,x0,w,gamma):
    
    with  Model("Basic Markowitz") as M:

        # Redirect log output from the solver to stdout for debugging. 
        # if uncommented.
        # M.setLogHandler(sys.stdout) 
        
        # Defines the variables (holdings). Shortselling is not allowed.
        x = M.variable("x", n, Domain.greaterThan(0.0))
        
        #  Maximize expected return
        M.objective('obj', ObjectiveSense.Maximize, Expr.dot(mu,x))
        
        # The amount invested  must be identical to initial wealth
        M.constraint('budget', Expr.sum(x), Domain.equalsTo(w+sum(x0)))
        
        # Imposes a bound on the risk
        M.constraint('risk', Expr.vstack( gamma,Expr.mul(GT,x)), Domain.inQCone())

        # Solves the model.
        M.solve()

        return np.dot(mu,x.level())
```
- 注意`risk`那行
  - 用`Expr.vstack`得到$(\gamma, G^T x)$
  - 回顾[[3-2-conic-quadratic-modeling]]，$\gamma$和后面的维度并不对称
## 能跑例程
- 这个例子反映了[[tradeoff]]风险和收益
```python
import mosek
from mosek.fusion import *
def BasicMarkowitz(n,mu,GT,x0,w,gamma):
    with Model("Basic Markowitz") as M:
        x = M.variable("x", n, Domain.greaterThan(0.0))
        M.objective('obj', ObjectiveSense.Maximize, Expr.dot(mu,x))
        M.constraint('budget', Expr.sum(x), Domain.equalsTo(w+sum(x0)))
        M.constraint('risk', Expr.vstack(gamma, Expr.mul(GT,x)), Domain.inQCone())
        M.solve()
        return x.level()

n = 3
mu = [0.5] * n
mu[-1] = 1
mat_list = [0.1] * (n*n)
mat_list[-1] = 2
GT = Matrix.dense(n, n, mat_list)
x0 = [0.0] * n
w = 1.0
for gamma in range(1, 10):
    gamma *= 0.3
    print(BasicMarkowitz(n,mu,GT,x0,w,gamma))
```