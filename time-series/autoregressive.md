- [参考](https://zhuanlan.zhihu.com/p/341779110)
- $x_t = \phi_0+\sum \phi_i x_{t-i} +\epsilon_t$, $\phi_p\ne 0$
- 随机干扰序列均值方差给定相互[[cov#无关]]
  - 回忆[[multi-ary]]的假设中也有
- $E(x_s\epsilon_t)=0,s<t$
  - 随机干扰可能和将来序列值有关（干扰是原因）
  - 但干扰不是结果（这种“结果”应该建模起来）
- 常见数字特征
  - 类比普通的随机变量的[[expectation]], [[cov]], [[correlation]]等数字特征
  - 自协方差函数
  - [[autocorrelation]]
    - 拖尾，和[[moving-average]]相对
  - [[partial-correlation]]
    - 各个$\phi_i$，截尾