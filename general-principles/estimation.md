[toc]
# 抢占市场先机
- [[mental-math]]
- [[fermi-estimation]]
- [[adverse-selection]]
- [[jane-street-introduction]]中[文档链接](https://www.janestreet.com/static/pdfs/trading-interview.pdf)提到knowable unknowns
  - 比如喜马拉雅山天气，确实是已知数，但是你现在不知道，需要估个概率
# 理论
- [[inequalities]]
  - 给出界（所谓“推bound”）
    - [[2-7-brain-teasers]]第16题
  - 给出[[enumerate]]范围
- 物理常用估计式（$x$小）
  - $sinx\approx x$
  - $cosx \approx 1-x^2/2$
  - $(1+x)^n \approx 1+nx$
  - $ln(1+x)\approx x$
  - $e^x \approx x$
- 统计中
  - [[2-estimation]]
  - [[confidence-interval]]
# 算法实际应用
- 作为替代手段给出实际可行算法
  - [[q-learning]]
# 虚假规律
- 对于一些不成立的“规律”，在估计时可以用于给出估计值
## $Ef(X)\approx f(EX)$
- 不等号方向参考[[convexity]]
- 平方的期望本来不等于期望的平方，$E(X^2)\ne (EX)^2$
  - 他们相差就是[[variance]]
  - 但作为估算时，如果期望好算，平方期望不好算，可以用期望平方估计平方期望
  - 例如4次硬币，正面次数的平方，可估计为$2^2=4$
  - 正确值：$\frac 1{16} (0*1+1*4+4*6+9*4+16*1) = 5$
- 如多个随机变量的最大值期望近似作为期望的最大值，$E(max(X,Y))\approx max(EX,EY)$
  - 认为等于，这就是[[q-learning]]的粗略估计
  - 实际上，期望的最大值，显然小于最大值期望
    - 直观：多个随机变量，任何一个的估计量高估了，结果都高估
  - 这正是[[double-q-learning]]要解决的overestimation问题
- [[normal#例题]]
  - 忽略[[unary]]回归截距
  - 认为样本方差就是总体方差的无偏估计，不遵守[[方差的无偏估计]]的$n-1$