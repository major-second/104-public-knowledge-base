- 可以从一元扩展来的
  - [[random-variable-functions#cdf]]
  - [[random-variable-functions#pdf-continuous]]
- cdf都有，但pdf只有连续才有。所以无法理解时抓住本质cdf即可
# marginal
- 离散：固定一个component求和就是marginal
- 连续：固定一个component求积分
# independence
- 参考[[1-1-prob/independent]]
- 定义：任意事件$A,B$有$P(X\in A)P(Y\in B)=P(X \in A,Y\in B)$
- 实际判定对于连续的可以看[[random-variable-functions#pdf-continuous]]是否可相乘
# conditional
- 连续的严格来说没那么简单，但我们这里就用[[random-variable-functions#pdf-continuous]]凑合一下吧
# distributions
- random vector
- i.i.d.
  - 很多统计理论基础
- 实例
  - [[bernoulli-binom#multi]]
  - [[multi-normal]]