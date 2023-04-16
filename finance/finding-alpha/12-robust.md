- 总述
  - Invariance：“迁移学习”也能work
  - Robustness：市场突变，不要变化太大
    - 指标参考[[4-design]]，[[5-case-study]]
# ordering
- 参考[[normalization#排序]]
- 提升invariance（对不同universe）
- ordinal scale
- 是一种非参数模型（参考[[parametric-or-not]]）
  - 在参数模型的[[hypothesis-testing]]不通过时常用！
- 需要更少假设。容易处理极端值
- quantiles approximation：如最小化平方残差的分位数（"median squares minimization"）
# Approximation to Normal Distribution
- 参考[[normal]]
- 如：大致正态，只不过有长尾、outlier
- Fisher：$F(x)=\frac 12 ln(\frac{1+x}{1-x})$
  - [参考](https://en.wikipedia.org/wiki/Fisher_transformation)，大致说来是二元正态分布的相关系数经过此变换后满足正态
- [[normalization#z-score]]
# Limiting Methods
- trimming：超过了就简单除去
- winsorizing：太极端的收收味
- 还可能用中位数缓解极端值影响
- 理论上，各种trim, winsorize, median都是[[order-statistics]]的线性组合
- 不适用：本来就有skew（参考[[moment]]），或者有很多相同值（一堆0显然不行）
  - 比如[[27-intra-day]]的乘以标准差，如果标准差常常为0（例如期货市场最小价格变动单位太大），就会出事