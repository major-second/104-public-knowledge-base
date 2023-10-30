- 前置[[random-variable-introduction]]
- 一般针对实值
# cdf
- cumulative distribution function
- $F_X(x) = P(X\le x)$
  - $F_X$记号可理解成$X$诱导出$F_X$
  - 有人当然会用$<$
  - 总之cdf只有单侧连续能保证
  - $P(X=x)=F(x)-F(x^-)$，这个$F(x^-)$记号意义明显吧？
- 和[[character/quantile]]关系
  - 这个是把数值映射成概率，单调不减
  - [[character/quantile]]反过来是概率映射成数值。性质好时互为反函数
- 决定分布
  - cdf相同，则$P(X\in A)=P(Y\in A)$
  - 但两个随机变量（两个映射）不一定相同
  - 称为“equal in distribution”
  - 记作$=^d$
- 性质（判定）
  - 当且仅当
    1. 单调不减
    2. 右连续
    3. 负无穷和正无穷处极限分别是0，1
  - 是某个随机变量的cdf
  - 其中“当”方向需要比较复杂的分析工具
# discrete
- 称为：probability function or probability mass function
- 每个点多少概率
- 反映在[cdf](#cdf)上：阶跃
- 实例：[[bernoulli-binom]], [[nega-binom]], [[poisson]]
# pdf-continuous
- 连续随机变量：有pdf可以积分得变量落在区间中概率
- 连续性
  - 此时[cdf](#cdf)肯定连续但pdf不一定
  - pdf连续的那些点，cdf可导，且$F'=f$
- 和[cdf](#cdf)区别
  - 连续随机变量每个单点处概率为0
  - pdf本身可超过1，甚至无界
- 实例：均匀，[[normal]], [[gamma-distribution]], [[chi-square]], [[t-distribution]], [[f]]
- 变换：[[pdf-transform]]