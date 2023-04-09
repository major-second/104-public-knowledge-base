- 前置
  - [[jensen]]
    - 这里运用的：对于下凸（$e^x$这种二阶导正），有$Ef(x)\ge f(E(x))$
  - [[moment-generating-functions#性质]]，比如随机变量相加，母函数相乘
- 参考
  - [[concentration]]中的求极值
  - [[markov-chebshev#chernoff bounds]]的“一系列不等式求界”思想
  - [知乎](https://zhuanlan.zhihu.com/p/573151917)
# lemma
- 条件$EX=0,X\in [a,b]$
- 结论$Ee^{sX}\le e^{s^2(b-a)^2/8}$
- 具体证明
  - 采用[[discrete-continuous]], [[forall]]思想，每次考察一小“对”，$p_1x_1+p_2x_2=0$的情况
  - 根据[[jensen]]
    - $e^{sx_1}p_1+e^{sx_2}p_2\ge 1$
    - 然而我们并不要这个方向
    - 而是$e^{sx_1}p_1+e^{sx_2}p_2\le e^{sa}p_a+e^{sb}p_b$了
    - $\ge$是向中间，$\le$是向两边
  - $ap_a+bp_b=0,p_b=-ac/(b-a),p_a=bc/(b-a)$
    - 所以就是$\le \frac{c(e^{sa}b-e^{sb}a)}{b-a}$
    - 此时[[naming#换元或简记]]
      - $\lambda = \frac{-a}{b-a}$，很自然
      - $\mu = s(b-a)$，方便指数上操作
    - $e^{sx_1}p_1+e^{sx_2}p_2\le ce^{sa}((1-\lambda)+\lambda e^\mu)$
  - 指数就是$\phi(\mu):=-\lambda\mu+ln((1-\lambda)+\lambda e^\mu)$
    - 关于$\mu$极值出现在$\phi'(\mu)=-\lambda +\lambda e^\mu/(1-\lambda+\lambda e^\mu)=0$处
      - 诶呦，熟悉的式子，如果我们需要关于$s$极值，直接解得$\mu = 0$
      - 参考[[concentration]], [[forall]]
    - 然而我们现在不是求关于$s$极值，而是针对指定$s$ 使用[[inequalities]] 放缩
      - $\phi(0)=0,\phi'(0)=0,\phi''(\mu)=(1-\lambda)\lambda e^\mu/(1-\lambda+\lambda e^\mu)^2$
      - $\phi''(\mu)=\frac{1-\lambda}{1-\lambda+\lambda e^\mu}\frac{\lambda e^\mu}{1-\lambda+\lambda e^\mu}\le \frac 14$
      - $\phi(\mu )\le \mu^2/8$
# main contents
- $P(\sum_{i=1}^n (X_i-\mu_i) \ge \epsilon)\le e^{-s\epsilon}Ee^{s\Sigma}$
- $\le e^{-s\epsilon}e^{\sum s^2(b_i-a_i)^2/8}$
- 任意$s$都成立，所以最紧的是$\le e^{-\frac{2\epsilon^2}{\sum(b_i-a_i)^2}}$
## 等价形式
- $P(\bar X\ge \mu+\epsilon/n)\le e^{-\frac{2\epsilon^2}{n(b-a)^2}}$
- $P(\bar X\ge \mu+\epsilon)\le e^{-\frac{2n\epsilon^2}{(b-a)^2}}$
- [[bernoulli-binom]] $P(\bar X\ge \mu+\epsilon) \le e^{-2n\epsilon^2}$
- 注意[[trivial-mistakes-in-math#单双侧]]，如果双侧就是$P(|\bar X-\mu|\ge \epsilon)\le 2e^{\cdots}$
- 用[[confidence-interval]]语言
  - $[\mu - \epsilon,\mu+\epsilon]$是置信水平$1-2e^{-2n\epsilon^2/(b-a)^2}$置信区间
  - $\sqrt{\frac{(b-a)^2}{2n}ln(2/\alpha)}$是置信水平$1-\alpha$置信区间