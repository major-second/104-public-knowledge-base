- [参考](https://zhuanlan.zhihu.com/p/27689464)
- [[6-ensemble-methods]]
- [[8-ensemble]]

[toc]
# bagging
- 参考[[bootstrap-in-stats]]
- 全称bootstrap aggregating
- 结果：分类投票/概率做平均，回归做平均等
- 相比[[ensemble#boosting]]
  - 可以[[parallelism]]，例如随机森林
    - 这个除了[[bootstrap-in-stats]]外
    - 还注意每次没有使用相同features
  - 能减缓[[overfit]]而不是增加
- 可对比[[augment]]
  - “都更好utilize已有数据集”
## random forest
- [调参例子](https://zhuanlan.zhihu.com/p/126288078)
# boosting
- 串行，不断提升
## AdaBoost
- 失败的点权重变多，更加重视
## GradientBoost
- [[gradient-boost]]
# stacking
- 输出信号再做组合，套娃！
- 理论上可以表示上面两种
- 但特别小心[[overfit]]
# 广义
- [[central-limit]]
  - 可以解释为很多预测为单点值的预测器，加在一起效果变稳定了
- [[normal]] [[可加性]]
  - $N(1,1)$和$N(1,1)$ [[cov#无关]]随机变量得到$N(2,2)$，则$\mu/\sigma$变为$\sqrt 2$倍
  - 推论应用：投资策略多样化导致[[sharpe]]提升
- 在变量少时，多变量[[OLS]]比单变量
  - 结果在不同时段/数据集更稳定，相当于某种“互补”、去噪
  - 可以理解成多个单变量线性回归的stacking
  - 但太多了显然会[[overfit]]
- 手动[[feature-engineering]]中部分操作
  - [[naming#命名有时是相对的]]，你已经很不[[end-to-end]]了，还可以更加手工
  - 比如两个高度相关的，手动$a+b$，$rank(a)+rank(b)$等权，不要[[OLS]] suffers from [[multicollinearity]]