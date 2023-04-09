- 参数取值空间：$\mathbb R^m$子集
- 待估计：$\theta$的函数（回忆[[数理统计学讲义/1-introduction]]中说是“泛函”。目前当然是特殊情况）
  - 比如正态分布中的$P(X>c)$可以用参数$\mu, \sigma$表示
# 方法
- 通法
  - [[maximum-likelihood]]
  - [[method-of-moments]]
  - [[statistical-functionals#plug-in estimator]]
- [[unbiased]]中一些非通法
  - 必记特例：[[方差的无偏估计]]
# 性质
- [[相合性]]，[[unbiased]]，[[优良标准]]，[[asymptotically-normal]]
- 有了优良标准就有[[optimal-estimator]]
# 区间估计[[confidence-interval]]
- 之前：由样本观测值计算出某个统计量，作为估计量
  - 参考[[数理统计学讲义/1-introduction]]
- 而现在计算出两个统计量，作为上下限
  - 要求满足：对一切参数
    - 参数一律平等，[[forall#一致]]
    - 参考[[优良标准]]
  - 满足“落在里面”概率大于等于置信度$\gamma$
  - 必读：[[confidence-interval#interpretation]]
# [[parametric-or-not#non-parametric]]
- [[empirical-distribution-function]]，[[密度函数估计]]
# 用作精确计算
- 有时用类似“估计”的过程可以精确计算
  - 例如[[proportional#等车例题]]
    - 先确定分布是[[nega-binom#geometric]]
    - 再给定一个[[general-principles/special-case]]，$P(X=0)$即可得到分布
    - 相当于[[待定系数法]]