- 前置
  - [[1-prob/independent]]
- 请区别于[[stationary-processes]]
- 定义
  - [[1-prob/independent]]：时间轴拆成无交并，i.i.d中的[[1-prob/independent]]
  - stationary：起始点不matter，只由长度决定，对应i.i.d.中的identically
- 性质
  - [[expectation]]，$E[X_t]=m_0+m_1 t$
    - 证明过程需要柯西函数方程，下同
  - [[variance]]类似，$Var(X_t)=\sigma_0^2+\sigma_1^2t$
- 例子
  - [[poisson-process]]
  - [[5-brownian-motion-and-stochastic-calculus]]
- 实际应用
  - [[ARIMA]]
  - 股价，不是[[stationary-processes]]，但可以作差
    - 推论：[[autocorrelation]]