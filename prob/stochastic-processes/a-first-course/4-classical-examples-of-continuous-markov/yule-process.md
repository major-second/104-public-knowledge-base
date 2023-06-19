- 前置
  - [[pure-birth-process]]
  - [[moment-generating-functions]]
- $\lambda_n=\beta n$
# $N=1$
- 参考
  - [[pure-birth-process]]的$Q_n = P_n e^{\beta nt}$
  - [[first-order-linear#常数变易法]]
- 取$N=1$
  - $P_1(0)=1$而非$P_0(0)=1$
- $P_1=e^{-\beta t},Q_1=1$
- $Q_n' = \beta(n-1)Q_{n-1}e^{\beta t}$
- $Q_2' = \beta e^{\beta t},Q_2 = e^{\beta t}-1$
- $Q_3' = 2\beta (e^{\beta t}-1)e^{\beta t}=\beta e^{\beta t}\cdot 2(e^{\beta t}-1),Q_3 =(e^{\beta t}-1)^2$
- 容易[[induction]]得到$P_n = e^{-n\beta t}(e^{\beta t}-1)^{n-1}$
# 一般情况
- [[yule-process#$N=1$]]的[[moment-generating-functions]]容易计算
- [[1-prob/independent]]相加相当于[[moment-generating-functions]]相乘
- 于是反解出一般情况分布列