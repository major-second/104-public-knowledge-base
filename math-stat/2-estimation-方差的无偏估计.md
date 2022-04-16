$X$方差存在，则$S^2:=\frac 1{n-1}\sum (X_i-\bar X)^2$是方差的无偏估计（和具体分布，参数无关）
证明：
首先三大传统艺能（应该熟得不能再熟）
- 注意$\sum X_i \bar X = \sum \bar X\bar X$，故$\sum (X_i-\bar X)^2=\sum X_i^2-\sum \bar X^2$
- 由独立随机变量方差可加性，$\bar X$的方差是$X_i$的$1/n$
- $VarX=EX^2-(EX)^2$

因此容易得到$ES^2 = \frac n{n-1}(EX_i^2-E\bar X^2)=\frac n{n-1}(VarX_i-Var\bar X)=\frac n{n-1}(1-\frac 1n)Var X_i=Var X_i$
根据强大数律得强[[2-estimation-相合性]]