- 前置[[lob]]
- 参考
  - [知乎链接](https://www.zhihu.com/question/513782601/answer/2328043857)
  - [IC课件](https://www.ma.imperial.ac.uk/~ajacquie/Gatheral60/Slides/Gatheral60%20-%20Stoikov.pdf)
- 很多时候没有标准答案，各有优劣
  - [[aggregation]]
# midprice
- $M=\frac 12 (P^a+P^b)$
- $P^a$是best ask, $P^b$是best bid
- 缺点
  - [[bid-ask-bounce]]
    - 从而也[[autocorrelation]]，不是[[martingale]]
    - 没法[[problem-decomposition]]掉无意义赚不了钱的bounce
    - 假阳性
  - 相对于[[quote]]变化频率太低
  - 没考虑volume
# weighted midprice
- 前置[[imbalance]]
- $\frac{Q^bP^a+Q^aP^b}{Q^b+Q^a}$
- [参考](https://quant.stackexchange.com/questions/50651/how-to-understand-micro-price-aka-weighted-mid-price)
  - 此处被称为microprice
  - 讲了直觉：$Q^b$大，说明greater buying pressure, fair price is closer to the ask
- 缺点
  - 变化频率过高[[market-microstructure-noise]]太高
  - 不是[[martingale]]
  - 反直觉现象
    - 问题来源：出现跨档
# microprice
# start and end
- 除了数值本身，还要看起止点怎么选择。比如指定时间/量/event...
  - [[bar-data]]