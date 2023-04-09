- 前置
  - [[estimation#$Ef(X)\approx f(EX)$]]
  - [[unbiased]]
- 参考
  - [double q-learning](https://paperswithcode.com/method/double-q-learning)
    - 2 Estimating the Maximum Expected Value
- 待估计量：$max_i EX_i$，一系列[[expectation]]的最大值
# single estimator
- single estimator $max_i \bar X_i$，paper中记为$max_i \mu_i(S)$
  - $\bar X_i$，$\mu_i(S)$：样本均值
  - $\bar X_i$当然是$EX_i$的[[unbiased]]估计
- 然而$max_i \bar X_i$并不是$maxEX_i$的[[unbiased]]估计
- 原因
  - [[symmetry#轮换]]，不妨设$EX_1$最大
  - $Emax\bar X_i-maxEX_i=E(max\bar X_i-EX_1)=E(max \bar X_i -X_1)\ge 0$
  - 一般情况都是大于号
# double estimator
- $\mu_i^A,\mu_i^B$是两个$EX_i$的[[unbiased]]估计
  - 可能是$\bar X_i$但不一定是
- double estimator定义
  - $\mu_{a^*}^B$
  - 其中$a^*:=argmax_i \mu_i^A$
- 对比 [single estimator](#single-estimator)，两个要点
  1. 先指定脚标$i$（比如$a^*$）再生成估计量
     1. 第二步生成的$\mu_1$即使很小，那也就留着了
        1. 还是不妨设$EX_1$最大
        2. $a^*$应该等于$argmax_i EX_i=1$
     2. 相比之下，[single estimator](#single-estimator)生成的$\mu_1$如果太小，就会被其它碰巧大的$\mu_i$掩盖
  2. 指定的脚标$i$不一定正确
     1. 如果所有时候$a^*=1$，则[[unbiased]]
     2. 但实际上并不是，故反而低估了
- 加深理解：一个退化[[general-principles/special-case]]
  - 所有随机变量[[iid]]
  - single estimator还是高估了
  - double estimator变为[[unbiased]]而非低估