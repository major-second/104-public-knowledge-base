- $p$分位数：可以记作$z_p$，不一定唯一（可能多对一，也可能一对多）
    - 满足$P(X<z_p)\le p\le P(X\le z_p)$
    - 一定要唯一？则一种办法是定义为$inf\{x:F(x)>q\}$
- [[random-variable-functions#cdf]] $F$
  - 则（其性质）最好的情况下，有$F(z_p)=p,z_p=F^{-1}(p)$
  - 注意如果“性质最好”，那$P(X<x)=P(X\le x)=F(x)$，否则不一定
  - 比如标准正态[[normal]]的$F$就是$\Phi$，且性质好
  - 那就$\Phi(0)=0.5,z_{0.5}=\Phi^{-1}(0.5)=0$
- 特殊称谓：$1/4, 1/2, 3/4$为first quartile, median, third quartile