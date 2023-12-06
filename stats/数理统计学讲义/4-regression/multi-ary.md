- 参考
  - [[multicollinearity]]
  - [[OLS]]

[[reduction]]
- 由于可以引入自变量$x_0\equiv 1$，于是可以把$Wx+b$写成$Wx$
- 由于$Y$的各维间没有本质区别（[[forall]]），因此可以考察$Y$为一维，即$X\beta = Y$

像[[4-regression]]说的设$e$（引入误差：$Y=X\beta + e$）
不过可能有额外条件（推出不同理论需要的额外条件不同）
- 弱：$Ee_i=0,Ee_ie_j=0,Vare_i=\sigma^2$
  - 参考[[cov#无关]]
- 强：[[iid]], [[normal]]
  - 或用[[multi-normal]]表示为$e\sim N(0,\sigma^2 I)$
  - 推论：$\hat\beta$也满足[[multi-normal]]，因为有闭式解。相应可以解有关[[standard-error]], [[t-distribution#t stats]]的题
- 记号
  - $||a||$模长
  - $Proj_M a $为$a$在$M$投影向量，$a = Proj_M a +某个垂直于M的向量$
  - 字母$X$以前表示多维随机向量，但现在表示矩阵，每行地位“均等”（即$m\times n$，$m$个数据点，$n$维）
    - 这简直就是反客为主，本来$Wx$，现在$X\beta$. 数据变成了矩阵，参数变成了向量
    - 注意$X$一般“瘦”，很多行，但列数恒定，是用来回归$Y$的“依据”（“特征”）个数。这也可以记忆各种表达式中只有$X^TX$没有$XX^T$

# 定义和计算
- 参考[[orthogonal-decomposition#projection]], [[regression-projection]]
# 性质
- $Q(\hat \beta)(即“二乘”)=||Y-X\hat \beta||^2=||Y||^2-||X\hat\beta||^2=Y^TY-\hat\beta^TX^TX\hat\beta=Y^TY-Y^TX\beta=(Y,Y-X\beta)$，几何意义也很明显
  - 满秩则进一步$=Y^T(I-X(X^TX)^{-1}X^T)Y:=Y^TAY$
    - 应用：证明：
      - 已知$X_{n\times p},rank(X)=p$，而$Y$是$X$一些列组成的
      - 则$X(X'X)^{-1}X' - Y(Y'Y)^{-1}Y'$非负定
      - 原因是$X\beta:=X(X'X)^{-1}X'y$是$y$在$Im(X)$上的正交投影，$Y\alpha:=Y(Y'Y)^{-1}Y'y$是$y$在$Im(Y)\subset Im(X)$上的正交投影
- 进一步利用之前“弱”假设
  - 可得$E\hat \beta=\beta,Cov(\hat\beta,\hat\beta)=\sigma^2(X^TX)^{-1}$
    - 回忆[[linear-transform]]
    - 这里记忆：$(X^TX)^{-1}X^TY$中“两负一正”，所以结果最后“负”
    - 直观：数据条目越多，[[cov]]大小越小
    - 进一步参见[[standard-error#multi-ary SE]], [[t-distribution#t stats]]
  - $EY^TY=||X\beta||^2+\sum var Y_i$（即利用[[expectation]]可加性和[[variance]]）
    - $=||X\beta||^2+\sum vare_i$（“平移”）
    - 当然也可以直接$Y=X\beta +e$代入证
  - $EYY^T=X\beta\beta^TX^T+Cov(Y,Y)=X\beta\beta^TX^T+\sigma^2I$
  - $EQ=EY^TAY=Etr(Y^TAY)(因为是一个标量)=Etr(AYY^T)=tr(AE(YY^T))$（[[trace]]，把常矩阵$A$换到前面，随机量放到后面）
    - $=tr  [(I-X(X^TX)^{-1}X^T)(X\beta\beta^TX^T+\sigma^2I)]$
      - 注意到$AX=0$，那就有两项直接没了
      - 再注意$tr(X(X^TX)^{-1}X^T)=tr(X^TX(X^TX)^{-1})=p$，即得待求$EQ=\sigma^2(n-p)$
    - 因此$E\hat \beta=\beta,E\hat\sigma^2:=E\frac {Q(\hat \beta)}{n-p}=\sigma^2$为无偏估计
  - 但：$\beta$在$X$不满秩时未必有无偏估计
# 例题
- $corr(y,a)=p, corr(y,b)=q$，则$\hat y$ regressed on $(a,b)$
  - 新的[[r-squared]]范围？
    - 法一：[[regression-projection]]
      - a是一根轴，y是斜线，b是圆锥母线
      - 拎着y转b
      - 如果y a b共面则$R^2=1$，是最大值
      - 转到和“共面”相对的某种“垂直”处$R^2$最小
        - 这个最小也很容易说明，你投影到二维平面长度至少是投影到直线的长度
      - conclusion: the new R2 is at most 1 and at least the maximum of previous 2 R2s.
    - 法二：
      - [[orthogonal-decomposition]]
      - 利用[[correlation#与cov关系]]相当于算cov
      - $b = c_1 a+ c_2a',c_1^2+c_2^2=1,a\perp a'$
      - $E(yb) = c_1p+c_2E(ya')=q$
      - $E(y\hat y_{a,b})=E(y\hat y_{a,a'})=d_1p+d_2E(ya')$
        - 其中$d_1,d_2\quad s.t.d_1^2+d_2^2=1,d_1/d_2=p/E(ya') $
          - 注：这个$d_1/d_2$ [[ball-tangent-optimal]]结论很好用
        - $d_1=p/\sqrt\cdots, d_2=E(ya')/\sqrt\cdots$
      - 则$E(y\hat y_{a,b})=\sqrt{p^2+E^2(ya')} $
        - 此时：[[symmetry#break]]
          - $p\ge q$时可以$|c_1|\le 1,E(ya')=0$
          - 但$p<q$时麻烦，使得$E(y\hat y_{a,b})$最小时应为[[ball-tangent-optimal]]得到$c_1/c_2=p/E(ya'),\sqrt {p^2+E^2(ya')}=q$
          - 但得到结果：最小$R^2$确实是$max(p^2,q^2)$
        - 此时可以看到[[symmetry#break]]和[[symmetry]]的对立统一：正因为[[symmetry#break]]了，我们才要用[[symmetry]]简化运算
  - 已知新旧所有[[r-squared]]求$corr(\hat y, a)$
      - [[orthogonal-decomposition]]
        - 继承上题，$d_1/d_2=p/E(ya')$
        - 故$E(\hat y a)/E(\hat y a')=d_1/d_2=E(ya)/E(ya')$
        - [[linearity]]易知$E(\hat y (na+n'a'))/E(\hat y (ma+m'a'))=E( y (na+n'a'))/E( y (ma+m'a')),E(\hat yb)/E(\hat ya)=E(yb)/E(ya)=q/p$
        - 结合$corr(\hat y,y)=E(\hat y y)=d_1E( y a) +d_2E( y a')=\sqrt{E^2( y a)+E^2(y a')}=\sqrt {R^2}$
        - 得$E(\hat ya)=E(ya)\frac{\sqrt{E^2(\hat y a)+E^2(\hat y a')}}{\sqrt{E^2( y a)+E^2( y a')}}=p\frac{1}{\sqrt {R^2}}$
        - $E(\hat y b)=q/\sqrt {R^2}$
- 标准正态，已知$corr(Y,X_1)=\rho_1, corr(Y,X_2)=\rho_2, corr(X_1,X_2)=\rho_3$，求二元回归$\rho$
  - 设$X_2 = \rho_3 X_1 + \alpha_3 Z_1, X_1\perp Z_1$
  - $Y=\rho_1 X_1 + aZ_1+bZ_2$
  - 此时有$\rho_2=E(X_2 Y)=\rho_1\rho_3+a\alpha_3 $
  - 即$(\rho_2-\rho_1\rho_3)^2 = a^2(1-\rho_3^2)$
  - $R^2=\rho_1^2+a^2 = \rho_1^2+(\rho_2-\rho_1\rho_3)^2/(1-\rho_3^2)=(\rho_1^2+\rho_2^2-2\rho_1\rho_2\rho_3)/(1-\rho_3^2)$
  - [[general-principles/special-case]]检验
    - $\rho_3=0\Rightarrow R^2=\rho_1^2+\rho_2^2$
    - $\rho_1=1,\rho_2=\rho_3\Rightarrow R^2=1$
    - $\rho_1,\rho_2$具有[[symmetry#轮换]]