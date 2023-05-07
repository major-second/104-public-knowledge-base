- 前置
  - [[random-variable-functions#pdf-continuous]]
  - [[naming#换元或简记]]
  - [[monotonous]]
  - [[chain-rule]]
# general
- pdf: $f(x)$
- $y=t(x)$
  - 先假设[[monotonous]]
  - 取[[forall#微元]], $f(x)dx = g(y)dy=g(y)dt(x)=g(y)|t'(x)|dx,g(y)=\frac{f(x)}{|t'(x)|}$
# examples
## [[chi-square]]
- 注意不[[monotonous]]，有[[symmetry#翻转]]，有2倍关系
- $x\sim N(0,1)$
- $y=x^2$
- $\phi(x)=\frac{1}{\sqrt {2\pi}}exp(-\frac{x^2}{2})$
- $g(y)=2\cdot \phi(x)/2x = \phi(x)/x=\frac{exp^{-y/2}}{\sqrt {2\pi}\sqrt y}=\Gamma(y;1/2,2)$
  - 回忆[[gamma-distribution]]
    - [[归一化]]常数$\frac{1}{2\Gamma(1/2)}=1/2\sqrt \pi$
    - $\Gamma(y;1/2,2)=(y/2)^{-1/2}e^{-y/2}/ 2\sqrt \pi=\frac{e^{-y/2}}{\sqrt{2\pi y}}$
- 结论：标准正态的平方是[[chi-square]], 自由度为1
## cdf-uniform
- $X$的pdf $f(x)$
- [[random-variable-functions#cdf]] $F(x)$
- $Y=F(X)$也是随机变量，且$F$ [[monotonous]]
- $g(y)=f(x)/F'(x)=1,0\le y\le 1$
- $Y$是[[uniform-distribution]]