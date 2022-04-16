- 强相合性和（弱）相合性分别对应强大数律和弱大数律
  - “大样本”性质！
- 和大数律的不同：大数律是均值趋向于期望，而这里是估计参数值趋向于实际参数值
- 和大数律的相同：收敛的“种类”相同（本质上，参数估计值$\hat \theta_n$是个随机变量，和大数律的$\bar X_n$类比）
  - 弱：随机变量依概率收敛，即$\forall \epsilon >0,lim P(距离<\epsilon)$
  - 强：$P(lim\hat \theta_n=\theta)=1$
- 联系：当$\hat \theta$表达式就是均值，显然可以用大数律推出相合性
  - 强大数律的结论下游比较强（根据极限的性质，可以“传递”一些强相合性）
  - 例如$\hat \theta\to\theta$则$\hat \theta^{-1}\to\theta^{-1}$这种
  - 又例如正态分布$\sigma$的MLE估计的相合性：注意除了$\bar X$满足大数律，$X^2$均值也满足即可
## 用[[borel-cantelli]]证明相合性
其实强大数律用的也是[[borel-cantelli]]. 我们这里就是拆包装（参见[[primitive-operations]]）
一般用法是证明$\forall \epsilon, P(距离_n\ge \epsilon)$（关于$n$）求和收敛（这时，如果不强相合，则存在概率大于0的事件，$\overline{lim} 距离_n>0$，矛盾）
- 举例：均匀分布上下限的mle. 这里求和就是等比级数