- 属于[[evaluation]]
- [参考](https://zhuanlan.zhihu.com/p/409732430)

|quantity|数量|公式
|-|-|-|
|InitialCapital| 初始资产|
|Value| 持仓股总市值|
|Cash| 账户可用现金|
|Capital| 账户总资产|Value+Cash|
|NetValue| 账户净值| Capital/InitialCapital|
|ProfitPct| 账户总收益率|(NetValue−1)∗100|

- 可通过[[returns]] [[pnl]]的估计，画出大致的曲线
  - 需要[[cumsum]]
- 可导出（看出）指标
  - [[sharpe]]
  - 回撤[[drawdown]]
- 可画train/test的，看出[[overfit]]程度