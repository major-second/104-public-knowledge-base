# Gamma分布
- 首先记住$\Gamma$函数定义$\Gamma(\alpha)=\int_0^\infty x^{\alpha-1}e^{-x}dx$，$\Gamma(1)=\Gamma(2)=1$，$\Gamma(3)=2\Gamma(2)$
- 在$\Gamma$分布中，$\alpha$含义不变，$\beta$是$x$前的系数，即$f(x;\alpha,\beta)\propto (\beta x)^{\alpha-1}e^{-\beta x}$
  - 比例系数（归一化常数）$\frac {\beta}{\Gamma(\alpha)}$就容易积分算出了