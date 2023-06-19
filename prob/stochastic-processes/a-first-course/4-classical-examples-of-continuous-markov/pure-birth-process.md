- 前置
  - pure birth process是推广[[poisson-process]]
  - [[first-order-linear]]
  - [[characteristic-function]]
- 例如[[yule-process]]，出生率恒定，人口越多生育越多
- 可能convention：$X(0)=0$，则$X(t)$表示出生数量而非人口数
# ode
- 参考[[derive-ode]]，导出一系列微分方程
  - $P_0'(t)=-\lambda_0P_0(t)$
  - $P_n'(t)=-\lambda_n P_n(t)+\lambda_{n-1} P_{n-1}(t)$
- 解
  - 可直接解出$P_0(t)=e^{-\lambda_0t}$
  - 后面[[first-order-linear#常数变易法]]
  - $(e^{\lambda_nt}P_n)'=e^{\lambda_n t}\lambda_{n-1}P_{n-1}$
  - [[naming#换元或简记]] $Q_n=e^{\lambda_n t}P_n$
  - $Q_n' = \lambda_{n-1}Q_{n-1}e^{(\lambda_n-\lambda_{n-1})t}$
# waiting times
- $T_k$: the time between the kth and the $(k+1)$st birth
- 直观意义得出：各$T_k$是参数不同的[[gamma-distribution#指数分布]]，且[[1-prob/independent]]
# [[characteristic-function]]
- 参考[[characters-list]]
- $\phi_n(t)=\prod_{k=0}^{n-1}\frac{\lambda_k}{\lambda_k-it}$
- 是[[gamma-distribution]]特殊情况
# 敛散性
- $\sum P_n(t)=1\Leftrightarrow \sum \lambda_n^{-1}=\infty$
- 此处证明略
- 直觉：$ET_0+ET_1+\cdots = \sum \lambda_n^{-1}$，如果有限则说明有限时间内“人口爆炸”