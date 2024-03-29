- $X$变为$aX+b$
  - 则均值变为$aEX+b$
  - 方差变为$|a|^2varX$
- 两个随机变量的协方差[[cov]]
  - 平移不影响
  - 乘法则“双线性”[[linearity]]
  - 这个性质在[[orthogonal]]中得到应用
# 多元随机变量[[multivariate]]
- 尤其[[multi-normal]]常用
- $X$变为$AX+b$则均值也类似变为$A\mu+b$
  - $A$不一定是方阵
  - 特别地，可能是行向量
- 协方差矩阵[[cov]]
  - 可以根据定义计算
   $$Cov_新(i;j)\\
   =Cov(\sum_k a_{ik}x_k+b_i,\sum_k a_{jk}x_k+b_j)\\
   =E(\sum_k a_{ik}x_k+b_i)(\sum_k a_{jk}x_k+b_j)-E(\sum_k a_{ik}x_k+b_i)E(\sum_k a_{jk}x_k+b_j)\\
   =(对应项配对相减)\sum_{k,l} a_{ik}a_{jl}Cov_旧(k;l)\\
   =\sum_{k,l} A(i;k)Cov_旧(k;l) A^T(l;j)$$
  - 这时根据[[multiply-chain]]得$Cov_新 = ACov_旧 A^T$
  - 可以使用[[general-principles/special-case]]记忆
    - 如果$A$是列向量，则$AX$无意义，所以$A$如果是向量，必须是行向量
    - 所以必须是$ACov_旧 A^T$
  - 常数项不影响[[cov]]
    - 类似于[[variance]]
  - 配对相减技巧是[[cov]]标准操作