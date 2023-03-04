- 前置[[poisson]]
  - 来自稀有事件、小数定律
  - $t$时间内表示有多少个事件
  - nondecreasing step function
- 参考[[1-elements]]
# 推导
## 低阶
- 无记忆性（独立[[prob/independent]]）
  - 因此$P_0(t+h)/P_0(t) = 1-p(h),\frac{P_0(t+h) - P_0(t)}{h} \to -常数\cdot P_0(t)$（当$h$小）
  - 其中$p(h)$表示泊松过程，$P_0$表示一段时间没有发生事件，常数来自$p(h)/h\to a$
- 列解微分方程得到
  - $p'_t = -at$
  - $P_0(t)=e^{-at}$（精确）
  - $P_1(h)=p(h)+o(h)=ah$（大约）
  - $\sum_{i=2}^m P_i(h)=o(h)$
## 高阶
- 类似刚才
  - $P_m(t+h)-P_m(t)=(我记为)\Delta P_m=ah(P_{m-1}-P_m)$
  - $P_m'=aP_{m-1}-aP_m,P_0=e^{-at}$
- 这是[[first-order-linear]]微分方程
  - 参考常数变易法思想进行换元
  - 而不是直接套公式！这里相当于[[leaky-abstraction]]
  - $Q_m=P_me^{at},Q'_m=aQ_{m-1}$
  - $Q_0=1,Q_1=x(常数为0由Q_m(0)=0,m=1,2,\cdots得到)$，等等
  - $Q_m=\frac{a^mt^m} {m!},P_m=\frac{a^mt^m} {m!}e^{-at}$
  - 这个$P_m$恰为参数为$at$的[[poisson]]分布，符合原始物理含义！
  - 除了时间，有时也用于空间分布