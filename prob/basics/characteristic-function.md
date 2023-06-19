# 定义
- $\phi(t):=E[e^{itX}]$
- 是一个随机变量$X$的复（值域）函数$e^{itX}$（也是随机变量）的[[expectation]]
- 联系参考
  - [[moment-generating-functions]]
  - [[characters-list]]
# 性质
- [[expectation#linearity]]可以用，则对于$p$概率取$X$，$1-p$概率取$Y$这种就可以线性相加
  - [[poisson-process#electrical pulses]]
- 一一对应随机变量分布，可还原
  - 这点和[[cov]], [[expectation]]等不同，包含全部信息
  - 是没有丢失信息的[[encode-decode]]
- [[1-prob/independent]]随机变量和的特征函数是特征函数的积
  - [[pure-birth-process]]，先找到[[1-prob/independent]]随机变量和，再找到特征函数
- 对$t$求导可求[[moment]]
# 例题
- 两个[[iid]]随机变量相加是[[uniform-distribution]] $U[0,1]$
  - $f(t)=Ee^{itx}=\int_0^1 e^{itx}dx=\frac{e^{it}-1}{it}$
  - [[calculus/limit]]，易知$f(0)=1$
  - 因此$\sqrt {f(t)}$，反变换回去即可给出待求随机变量