- 可以从一元扩展来的
  - [[random-variable-functions#cdf]]
  - [[random-variable-functions#pdf-continuous]]
- cdf都有，但pdf只有连续才有。所以无法理解时抓住本质cdf即可
# marginal
- 离散：固定一个component求和就是marginal
- 连续：固定一个component求积分
# independence
- 参考[[1-prob/independent]]
- 定义：任意事件$A,B$有$P(X\in A)P(Y\in B)=P(X \in A,Y\in B)$
- 实际判定对于连续的可以看[[random-variable-functions#pdf-continuous]]是否可相乘
# conditional
- 连续的严格来说没那么简单，但我们这里就用[[random-variable-functions#pdf-continuous]]凑合一下吧
- 实例[[multi-normal#条件分布multivariate#conditional]]
# distributions
- random vector
- i.i.d.
  - 很多统计理论基础
- 实例
  - [[bernoulli-binom#multi]]
  - [[multi-normal]]
# transforms
- 特殊情况线性参考[[linear-transform]]
- 平时
  - 如果[[random-variable-functions#discrete]]很好求
  - 否则往往先求[[random-variable-functions#cdf]]，再导出[[random-variable-functions#pdf-continuous]]
  - **如果单调**
    - 可以直接$y=g(x),\int_{x_1}^{x_2} f(x)dx = P_0=\int_{g(x_1)}^{g(x_2)} f(y)dy =\int f(y)|g'(x)|dx,f(y)=f(x)/|g'(x)| $
    - 或写作$f(y)=f(x)\cdot |\frac{dx}{dy}|$
    - 便于记忆，不严谨：$f(y)dy=dP=f(x)dx$
    - 这作为[[general-principles/special-case]]用于记忆多元情况：$f(y)=f(x)\cdot |某个雅可比|$