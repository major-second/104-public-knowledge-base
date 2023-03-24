$Poisson(\lambda)$是离散分布，概率函数$P(X=k)=\frac{\lambda^k}{k!}e^{-\lambda}$，前面部分从0开始求和显然得$e^\lambda$
- [[expectation]] $\lambda$
- [[variance]]
  - $E(X(X-1))$比较好求（抵消掉阶乘两项），是$\lambda^2$，从而方差$VarX=E(X(X-1))+EX-(EX)^2=\lambda$（方差也是$\lambda$）
- 小数定律：二项当$p \to 0, n \to \infty, np$为定值时
  - 所以实际中，两个事件绝不同时发生，观察周期短，就是好近似，例如被马踢死的士兵，十字路口车祸，被女生喜欢（bushi）
- 延伸到[[poisson-process]]