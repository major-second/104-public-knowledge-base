- 参考
  - [[t-distribution]]
  - [[hypothesis-testing]]
  - [[f-stats]]
- [参考](https://zhuanlan.zhihu.com/p/36782834)
- $t_j = \frac{\hat w_j - w_j}{\sqrt{\hat \sigma^2 (X^TX)_{jj}^{-1}}}=\frac{\hat w_j-w_j}{\hat{se}(w_j)}\sim t\_distribution_{n-k}$
  - 典型的：检验的零假设$w_j=0$，则$t_j=\frac{\hat w_j}{\hat{se}(w_j)}$
  - 因此[[multicollinearity]]会导致抖动，分母大，t统计量小，不显著
    - 对比[[f-stats]]
- [[general-principles/special-case]]
  - [[unary]]
    - [[unbiased]]: $\hat \sigma^2=\frac{RSS}{n-k}$
    - $t_j=\sqrt{n-1} \frac{l_{xy}/l_{xx}}{\sqrt{RSS/l_{xx}}}=\sqrt{n-1}\frac{l_{xy}}{\sqrt{l_{xx}(TSS-ESS)}}=\sqrt{n-1}\frac{\rho}{\sqrt{1-\rho^2}}$