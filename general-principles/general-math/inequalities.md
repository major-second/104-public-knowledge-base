- 放缩，使用不等式
- 参考
  - [[estimation#理论]]
  - [[estimation#算法实际应用]]
## 放缩到界
- $min_{\theta \in \Theta}X(\theta)\le X\le max_{\theta \in \Theta}X(\theta)$
- 或min换成inf, max换成sup
- 例子
  - [[markov-chebshev#Markov]]
    - $X$天然非负，然后分成两部分，一部分大于0，一部分大于$t$
  - [[hoeffding#lemma]]
    - [[taylor-expansion]]
    - $a(1-a)\le 1/4$（均值不等式）
  - 第一积分中值定理
- 拓展
  - [[normal#Mill's Inequality]]
    - $1\le X/minX$，当$X>0$
    - 这里用在$e^{-x^2/2}\le \frac xte^{-x^2/2}$，凑出[[换元积分]]
## 十字放缩
- 思想：要不然范围小，要不然本身小
- 例子
  - [[converge-in-probability]]: 要不然概率小，要不然误差小
  - 黎曼积分的定义
## 利用导数证明
- $ln(1+x)<x,x>0$
- $e^x > x+1, x\in \mathbb R$
- $e^x > \frac {x^2}2 +x+1,x>0$，注意[[trivial-mistakes-in-math#范围]]
- $e^x \ge ex$
- $lnx\le x/e$
## 其它
- $\pi > 3$：放缩到六边形
# 经典不等式
## 均值不等式
- 和[[ball-tangent-optimal]]优化问题有关
- 初等形式
  - $(\frac{a^{-1}+b^{-1}}2)^{-1}\le \sqrt{ab}\le \frac{a+b}2\le (\frac{a^2+b^2}2)^{1/2}$
## 排序不等式
## cauchy
## [[jensen]]
## 三角不等式
