- 参考[[gamma-function]]中的$\Gamma$函数定义和性质
- 在$\Gamma$分布中，$\alpha$含义不变，$\beta$是$x$前的系数，即$f(x;\alpha,\beta)\propto (\beta x)^{\alpha-1}e^{-\beta x}$
  - 比例系数（归一化常数）$\frac {\beta}{\Gamma(\alpha)}$就容易积分算出了
- 记作$\Gamma(\alpha,\beta)$
  - 当然也有人用$\beta$的倒数作为记号
- 特例
  - $\alpha=1$就是[指数分布](#指数分布)
  - $\Gamma(\frac n2,\frac 12)$就是$n$个自由度卡方分布[[chi-square]]
  - 所以$n=2$个自由度卡方分布就是指数分布
- [[可加性]]：$\Gamma(\alpha_1+\alpha_2,\beta)$
  - 即[[iid]]指数分布随机变量和不再是指数分布但是是$\Gamma$分布
  - 卡方分布[[chi-square]]相加还是卡方分布。“自由度”直接相加
  - 由可加性和[[linear-transform]]也容易直接得到均值$\alpha/\beta$，方差$\alpha/\beta^2$
- 若$S^2$满足$\Gamma$分布，则$S$的期望可以用高斯积分求
# 数字特征
- 期望就多乘一个$x$，[[variance]]就考虑$x^2$期望和$x$期望，因此都能由[[gamma-function]]求
- 举例：指数分布$f(x) = \beta e^{-\beta x}$，均值$1/\beta$，方差$1/\beta^2$
  - 因为容易计算$x$期望$\Gamma(2)/\beta = 1/\beta$，$x^2$期望$\Gamma(3)/\beta^2=2/\beta^2$
# 指数分布