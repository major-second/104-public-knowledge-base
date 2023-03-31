- 前置
  - [[normal]]
  - [[cov]]
  - [[linear-transform]]
# 基础
- 用向量表示均值，用矩阵表示[[cov]]，记为$N(\mu,\Sigma)$
- 标准正态：$N(0(零向量),I(单位阵))$
  - 在[[multi-ary]]中用到了
  - $f(z)=\prod_{i=1}^k f(z_i)=\frac 1 {(2\pi)^{k/2}}exp\{-\frac 12 \sum_{j=1}^k z_j^2\}$
    - 其实也是多个iid相乘
# 一般情况
- $f(x;\mu,\Sigma)=\frac 1{(2\pi)^{k/2}|(\Sigma)|^{1/2}}exp\{-\frac 12 (x-\mu)^T \Sigma^{-1}(x-\mu)\}$
- 一种退化[[general-principles/special-case]]
  - $\Sigma=\sigma^2I$
  - 这样看出分母$(2\pi)^{k/2}\sigma^k$
- 再继续退化就$\sigma=1$
- 变换参考[[linear-transform]]
  - $\Sigma^{1/2} Z+\mu\sim N(\mu,\Sigma)$
  - $\Sigma^{-1/2}(X-\mu)=^d Z(标准正态)$
    - 由此，$V=(X-\mu)^T\Sigma^{-1}(X-\mu)$相当于标准正态中平方和，满足$\chi^2_k$
    - 参考[[chi-square]]
  - $a^T X\sim N(a^T\mu, a^T \Sigma a)$
# 条件分布[[multivariate#conditional]]
- $\mu = (\mu_a, \mu_b)$
- $\Sigma = \left(\begin{matrix}\Sigma_{aa}&\Sigma_{ab}\\\Sigma_{ba}&\Sigma_{bb}\end{matrix}\right)$
- $X_b|X_a=x_a \sim N(\mu_b + \Sigma_{ba}\Sigma_{aa}^{-1} (x_a-\mu_a), \Sigma _{bb}-\Sigma _{ba}\Sigma _{aa}^{-1}\Sigma_{ab})$
- 证明：思路是利用[[linear-transform]]得到[[1-prob/independent]]随机变量
  - $diag(\Sigma_{aa}^{-1/2},I)(X-\mu)\sim N(0,\left(\begin{matrix}I&C\\C^T&\Sigma_{bb}\end{matrix}\right))$
  - $\left(\begin{matrix}I&0\\-C^T&I\end{matrix}\right)diag(\Sigma_{aa}^{-1/2},I)(X-\mu)\sim N(0,diag(I, \Sigma_{bb}-C^TC))=N(0,diag(I,\Sigma_{bb}-\Sigma_{ba}\Sigma_{aa}^{-1}\Sigma_{ab}))$ 
  - $\left(\begin{matrix}\Sigma_{aa}^{-1/2}&0\\-\Sigma_{ba}\Sigma_{aa}^{-1}&I\end{matrix}\right)(X-\mu)$后面分量，等于$X_b-\mu_b-\Sigma_{ba}\Sigma_{aa}^{-1}(X_a-\mu_a)\sim N(0, \Sigma_{bb}-\Sigma_{ba}\Sigma_{aa}^{-1}\Sigma_{ab})$
  - 证毕
# 例题
- $X_1, X_2$独立标准正态，则$X_1>0, X_1+X_2<0$概率是$\frac 18$，因为在平面上画出来占45度角
  - 在[[5-brownian-motion-and-stochastic-calculus]]中包装它出了道题
  - [[2-6-prob]]也有