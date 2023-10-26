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