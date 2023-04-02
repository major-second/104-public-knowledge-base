# 心算中
- 估算、速算、心算使用
- 背诵常用数值
  - 乘法表
  - 2、3、5的幂
  - $ln2\approx 0.693, ln3\approx 1.099,ln5\approx 1.609, ln10\approx 2.303$
  - $\sqrt 2 \approx 1.414,\sqrt{3} \approx 1.732, \sqrt{5} \approx 2.236$
  - $\pi \approx 3.14, e\approx 2.718$
- 熟悉运算法则
  - 如完全平方公式应用$(10a+b)^2=...$，平方差公式，对数相关的公式等
- [[2-7-brain-teasers]]第16题利用$1024\approx 1000$可估算$125^{100}$的位数
# 虚假规律
- 对于一些不成立的“规律”，在估计时可以用于给出估计值
- 平方的期望本来不等于期望的平方，参考[[variance]]
  - 但作为估算时，如果期望好算，平方期望不好算，可以用期望平方估计平方期望
  - 例如4次硬币，正面次数的平方，可估计为$2^2=4$
  - 正确值：$\frac 1{16} (0*1+1*4+4*6+9*4+16*1) = 5$
- 如多个随机变量估计（量）的最大值期望近似作为估计（量）期望的最大值
  - 认为等于，这就是[[q-learning]]的粗略估计
  - 实际上，估计期望的最大值就是期望的最大值，显然小于估计的最大值期望
    - 直观：多个随机变量，任何一个的估计量高估了，结果都高估
  - 这正是[[double-q-learning]]要解决的overestimation问题
  - [[general-principles/special-case]]里也提到这个
# 统计中
- 参考[[2-estimation]]
  - 例如[[moment-estimation]], [[mle]]等等
- 利用已有数据进行统计学意义的估算
# 无先验时
- 参考[[jane-street-introduction]]中[文档链接](https://www.janestreet.com/static/pdfs/trading-interview.pdf)提到knowable unknowns
  - 比如喜马拉雅山天气，确实是已知数，但是你现在不知道，需要估个概率
- 方法技巧
  - [[fermi-estimation]]
  - 注意[[adverse-selection]]，看别人表现也可以影响你的决策
# 放缩
- 放缩也算估计的一种吧哈哈
## 放缩到界
- $min_{\theta \in \Theta}X(\theta)\le X\le max_{\theta \in \Theta}X(\theta)$
- 或min变成inf, max变成sup
- 例子
  - [[markov-chebshev#Markov]]
    - $X$天然非负，然后分成两部分，一部分大于0，一部分大于$t$
  - [[hoeffding#lemma]]
    - [[taylor-expansion]]
    - $a(1-a)\le 1/4$（均值不等式）
- 拓展
  - [[normal#Mill's Inequality]]
    - $1\le X/minX$，当$X>0$
    - 这里用在$e^{-x^2/2}\le \frac xte^{-x^2/2}$，凑出[[换元积分]]