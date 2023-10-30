- 参考[[16-HFT]]
- 区别于[[26-intra-day-data]]，这里重点讲的是日内交易，而不是使用日内数据做其它交易
## 总述
- 日内交易，收盘前停
- 可能作为overall strategies一部分
- 对于[[future]]交易三种目的，日内交易基本属于投机
- 和价值投资不同（参考[[3-alpha-models]]的分类）
- 有了纳斯达克，电子交易，废止commission rates，才流行
- 和日频不同，有pros and cons
## 和daily的不同
- 更加关注微观，如量价，订单簿等，[[16-HFT]]也提到
- less diverse information sources
- 更加希望单因子（相对于其cost）有效，因为计算要求高，信息量少
- 往往赚钱多，表现好
- 训练/测试集差别少
- 规避隔夜风险（见势不对马上跑）
- 只能小资金，高流动性！
## 分类
- overnight-0：绝不过夜，不overlay
- 可能由某indicator连续指定，或由某进场出场离散信号决定
  - `abnormal change in some derived statistics (called events)`
  - 出场可能是信号/止盈止损
- 大部分量在开收盘
- 不同种的性质很不同。往往要针对一个instrument/相近的一组，设计策略
## MAKING AN INTRADAY ALPHA
- 参考[[3-alpha-models]]. 一个mean reversion因子
- $second\_last\_interval\_close - last\_interval\_close$
- 不是简单用，而是用给流动性前五百，有买有卖，dollar neutral
- 进阶：乘以一个标准差，表示波动大的更容易回调
  - 也可以除
  - “乘”：激进，期望高，但波动性大，Sharpe小
  - 标准差可以用绝对数值，也可以用sector的相对排名