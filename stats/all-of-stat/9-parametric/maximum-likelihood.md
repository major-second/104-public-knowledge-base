# likelihood function
- [[random-variable-functions#pdf-continuous]]**或**[[random-variable-functions#discrete]]$f(x;\theta)$
- 似然函数（给定$x$下$\theta$的函数）$L(x_1,\cdots;\theta)=\prod_i f(x_i;\theta)$
  - 和概率、概率空间
    - 区别：$\theta$不是事件，$L$关于$\theta$积分不为1
    - 联系：在[[bayesian-inference]]先验为常数时，如果积分有限，则是[[归一化]]常数，可放到分母，最后得到$\theta$后验分布。**先验为常数，似然函数和后验成正比**
- 最大似然的定义$\hat\theta=argmax_{\theta\in \Theta}L$
- 实际中常用对数似然函数
  - 原因：$f$往往做了连乘，取对数后比较方便
  - 例如[[maximum-likelihood-normal]]
# MLE
- 本质是[[optimization-using-derivatives]]，数分题
  - $\Theta$是开集时求导即可
    - 往往取对数再求导
  - [[naming#换元或简记]]后求导，例如[[maximum-likelihood-normal]]
- 极值与最值
  - 求导得到极值，不一定是最大值。这在数分里也是经常需要检验的
    - [[uniform-distribution]]的MLE就经常在边界
  - 由此还引申出一类题目：证明MLE存在
    - 类似数分证明最值存在，可能可以通过证明区域$\Omega$外都小来证。
    - 例如$x$满足参数为$\alpha,\beta$的[[gamma-distribution]]，可以取个范围，范围外$f$都足够小，范围内有一个$f$比较大的点，即可证明
  - 有时要在边界上找最值（有时在角，有时还会在曲边边界，更麻烦），但总之都是数分题
- 结果不一定是显式解，比如韦布尔分布
  - 这时说明[[相合性]]就需要用隐函数的连续性等性质
  - 这个有点像[[method-of-moments]]中的合理性说明
  - 对于非显式解，实际中就可能$||\tilde\theta-\theta||^2\le ||\tilde \theta-\hat\theta||^2+||\hat\theta-\theta||^2$，一部分计算（优化）误差，一部分统计误差
- 参数模型设计得不好会怎么样
  - 可能没有MLE
    - 比如没最大值
      - $f(x;\mu,\sigma^2)=Ae^{-x^2/2}+B/\sigma \cdot e^{-(x-\mu)^2/2\sigma^2}$，那你完全可以前半部分保底，后半部分“针尖”搞得似然函数无界
  - 可能MLE存在但不相合
    - 比如下面诡异的模型
      - $P_\theta(X=x)=\theta^x(1-\theta)^{1-x},x=0,1$（当$\theta$有理）
      - $P_\theta(X=x)=\theta^{1-x}(1-\theta)^x,x=0,1$（当$\theta$无理）
# consistency
- 前置[[entropy#KL Divergence]]
  - 其非负
- 不用管太细节，只看大致思想
  - 优化似然函数相当于优化$\frac 1n\sum log\frac{f(X_i;\theta)}{f(X_i;\theta^*)}$
  - 后者期望显然是$-D(\theta^*,\theta)$，在$\theta=\theta^*$时最大值0
# equivariance
- [[equivariant-invariant#equivariant]]
- 例子：$\hat \mu = \bar X,\hat{e^\mu}=e^{\bar X}$
- 证明：设$\tau = g(\theta),\theta=h(\tau)$，则写出$\tau$的似然函数为$\prod_i f(x_i;h(\tau))$，当且仅当$h(\tau)=\theta^*,\tau=g(\theta^*)$时似然函数最大
# [[asymptotically-normal]]
- [[standard-error]]表示MLE出的$\hat \theta$标准差，是[[statistical-functionals]]
  - 它约等于$\sqrt {1/I(\theta)}$，参考[[fisher-information]]
    - [[fisher-information]]对于某个$\theta$，是[[数理统计学讲义/1-introduction#估计量和统计量]]统计量，可用于估计[[standard-error]]
- $\frac{\hat\theta-\theta}{se}$依分布收敛到标准[[normal]]
- $se$换成$\hat{se}:=\sqrt{1/I(\hat\theta)}$（估计值），还是依分布收敛到标准[[normal]]
- 因此可构造出[[asymptotically-normal#normal-based interval]]
- 简单例子[[fisher-information#bernoulli-binom#bernoulli]]
# optimality
- 用MLE相比用中位数作为估计，是[[优良标准#无偏-有效性]]的
  - 参考[[optimal-estimator]]
    - 不过条件和那里不一样
    - 考察细节太复杂，这里不考察了
  - 直觉：中位数只利用了一部分数据