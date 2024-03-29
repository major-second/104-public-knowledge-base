- 前置
  - [[expectation]]
  - [[moment]]
# 基础
- $\sum X_i \bar X = \sum \bar X\bar X$，故$\sum (X_i-\bar X)^2=\sum X_i^2-2\sum \bar X^2+\sum \bar X^2=\sum X_i^2-\sum \bar X^2=\sum X_i^2-n\bar X^2$
- $VarX=EX^2-(EX)^2$
  - 因此$EX=0$情况$EX^2=VarX$，例如[[fisher-information#均值为0]]
- 是特殊的中心矩[[moment]]，[[general-principles/special-case]]
  - 当然也就可以先算[[moment]]再算出方差，例如[[gamma-distribution#数字特征]]
- [[linear-transform]]的方差参见[[linear-transform]]
# standard deviation
- 标准差：方差开方
- 标准误：参考[[standard-error]]，区别于标准差
# 可加性
- [[1-prob/independent]]独立（其实只需无关）随机变量方差可加
  - 由此，[[iid]]时$\bar X$的方差是$X_i$的$1/n$
- 联合[[linear-transform]]得到常见结论：[[iid]]相加$N$个，方差变为$1/N$，标准差变为$1/\sqrt N$
  - 联想[[central-limit]]
  - [[trivial-mistakes-in-math#开根号]]
  - 应用
    - [[normal#cov#corr绝对值期望]]
    - [[chi-square#variance]]
# [[unbiased]]估计
- 条件$X$方差存在[[iid]]
  - 则$S^2:=\frac 1{n-1}\sum (X_i-\bar X)^2$是方差的无偏估计
  - 即：无偏估计$S^2 =\frac{n}{n-1}样本方差> 样本方差$
    - 相当于样本方差因为错误估计[[expectation]] ，会偏小
  - 此结论和具体分布，参数无关
- 证明
  - 回忆[[variance]]性质和常见操作
    - [基础](#基础)
    - [可加性](#可加性)
  - 容易得到$ES^2 = \frac n{n-1}(EX_i^2-E\bar X^2)=\frac n{n-1}(VarX_i-Var\bar X)=\frac n{n-1}(1-\frac 1n)Var X_i=Var X_i$
  - 根据强大数律得强[[相合性]]
- 应用
  - 结合B-L-S定理，给出[[optimal-estimator]]
  - 多一个“武器”用于[[linearity#估计量线性组合]]
  - 用于[[standard-error]]估算，使得不需要做多次试验[[bootstrap-in-stats]]
    - 进而计算[[asymptotically-normal#normal-based interval]]等
# 与$EX^2$关系
- 参考
  - [[estimation#$Ef(X)\approx f(EX)$]]
  - [[orthogonal-decomposition#projection-to-a-hyperline]]
- 刚刚[基础](#基础)提过
- 中心矩[[moment]]方差恒小于等于原点矩$EX^2$
- 对于$N$大，$EX=0$情况
  - 样本$E|\sum _iX/n|$以$1/n$速度趋于0（[[central-limit]]）
    - 样本$(EX)^2/n^2$以$1/n^2$速度趋于0
  - 样本$E\sum_i X^2/n$是常数量级，不趋于0
    - 且越来越接近[[variance#unbiased估计]]
  - 因此此时$EX^2\approx VarX$
- 小样本粗略[[estimation]]，认为方差为0
  - 则此时$EX^2\approx (EX)^2$（和刚刚对比一下！）
  - 4次硬币，正面次数的平方，可估计为$2^2=4$
  - 正确值：$\frac 1{16} (0*1+1*4+4*6+9*4+16*1) = 5$