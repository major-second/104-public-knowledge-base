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
  - [[方差的无偏估计]]
  - [[estimation#虚假规律]]
- 法一：正常法
$E|\hat \rho|\\
 \approx(认为无截距) E \frac{\sum x_iy_i}{\sqrt{\sum x_i^2\sum y_i^2}} \\
 = \sqrt{\frac{(\sum x_iy_i)^2}{\sum x_i^2\sum y_i^2}} \\
 $
- 法二：[[high-dimension#球]]几何意义