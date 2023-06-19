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
- 应用：对于[[1-prob/independent]]随机变量相加十分友好
  - [[markov-chebshev#chernoff bounds]]：先构造出和[[moment-generating-functions]]相关的不等式，再用来考察[[1-prob/independent]]随机变量
  - [[yule-process#一般情况]]分布列计算：由[[yule-process#$N=1$]]得到
# 性质
- 和[[characteristic-function]]类比
  - [[linear-transform]]时，乘以常数$e^bt$，然后本身核心部分变为$\psi_X(at)$
  - 随机变量相加转化为此函数相乘（指数运算性质）
- 和分布一一对应
- [[holomorphic]]
- 和[[可加性]]联系密切（互相推）
# Laplace transform
就是个别名