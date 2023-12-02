- [[imagination]] [[orthogonal-decomposition#projection]]
- 前置[[multi-ary]]
# 计算得公式
- 要求$||X_{m\times n}\beta_{n\times 1} - Y_{m\times 1}||^2$最小（即最好地拟合现有数据点）
- $X\beta$所有可能取值就是矩阵$X$的列空间，记为$\mu(X)$，则$Proj_{\mu(X)} Y:=X\hat \beta$，一定存在唯一
- 充要条件：根据投影定义，$(Y-X\hat \beta)\perp \mu(X)$，于是（根据$\mu(X)$定义）考察$X$每一列，得$ X^TX\hat \beta=X^TY$
  - 这里又用到了[[forall]]思想
- 当然，前述逻辑是用投影存在证明了方程解存在。你也可以根据[[rank]]说明方程解存在
- 特殊情况：$X^TX$正定（可逆），即$X$“瘦”且列满秩，那$\hat\beta$表达式可直接得：$(X^TX)^{-1}X^TY$
  - 拓展：[[multicollinearity]]
# 直观几何意义
- 三个$(x,y)$ datapoint 3维空间，n个就是n维空间
- [[unary]]: x是一条直线，$y$投影到$x$上部分对应ESS, 勾股定理就是ESS + RSS = TSS