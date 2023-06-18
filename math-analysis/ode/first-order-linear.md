- https://zhuanlan.zhihu.com/p/537253058
- $y'+P(x)y=Q(x)$
  - $y$这里是“线性”
  - $P(x), Q(x)$关于$x$不一定
  - $P,Q$中不能含$y$显然
- 对应的齐次$y'=-Py$是[[separable]]，解为$y=Ce^{-\int Pdx}$
  - 当$P$为常数特殊情况$y=Ce^{-Px}$
# 常数变易法
- 凑出**积求导法则**
  - $y'e^{\int Pdx}+Pe^{\int Pdx}y=Qe^{\int Pdx}$
  - $(ye^{\int Pdx})'=Qe^{\int Pdx}$
  - **背公式**：$y=e^{-\int Pdx}(C+\int(Qe^{\int Pdx})dx)$
- 可能[[naming#换元或简记]] $()'$内的为整体
# 应用
- [[poisson-process]]
- [[pure-birth-process]]