- 参数取值空间：$\mathbb R^m$子集
- 待估计：$\theta$的函数
  - 回忆[[数理统计学讲义/1-introduction]]中说是“泛函”
  - 目前当然是特殊情况
  - 比如正态分布中的$P(X>c)$可以用参数$\mu, \sigma$表示，是参数的函数
# 方法
- 通法
  - [[maximum-likelihood]]
  - [[method-of-moments]]
  - [[statistical-functionals#plug-in estimator]]
  - [[linearity#估计量线性组合]]
- 一个必记特例：[[variance#unbiased估计]]
# 性质
- [[优良标准]]
- [[相合性]]，[[unbiased]]，[[asymptotically-normal]]
- 有了[[优良标准]]就当然可找[[optimal-estimator]]
# 相关链接
- [[confidence-interval]]
- [[non-parametric]]
  - [[empirical-distribution-function]]
  - [[密度函数估计]]
# 用作精确计算
- 有时用类似“估计”的过程可以精确计算
  - 例如[[proportional#等车例题]]
    - 先确定分布是[[nega-binom#geometric]]
    - 再给定一个[[general-principles/special-case]]，$P(X=0)$即可得到分布
    - 相当于[[待定系数法]]