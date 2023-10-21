- [参考](https://zhuanlan.zhihu.com/p/27689464)

[toc]
# bagging
- 参考[[bootstrap-in-stats]]
- 全称bootstrap aggregating
- 相比[[ensemble#boosting]]
  - 可以[[parallelism]]，例如随机森林
    - 这个除了[[bootstrap-in-stats]]外
    - 还注意每次没有使用相同features
  - 能减缓[[overfit]]而不是增加
- 可对比[[augment]]
  - 其实也相当于某种增强
## random forest
- [调参例子](https://zhuanlan.zhihu.com/p/126288078)
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
- 思想
  - 拟合负梯度，使得总的损失函数梯度下降
    - 当然也可以有类似[[deep-learning/optimization#BGD, SGD, MBGD]]的随机做法
  - 直接拟合残差是直接看哪个数据点离得远，而现在拟合负梯度是看哪个数据点附近预测值变化能导致损失变小得多
  - 拟合完负梯度得到的弱学习器线性地乘以某个系数加上去
    - 对于GBDT，稍微不同
      - 每个区域各自乘系数
      - 总体框架（怎么分区域）是拟合负梯度，完了之后每个区域各自看了，而不保持原来比例
      - [[4-decision-tree]]
- 独特参数：shrinkage，加上新学习器时乘以一个系数再加，有点感觉是平滑
- [应用例子](https://blog.csdn.net/RuDing/article/details/78332192)
# stacking
- 输出信号再做组合，套娃！
- 理论上可以表示上面两种