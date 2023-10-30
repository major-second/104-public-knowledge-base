- CLOB系统：中心化，订单簿，撮合交易
- RFQ：交易者向做市商要求数量，做市商报价，交易者比价成交
  - 这个比价自动完成相当于有个LOB出来了（LOB-like）
  - 典型：fixed income市场（债券等）
  - 软件让RFQ变得越来越all-to-all，像CLOB了
  - 然而变化需要时间
- LOB好处
  - 匿名多边交易
  - 快速、同步，支持fragmentation，竞争比价
  - 对买方（asset managers）、监管者有利，对卖方（broker等）不利
  - 现代，没必要因为可能的逆向选择给做市商补偿了
  - 做市商现在也知道orderbook dynamics了，不像五十年代，买方有很多很多信息，做市商没有
  - 而且现在这种，交易者和做市商很难区分了
- 不管哪一方，都需要分析orderbook dynamics！
  - 本章内容不仅可用于LOB
# Information reaching orderbooks
- 一天开始，空
- 出现卖价小于等于买价，则发生一笔公开交易，两笔（双方各自）private
  - 在数据中心（所以数据中心地理位置重要，决定延迟）
- 安全性：使用很多法语缩略语
  - SLE：private，和你有关的order和应答信息
  - SLC：每个人都能看到。orderbook state
  - 交易所肯定会give an advantage to客户，所以SLE更快
## A toy example
- fair price 10，典型交易者可能设定9买11卖
- 中途可能增删改
- 出现匹配就进行交易，发出两私一公信息
- 一些超出目前范围的讨论：order的附加信息。如阴阳order（iceberg），有效时间，immediate or cancel等
- 与流动性密切相关：如市价吃单/撤单减少流动性，挂单增加流动性
- 成交只能在第一档
- 我们当然要考察order book当前状态对增删改的影响
  - 更复杂的：考察外生变量
  - 但现在暂时不管
# Understanding via conditioning
- 条件分布，less random
  - 例子：只看一档大单
  - condition on一些东西，到底是否带来很大差别？学术界不同观点
  1. Zero-intelligence：很少conditioning
  2. Game theoretic：建模参与者间行为
  3. empirical：如PDE等，看变量间关系
- [[poisson-process]]
  - $\lambda=lim_{\Delta t\to 0} \frac{\mathbb E(\Delta N)}{\Delta t}$
    - 在一段小时间内，$N$上升1的概率无穷小（和时间长度成正比）
  - $\lambda \Delta t$当然就是接下来一段时间内$N$上升的期望
  - 常见分析建模方式：三个intensity: $\lambda^+,\lambda^c,\lambda^\chi$（挂限价单、撤单、交易发生）
- homogeneous（没有“条件”）
  - 三个$\lambda$都是和context无关的
  - 估算$\lambda$很简单：确定每个事件是挂单、撤单还是交易，然后在一段时间内根据$\lambda \Delta t = E$即可计算
  - （当然，选择起始点是个非平凡问题。一天的开始，还是一个事件开始，还是什么？）
  - 效果当然不好，算出概率分布和实际相差很大
- Model I of the Queue Reactive Model
  - 所有intensity的计算条件于AES（Average Event Size）这个数字
  - 例如5：表示queue size（某一档的大小）取整的话是5倍某个“平均事件大小”
  - 每次从某个时间$t$开始，到下个时间（比如某个取消$c$在$\tau^c$发生）结束
- 拓展Model II, III: 还condition on某个档的俩neighbors
  - 合理性：比如一边一档比另一边大很多，则会吃那边；比如一档很大，二档很有可能取消很多
  - predictive power of the imbalance: 一般来说不足以搞出有套利价值的波动。但是包含进交易算法是可以的！
- Asymptotic behaviors of the first two queues
  - $A/R$：到达比出发（挂单比撤单）
  - 常见的：一档消失，二档爆炸（增加）
  - 一档消失，二档成了新的一档
  - stable, (更技术地说) ergodic
- Liquidity dynamics vs. price dynamics
  - 用这些volume dynamics生成，发现价格volatility相比实际太低了
  - 问题：模拟出的二档爆炸，导致每次一个一档消失后，就要面对一座大山……，price reversion了
  - 一个可能的解决方案：[[hawkes-process]]代替[[poisson-process]]
  - 另一种，每次一个一档deplete了，有一定概率设置新价格为新fair price然后（从某个分布中随机取）重置订单簿状态
# Conclusion on orderbook dynamics
- tick大小当然很重要
- 有时可以用event做标尺，而非物理时间