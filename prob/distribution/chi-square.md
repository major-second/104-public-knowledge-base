- 卡方分布是特殊的[[distribution/gamma]]
  - 即$\Gamma(\frac n2,\frac 12)$
- 标准[[normal]]分布平方和：$n$个自由度的卡方分布
  - 来源：可以通过[[distribution/gamma]]可加性记忆（这样同时还记住了期望是$n$）
  - 至于单个[[normal]]随机变量平方怎么记？$f_新dt=f_旧 dx $则$f_新=(2\sqrt t)^{-1} \frac{1}{\sqrt {2\pi}}e^{-t/2}$
    - 注意$t=x^2,(dt/dx)^{-1}=(2\sqrt t)^{-1}$
    - 额还有一个正负号导致的2但反正能看出参数是$1/2,1/2$了已经
    - 参考：[[分布的变换]]
- 由[[normal]]随机变量的线性组合的性质，得：
  - $\bar X\sim N(\mu,\sigma^2/n)$
  - $(n-1)S^2=\sum (X_i-\bar X)^2=\sum X_i^2-n\bar X^2$（参考[[character/var]]）
    - 这里$S^2$分母本来就有$n-1$，所以$(n-1)S^2$其实就是$\sum()^2$
  - 对于标准正态。注意$\sqrt n\bar X$看作$Y_1$，你的$(n-1)S^2$自然$\sim \chi^2(n-1)$
  - 对于一般情况，$\sqrt n\bar X/\sigma$看作$Y_1$，你的$(n-1)S^2/\sigma^2\sim \chi^2(n-1)$
  - 这个“看作$Y_1$”还告诉你$\bar X$和$S^2$独立
- 方差
  - 根据[[character/var]]，独立随机变量方差可加
  - 只需看$\chi^2(1)=\Gamma(1/2,1/2)$方差为$EX^4-(EX^2)=3\sigma^4-\sigma^4=2\sigma^4=2$，那么$\chi^2(n)$方差就是$2n$
  - 这里利用了[[normal]]的中心矩结论