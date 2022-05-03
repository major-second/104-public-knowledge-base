$X$变为$aX+b$，则均值变为$aEX+b$，方差变为$|a|^2varX$
（多元随机变量）$X$变为$AX+b$则均值也类似变，但是协方差矩阵[[cov]]呢？
- 可以根据定义计算：$Cov_新(i;j)=Cov(\sum_k a_{ik}x_k+b_i,\sum_k a_{jk}x_k+b_j)=E(\sum...+...)(\sum...+...)-E()E()$，然后对应项配对相减得$\sum_{k,l} a_{ik}a_{jl}Cov_旧(k;l)=\sum_{k,l} A(i;k)Cov_旧(k;l) A^T(l;j)$
  - 这时根据[[multiply-chain]]得$Cov_新 = ACov_旧 A^T$
  - 当然，常数项像[[character/var]]一样不影响[[cov]]