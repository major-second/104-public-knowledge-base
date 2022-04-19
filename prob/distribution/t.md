参考[[calculus/gamma]]
$n$个自由度的$t$分布$t(n)$，分布密度$\frac{\Gamma(\frac {n+1}2)}{\Gamma(\frac n2)\sqrt {n\pi}}(1+x^2/n)^{-\frac {n+1}2}$
- $\xi\sim N(0,1),\eta \sim \chi^2(n)$则$\xi /\sqrt {\eta/n}\sim t(n)$
- $\sqrt n\bar X/\sigma\sim N(0,1),(n-1)S^2/\sigma^2\sim\chi^2(n-1)$则$\sqrt n\bar X/S\sim t(n-1)$（应用：[[枢轴量方法]]）
  - 注意区分$n$和$n-1$. [[枢轴量方法]]中的$\sqrt n$是$\bar X$那里来的，不是$\xi/\sqrt {\eta/(n-1)}$来的
- $n$趋于无穷时，该分布趋于标准正态[[normal]]
  - 严格说法：任意$x$，$lim_n p_n(x)=\phi(x)$（这里左右都是密度）
    - 提示：应用[[sterling]]公式，如[[calculus/gamma]]所述
  - $n\ge 25$时，极为接近
  - 和[[normal]]一样“钟形”，偶函数。用[[枢轴量方法]]时用法挺像
  - 查分布表时多一个“自由度”参数要查