- $E[e^{itX}]$，是一个随机变量的复（值域）函数（也是随机变量）的期望
- 意义
  - 一一对应随机变量分布，可还原，和[[cov]], [[expectation]]等不同
  - 独立随机变量和的特征函数是特征函数的积
  - 对$t$求导可求矩
# 例题
- 两个[[iid]]随机变量相加是[[uniform-distribution]] $U[0,1]$
  - $f(t)=Ee^{itx}=\int_0^1 e^{itx}dx=\frac{e^{it}-1}{it}$
  - [[calculus/limit]]，易知$f(0)=1$
  - 因此$\sqrt {f(t)}$，反变换回去即可给出待求随机变量