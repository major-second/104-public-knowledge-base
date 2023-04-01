- 前置
  - [[moment]]
  - [[expectation]]
- 参考
  - [[characteristic-function]]
- $X$是随机变量，$e^{tX}$对于任意$t$都是随机变量
  - [[general-principles/special-case]] 0值很有用
  - $\psi_X(t):=E(e^{tX})$
  - $\psi'=E(Xe^{tX}),\psi'(0)=EX$
  - $\psi^{(n)}(0)=EX^n$
- 应用
  - [[markov-chebshev#许多统计量]]，即切诺夫
# 性质
- 和[[characteristic-function]]类比
  - [[linear-transform]]时，乘以常数$e^bt$，然后本身核心部分变为$\psi_X(at)$
  - 随机变量相加转化为此函数相乘（指数运算性质）
- 和分布一一对应
- [[holomorphic]]
- 和[[可加性]]联系密切（互相推）
# Laplace transform
就是个别名