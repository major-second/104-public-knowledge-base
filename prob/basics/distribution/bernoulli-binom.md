# bernoulli
- $P(X=1)=p, P(X=0)=1-p$
# binom
- $P(X=k)=C_m^k \theta^k(1-\theta)^{m-k},k=0,1,\cdots,m$
- 是独立同分布[bernoulli](#bernoulli)之和（[[可加性]]），因此
    - $EX=\theta m,EX^2=mEX_i^2+m(m-1)EX_iX_j=m\theta+m(m-1)\theta^2$
    - $VarX=m\theta+m^2\theta^2-m\theta^2-m^2\theta^2=m\theta(1-\theta)$
        - 当然也可以通过[[variance]]与[[可加性]]结合求方差
# multi
- $f(x)=\frac{n!}{x_1!\cdots x_k!}p_1^{x_1}\cdots p_k^{x_k}$
- 边缘分布是[二项](#binom)
- [[cov]]可以按定义计算（注意$X_iX_j\equiv 0, i\ne j$）