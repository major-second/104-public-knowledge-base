1. [[7-numerical-methods]]有方中画圆
   1. 方差：[[binom]]
   2. 小心粗心：当然不是$\pi(1-\pi)$而是$\frac \pi 4(1-\frac \pi 4)$
2. [[7-numerical-methods]]
   1. 如接受拒绝采样，使用$F^{-1}$等
   2. 拓展：Box-Muller
3. 明确定义$dS = \mu Sdt + \sigma SdW, dS/S = \mu dt + \sigma dW$
   1. 法一：$\Delta S = S\mu \Delta t + S\sigma \sqrt {\Delta t} Z$，缺点可能有小概率负数
   2. 法二：使用[[5-brownian-motion-and-stochastic-calculus]]，Ito引理，考察$V:=lnS$的情况
4. [[中心极限定理]]，$\frac{样本均值-期望}{标准差}$
   1. 缺点：效率低，不能生成边缘值
   2. 刚刚说过一些更好方法
5. ？todo
6. [[7-numerical-methods]]
7. [[cholesky]]，[[3-linear-algebra]]讲过
8. 称为quadratically convergent, $误差/上个误差^2 < M$
9.  ？