- [参考](https://zhuanlan.zhihu.com/p/27689464)

[toc]
# bagging
- 参考[[machine-learning/bootstrap]]
- 相比 [boosting](#boosting)可以[[parallelism]]，例如随机森林
  - 这个除了[[machine-learning/bootstrap]]外
  - 还注意每次没有使用相同features
- 可以对比[[augment]]
# boosting
- 串行，不断提升
## AdaBoost
- 失败的点权重变多，更加重视
## GradientBoost
- [参考](https://zhuanlan.zhihu.com/p/26327929)
  - 这里也提到防[[overfit]]措施
    - 迭代次数
    - 树复杂度
    - 最小叶子限制
- 思想：拟合负梯度，使得总的损失函数梯度下降
  - 当然也可以有类似[[deep-learning/optimization#BGD, SGD, MBGD]]的随机做法
# stacking
- 输出信号再做组合，套娃！
- 理论上可以表示上面两种