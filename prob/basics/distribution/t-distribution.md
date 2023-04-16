- 参考
  - [[gamma-function]]
  - [[normal]]
# 定义
- $n$个自由度的$t$分布$t(n)$
  - [[random-variable-functions#pdf-continuous]]
  - $\frac{\Gamma(\frac {n+1}2)}{\Gamma(\frac n2)\sqrt {n\pi}}(1+x^2/n)^{-\frac {n+1}2}$
- $\xi\sim N(0,1),\eta \sim \chi^2(n)$则$\xi /\sqrt {\eta/n}\sim t(n)$
## 应用
- 参考
  - [[chi-square#normal的variance#unbiased估计]]
    - 那里有[[off-by-one-errors]]，这里也有
- $\sqrt n(\bar X-\mu)/\sigma\sim N(0,1),(n-1)S^2/\sigma^2\sim\chi^2(n-1)$则$\sqrt n(\bar X-\mu)/S\sim t(n-1)$
  - 应用：[[pivotal-interval]]，[[广义似然比]]
  - 注意区分$n$和$n-1$
  - [[pivotal-interval]]中的$\sqrt n$是$(\bar X-\mu)$那里来的，不是$\xi/\sqrt {\eta/(n-1)}$来的
# [[general-principles/special-case#极限情形]]
- $n$趋于无穷时，该分布趋于标准[[normal]]
- 严格说法
  - 任意$x$，$lim_{n\to\infty} p_n(x)=\phi(x)$（这里左右都是密度）
  - 自然需要[[gamma-function]]比值极限
- 实际中$n\ge 25$时，极为接近
- 和[[normal]]一样的点
  - “钟形”，偶函数，[[symmetry#翻转]]
  - 用[[pivotal-interval]]时用法也挺像，只不过[[look-up]]时多一个“自由度”参数要查
# t stats
- 应用中，常常和[[hypothesis-testing]]联系，$t$统计量绝对值大说明“显著”
  - 联系[[asymptotically-normal]]理解
  - 例如[[multi-ary]]，零假设$H_0: \beta_j = 0$，则单个系数$\beta_j$的$t$统计量为$\frac{\hat{\beta_j}}{SE(\hat{\beta_j})}$
  - 其中$SE(\hat{\beta_j})$为$\hat{\beta_j}$的标准误[[standard-error#multi-ary SE]]