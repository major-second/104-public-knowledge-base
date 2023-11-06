- 前置
  - [[normal]]
  - [[maximum-likelihood]]
- $f(x;\mu,\sigma)=\frac{1}{\sqrt {2\pi} \sigma}exp(-\frac{(x-\mu)^2}{2\sigma^2})$
  - $l(\mu,\sigma)=const-nlog\sigma-\sum (x_i-\mu)^2/2\sigma^2$
  - [[orthogonal-decomposition#projection-to-a-hyperline]]得到$const-nlog\sigma-\sum(x_i-\bar x)^2/2\sigma^2 - \sum(\bar x-\mu)^2/2\sigma^2$
    - 由此$\hat\mu $马上看出为$\bar x$
  - 可以[[naming#换元或简记]]对$\sigma^2$求导
    - $\hat \sigma^2 = \frac 1n (x_i-\mu)^2=\frac 1n (x_i-\bar x)^2$（当$\mu$未知）
    - $\hat\sigma^2=\frac 1n (x_i-\mu_0)^2$（当$\mu$已知为$\mu_0$）
      - 不能生搬硬套！
- 参考[[variance#unbiased估计]]，这个并不[[unbiased]]