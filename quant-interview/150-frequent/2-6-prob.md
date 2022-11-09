1. 略（[[distribution/gamma]]）
2. 略（[[distribution/gamma]]）
3. [[poisson]]均值方差都是$\lambda$是常见结论
4. 等效于三角形重心
5. 几何意义显然（参考[[multi-normal]]）
6. 不要默认独立啊啊啊！
   1. lognormal: $lnX$满足正态
7. 
   1. cdf的定义：$E\Phi(Y)=E_Y(E_Z(1_{Z\le Y}))$
   2. 全期望公式：$=E_{Y,Z}(1_{Z\le Y})$
   3. 01事件的含义：$=P(Z\le Y)$
   4. 最后正态分布[[可加性]]即得
8. [[大数定律]]
   1. 独立同分布期望存在
   2. 弱，依概率收敛，$\forall \epsilon, P(误差超过\epsilon)\to 0$
   3. 强，$P(lim = ...)=1$
   4. 强推出弱
9.  [[中心极限定理]]
    1.  centered and scaled sum
    2.  条件：独立同分布有限方差（相比刚刚“期望存在”显然更强）
    3.  均值$n\mu$，方差$n\sigma^2$
    4.  因此$lim_{n\to \infty} \frac{S_n-n\mu}{\sigma \sqrt n}=Z$（注意分母是标准差）
    1.  或写作$\bar x = S_n/n\approx \mu + \sigma/\sqrt n \cdot Z$（均值是$\mu$，方差是$\sigma/\sqrt n$）
10. 