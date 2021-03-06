[[化归]]
- 由于可以引入自变量$x_0\equiv 1$，于是可以把$Wx+b$写成$Wx$
- 由于$Y$的各维间没有本质区别（[[forall]]），因此可以考察$Y$为一维，即$X\beta = Y$

像[[4-regression]]说的设$e$（引入误差：$Y=X\beta + e$）
不过可能有额外条件（推出不同理论需要的额外条件不同）
- 弱：$Ee_i=0,Ee_ie_j=0,Vare_i=\sigma^2$
- 强：i.i.d.正态
  - 或用[[multi-normal]]表示为$e\sim N(0,\sigma^2 I)$

- 记号
  - $||a||$模长
  - $Proj_M a $为$a$在$M$投影向量，$a = Proj_M a +某个垂直于M的向量$
  - $X$以前表示多维随机向量，但现在也可表示矩阵，每行地位“均等”（即$m\times n$，$m$个数据点，$n$维）
    - 这简直就是反客为主，本来$Wx$，现在$X\beta$. 数据变成了矩阵，参数变成了向量
    - 注意$X$一般“瘦”，很多行，但列数恒定，是用来回归$Y$的“依据”（“特征”）个数。这也可以记忆各种表达式中只有$X^TX$没有$XX^T$

定义和计算
- 要求$||X_{m\times n}\beta_{n\times 1} - Y_{m\times 1}||^2$最小（即最好地拟合现有数据点）
- $X\beta$所有可能取值就是矩阵$X$列空间，记为$\mu(X)$，则$Proj_{\mu(X)} Y:=X\hat \beta$，一定存在
- 充要条件：根据投影定义，$(Y-X\hat \beta)\perp \mu(X)$或考察$X$每一列，得$ X^TX\hat \beta=X^TY$（这里又用到了[[forall]]思想）
- 当然，前述逻辑是用投影存在证明了方程解存在。你也可以根据[[rank]]说明方程解存在
- 特殊情况：$X^TX$正定（可逆），即$X$“瘦”且列满秩，那$\hat\beta$表达式可直接得：$(X^TX)^{-1}X^TY$

性质
- $Q(\hat \beta)(即“二乘”)=||Y-X\hat \beta||^2=||Y||^2-||X\hat\beta||^2=Y^TY-\hat\beta^TX^TX\hat\beta=Y^TY-Y^TX\beta=(Y,Y-X\beta)$，几何意义也很明显
  - 满秩则进一步$=Y^T(I-X(X^TX)^{-1}X^T)Y:=Y^TAY$
    - 应用：$X_{n\times p},rank(X)=p$，而$Y$是$X$一些列组成的
    - $X(X'X)^{-1}X' - Y(Y'Y)^{-1}Y'$非负定
    - 原因是$X\beta:=X(X'X)^{-1}X'y$是$y$在$Im(X)$上的正交投影，$Y\alpha:=Y(Y'Y)^{-1}Y'y$是$y$在$Im(Y)\subset Im(X)$上的正交投影
- 进一步利用之前“弱”假设
  - 可得$E\hat \beta=\beta,Cov(\hat\beta,\hat\beta)=\sigma^2(X^TX)^{-1}$（需要[[transform]]）
    - 这里记忆：$(X^TX)^{-1}X^TY$中“两负一正”，所以结果最后“负”
  - $EY^TY=||X\beta||^2+\sum var Y_i$（即利用[[expectation]]可加性和[[character/var]]）
    - $=||X\beta||^2+\sum vare_i$（“平移”）
    - 当然也可以直接$Y=X\beta +e$代入证
  - $EYY^T=X\beta\beta^TX^T+Cov(Y,Y)=X\beta\beta^TX^T+\sigma^2I$
  - $EQ=EY^TAY=Etr(Y^TAY)(因为是一个标量)=Etr(AYY^T)=tr(AE(YY^T))$（[[trace]]，把常矩阵$A$换到前面，随机量放到后面）
    - $=tr  [(I-X(X^TX)^{-1}X^T)(X\beta\beta^TX^T+\sigma^2I)]$
      - 注意到$AX=0$，那就有两项直接没了
      - 再注意$tr(X(X^TX)^{-1}X^T)=tr(X^TX(X^TX)^{-1})=p$，即得待求$EQ=\sigma^2(n-p)$
    - 因此$E\hat \beta=\beta,E\hat\sigma^2:=E\frac {Q(\hat \beta)}{n-p}=\sigma^2$为无偏估计