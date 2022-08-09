- 本章：strategies + relation to the infrastructure
- 分类（大致）
  - contractual market making
  - noncontractual market making
  - arbitrage
  - fast alpha
# CMM
- 和传统的类比关系是最强的！
- 做市商概念
  - A卖5000，B买2000，那剩下的3000要不然就unfilled，要不然就有做市商接盘
  - 日常生活比喻：厂商 - 中间商 - 零售
- 小单
  - 散户要买200，则broker让CMM直接满足散户，卖给散户200
  - 不进入交易所order book
  - 反正散户来，CMM就被动接收
- 怎么赚钱
  - [[14]]提到被动接单可能遭遇逆向选择
  - 但这里：买卖抵消，被动接单往往量不大，一般不会逆向选择
- 一个大单例子
  - 10000单位，CMM去买给客户9500，价格上涨3 cents
  - 最后500，CMM自己卖（在100.03，很高的价格卖）
  - 之后预计价格下跌，CMM会赚！
    - 类似于抄底（你想象，你可以控制别人买左侧所有单，然后你买在最底下）
  - 所以CMM故意帮客户以“低效率”拿到单，自己赚钱
  - 所以有人抗击internalization（闲话：Knight Capital就是为了应付这种Retail Liquidity Program而搞出bug的）
- 为什么CMM需要高频
  - 了解当前市场情况，提供correct price
  - 快速退场
    - 一般来说，做散户对手方还不赖
    - 然而，极端单边行情就傻了
    - 所以还是要减少“净”当对手方，而是用高速使得自己不担风险（高速退场）
# NCMM
todo
# 套利
针对多个相关的instrument
todo
# Fast alpha
- 本质上和[[3-alpha-models]]一样，使用动量、均值回归、technical sentiment等
- fundamental information不会高频变化，而且很多时候不在交易时间出现
  - 也不绝对，有时这种事件也会在高频上体现影响（消息面）
  - 外汇这种：24小时可交易，只是传统交易时间流动性更大
- 总之：套用低频策略的只是小部分。fast alpha大部分还是用量价、订单簿等
  - 但消息面带来量突变这种可能被反映到这里
- 可以高频套利，但统计上的两instrument相关也不一定恒成立，有风险
  - 各种统计当然都不一定恒成立
- 可以类似NCMM地提供流动性，但是通过选择，减少风险
- 可以使用trend，此时高频重要性体现在：放接近市价的限价order，捕捉大trend中的小回调
  - 此时更容易“滑”（slippage）等，所以特别高频的话，trend不如mean reversion常见