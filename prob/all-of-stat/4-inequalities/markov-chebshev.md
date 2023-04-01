## Markov
- $tP(X\ge t)\le EX$，相当于分两段估计
  - 要求$X$==非负==
## Chebshev
- 前置[[variance]]，尤其是相加等
- $t^2P(X^2\ge t^2)\le E(X^2)$
  - 平方了，相比[Markov](#markov) 则不要求非负了
  - 变种：平移一下，变成$t^2P(|X-EX|\ge t)\le \sigma^2$
- 应用：[[bernoulli-binom]]
  - $P(|\bar X_n-p|>\epsilon) \le \frac{Var}{\epsilon^2} \le \frac 1{4n\epsilon^2}$
- 以上两节，大家的关注点都是"tail"（偏差大的那些），要求控制它们的概率小于某某
## 许多统计量
- 刚刚一阶矩，二阶矩[[moment]]都用过了，都可用于给出不等式估计概率上界
- 很多阶矩？那naive想法：$min \frac{EX^m}{t^m}$
- 那[[moment-generating-functions]]不也是一组（无穷个）统计量嘛？
  - 参考[[forall]]
  - 所以你也可以$P(X\ge k)\le inf_{t>0} e^{-tk}Ee^{tX}$（“切诺夫”）
  - 这里用到[[moment-generating-functions#性质]]
- 因此马尔可夫是根本，产生切比雪夫，切诺夫等