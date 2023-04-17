- 前置
  - [[empirical-distribution-function]]
  - [[statistical-functionals#plug-in estimator]]
  - [[variance]], [[standard-error]]
# 词源
- boot, 靴带 -> “自己提自己上天”
- 参考[[bootstrap]]，是一个词
  - 那里如[[u-disk-boot]], [[multiple-ubuntu-versions]]
  - 强调的是在有限条件下自己逐步搞定步骤，使用[[temp-solution]], [[workaround]]等
- 这里
  - 强调不需要人为划分
  - 而是通过$(1-1/m)^m\to 1/e$自己进行划分
    - 注：这是重要极限[[calculus/limit]]的应用
  - 得到和原数据集$D$大小相同的数据集$S$
- 同一个词，侧重点不同，但都体现“自己做”意思
# 概述
- 举例：需要估计一个[[statistical-functionals]]：$T_1(F):=Var_F(T)$
- 如果采用[[statistical-functionals#plug-in estimator]]，可直接代入[[empirical-distribution-function]] $\hat F_n$，也就是$Var_{\hat F_n}(T)$
- 现在怎么计算$Var_{\hat F_n}(T)$
  - 可以假设我们能[[stochastic-simulation]]出满足$\hat F_n$的许多($B$)个大小为$n$的数据集，对他们分别计算$T$，再求[[variance]]
  - 写成公式$v_{boot}=\frac 1B \sum_{b=1}^B(T^*_{n,b}-\frac 1B \sum_{r=1}^BT^*_{n,r})^2$
- 最后问题：怎么[[stochastic-simulation]]出$\hat F_n$
  - 根据[[empirical-distribution-function]]的定义，直接[[iid]]均匀抽即可
  - 这里是有放回 with replacement，参考[[1-prob/independent]]
# [[confidence-interval]]
1. 直接利用算出的[[standard-error]]，计算[[asymptotically-normal#normal-based interval]]
2. [[pivotal-interval]]
   1. [[pivotal-interval#pivotal]]是$\hat \theta_n-\theta$，分布关于$X_i$恒定，但未知，记为$H$
      1. 这点就和[[pivotal-interval#举例]]中很多例子不同了！
   2. 然后估计$H^{-1}(\alpha/2)\approx \hat \theta^*_{\alpha/2}-\hat \theta_n$
      1. 其中$\hat \theta^*_{\alpha/2}$是样本[[character/quantile]]
   3. 即可得到结果$(2\hat\theta_n-\hat \theta ^*_{1-\alpha/2},2\hat \theta_n-\hat \theta^*_{\alpha/2})$
3. percentile interval: 直接根据bootstrap算出$\hat \theta$的分布找[[character/quantile]]
   1. $(\theta^*_{\alpha/2},\theta^*_{1-\alpha/2})$
# 应用
- [[ensemble#bagging]]