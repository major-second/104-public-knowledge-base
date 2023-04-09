- https://zh.wikipedia.org/zh-cn/%E6%AD%A3%E6%80%81%E5%88%86%E5%B8%83
# 应用
- 由于[[central-limit]]定理，所以实际中常常用到
- [[random-variable-functions#pdf-continuous]]是有的：$\frac{1}{\sigma \sqrt {2\pi}}exp\{-\frac 1 {2\sigma^2} (x-\mu)^2\}$，记为$\phi(z)$
- [[random-variable-functions#cdf]]则没有闭式，记为$\Phi(z)$
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
# 各向同性
- [[encode-decode#直角坐标和极坐标]]
  - 特殊[[general-principles/special-case]]：二维情况，用于计算高斯积分
  - 一般： [相关系数绝对值期望](#绝对值期望)有用到
- [[iid]]正态，$P(X>0|X+Y>0)$
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
## [[cov#corr]]绝对值期望
- 题目
  - [[iid]] $X$, $Y$，各N维，N很大
  - 有截距[[unary]]回归
  - 估算从样本中算出[[cov#corr]]绝对值期望
- [[estimation]]
  - 首先可以估计成无截距
  - 然后可以认为$Ef(x)=f(EX)$
- 参考
  - [[2-estimation]]
  - [[variance#unbiased估计]]
  - [[variance]]
    - 
    - 当$EX^2- (EX)^2 \gg (EX)^2$
  - [[estimation#$Ef(X)\approx f(EX)$]]
- 法一：正常法
  - $E|\hat \rho|\\
    \approx(认为无截距) E \frac{|\sum x_iy_i|}{\sqrt{\sum x_i^2\sum y_i^2}} \\
    = E\sqrt{\frac{(\sum x_iy_i)^2}{\sum x_i^2\sum y_i^2}} \\
    \approx \sqrt{\frac{(E(\sum_i X_iY_i))^2}{ENX^2ENY^2}} \\
    $
  - 其中
- 法二：[[high-dimension#球]]几何意义