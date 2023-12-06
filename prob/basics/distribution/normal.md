- https://zh.wikipedia.org/zh-cn/%E6%AD%A3%E6%80%81%E5%88%86%E5%B8%83

[toc]
# [[random-variable-functions#pdf-continuous]]
- $f(x;\mu,\sigma)=\frac{1}{\sqrt {2\pi} \sigma}exp(-\frac{(x-\mu)^2}{2\sigma^2})$
- 可记为$\phi(x)$，必须背诵
- [[random-variable-functions#cdf]]则没有闭式，记为$\Phi(z)$
  - $\Phi(0)=1/2$
  - 和[[character/quantile]]关系：$\Phi^{-1}(1/2)=z_{1/2}=0$
# 应用
- 由于[[central-limit]]定理，所以实际中常常用到
- 实际应用：经常[[look-up]]
# [[moment]]
- 中心矩
  - 可以用[[gamma-function]]函数得结果
  - 也可以用[[characteristic-function]]的导数对应各阶矩
  - 奇数0
  - 偶数$\sigma^2, 3\sigma^4,5*3\sigma^6\cdots$
- 原点矩$V_1=\mu, V_2=\mu^2+\sigma^2, V_3 = \mu^3 + 3\mu \sigma^2,V_4=\mu^4 + 6\mu^2\sigma^2+3\sigma^4$
    - 原点矩表达式这里可以看出二项式系数（14641）（最后一项是二项式系数1乘以中心矩$3\sigma^4$）
    - 换句话说：背诵了中心矩表达式，可以快速推出原点矩
## 例题
- 标准正态，$Cov(X,Y)=\rho$
根据相关系数，设$Y=\rho X + \alpha Z, \alpha = \sqrt {1-\rho^2}, X\perp Z$
$Cov(X^2,Y^2)=E(X^2Y^2)-EX^2EY^2= E(X^2(\rho^2 X^2+(1-\rho^2)Z^2+2\rho\alpha XZ))-(EX^2)^2$
$=\rho^2 EX^4+(1-\rho^2) (EX^2)^2 - (EX^2)^2$
$=2\rho ^2$
# [[symmetry#旋转]]
- [[encode-decode#直角坐标和极坐标]]
  - 特殊[[general-principles/special-case]]：二维情况，用于计算高斯积分
  - 一般： [相关系数绝对值期望](#绝对值期望)有用到
- [[iid]]正态，$P(X>0|X+Y>0)$
- [[symmetry#翻转]]其实可以看成是[[symmetry#旋转]]特例（一维情况）
# Mill's Inequality
- $Z\sim N(0,1)$
- $P(Z>t)=\int_t^\infty \frac 1{\sqrt {2\pi}}e^{-\frac {x^2}2}dx\le \frac 1{\sqrt {2\pi}} \int \frac xt e^{-x^2/2}dx=\frac{1}{\sqrt{2\pi}}\frac{e^{-t^2/2}}{t}$
- $P(|Z|>t)\le \sqrt{\frac 2\pi}\frac{e^{-t^2/2}}t$
# 例题
## 截一半看[[cov#corr]]
- 两个[[iid]]
  - 只看$X+Y>0$部分，相关系数小于0，因为取$X\to \pm \infty$ [[general-principles/special-case]]可看出
  - 只看$X+Y<0$部分，还是
  - 参考[[counter-examples]]，这个可能反直觉
- 较严谨证明
  - $EXY=CE((X+Y)^2-(X-Y)^2)$
  - $E((X+Y)^2)$截了等于没截是$2E(Z^2)=2\sigma^2$
  - $E((X-Y)^2)$也是截了等于没截是$2E(Z^2)=2\sigma^2$
  - $EXEY$同号相乘为正
  - [[cov]]小于0
## 截中间看[[cov#corr]]
- $Y=\beta X +Z$
- 直觉
  1. 法一：只看$|X|<1$部分，噪声大，信噪比小，$|\rho|$变小
  2. 法二：理解成“椭圆，截取$|X|$小那个部分”
- 证明
  - 不妨$\beta = 1$
  - $\rho = \frac{EXY-0\cdot 0}{\sigma_X\sigma_Y}$
    - 那俩0截不截都是0
  - $\rho = \frac{EX^2}{\sqrt{EX^2}\sqrt{EX^2+EZ^2}}=(1+\frac{\sigma_Z^2}{\sigma_X^2})^{-1/2}$
  - 所谓低信噪比，就是$\frac{\sigma_Z^2}{\sigma_X^2}$偏大，结果$\rho$偏小
## $Var(XY)$
- $X,Y$正态，相关，求$Var(XY)$
  1. $Y=\rho X+\sqrt{1-\rho^2}Z$
  2. $Var(XY)=E(X^2Y^2)-(EXY)^2=E(X^2\rho^2X^2+(1-\rho^2)Z^2X^2)-\cdots$
  3. 接下来利用$X,Z$ [[1-prob/independent]]，背诵[[normal#moment]]即可
- 和[[normal#截中间看cov#corr]]类似点
  - 都是设个$Z$使得$X\perp Z$
  - [[1-prob/independent]]
  - [[naming]]
## [[cov#corr]]绝对值期望
- 题目
  - [[iid]] $X$, $Y$，各N维，N很大
  - 有截距[[unary]]回归
  - 估算从样本中算出[[cov#corr]]绝对值期望量级
- 法一：正常法
  - [[variance#与$EX^2$关系]]
  - [[estimation#$Ef(X)\approx f(EX)$]]
  - [[estimation#其它]]
  - [[variance#可加性]]
  - [[naming#有名字作为交流基础]]
  - $E|\hat \rho|\\
    \approx(认为无截距) E \frac{|\sum x_iy_i|}{\sqrt{\sum x_i^2\sum y_i^2}} \\
    \approx \frac{E|\sum xy|}{\sqrt{\sum Ex^2\sum Ey^2}}\\
    \approx E|\bar W|/Ex^2\\
    \sim (量级) E|\bar W|\sim std(\bar W)\sim std(W)/\sqrt N
    $
  - 其中$W=XY$，分布长得啥样不管，反正方差$1$量级
- 法二：[[high-dimension#球]]几何意义
  - [[imagination]]
  - [[estimation#泰勒]]
  - [[estimation#其它]]
  - [[B-function]], [[gamma-function]]
  - [[symmetry#旋转]]（各向同性）
  - [[expectation#归一化]]
  - 还是$E \frac{|\sum x_iy_i|}{\sqrt{\sum x_i^2\sum y_i^2}}$
  - 相当于N维高维[[high-dimension#球]]，夹角余弦期望，根据各向同性，“质量”集中于赤道附近
  - 现在考察纬度，即赤道记为0度，则$|sinx|$期望
  - $E|sinx|\sim \frac{\int xdm}{\int dm}$（[[归一化]]）
    $\sim \frac{\int xcos^Nxdx}{\int cos^Nxdx}(二维cos^0x，三维cos^1x以此类推)\\
    \sim \frac{\int t^{1/2}(1-t)^Ndt^{1/2}}{\int(1-t)^N dt^{1/2}}\\
    \sim \frac{B(C+1/2,N)}{B(C+0,N)}\sim \frac{\Gamma(N)}{\Gamma(N+1/2)}\sim 1/\sqrt N$，其中$C$是较小的常数（0，1，2这种）