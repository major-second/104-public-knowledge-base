- 参考
  - [[tick]]
  - [[2-financial-data-structures]]
- [tick 到bar](https://blog.csdn.net/weixin_38753422/article/details/95699776)
  - 需要sample（采样）

# [[2-financial-data-structures]]
- irregular -> regular
- [参考](https://zhuanlan.zhihu.com/p/158814757)
- 别忘了bar长度本身可调。可能根据实际需求，不能太浪费也不能太粗糙
## standard bars
### time bars
  - 内容
    - [[pd-timestamps]]
    - [[vwap]]
    - OHLC：open, high, low, close
    - volume
  - 缺陷
    - 未考虑time of the day影响（如开盘，量大）
      - “算法时代，cpu时钟比生物钟重要”，所以按人感知时间不准确。按市场“活跃度”更好
    - 统计性质差
      - [[autocorrelation]]
      - [[heteroskedasticity]]
        - [GARCH](https://zhuanlan.zhihu.com/p/424902442)处理这个
          - 基础是[[autoregressive]]
      - [[returns]]不是[[normal]]
- [[tick]] bars
  - 直接看多少个tick，代表信息量
  - > Price changes over a fixed number of transactions may have a Gaussian distribution
  - 小心[[auction-trades]]导致的 outliers （一个tick代表的信息量很大）
### volume bars
  - [[order-fragmentation]]或者[[matching-engine]]拆都有可能破坏tick bar有效性
  - 对于[[market-microstructure]]相关features，用volume bar可能天然方便
### dollar bars
  - [[dollar-volume]]
    - xs，gold bars would make for a fun pun
  - appreciation升值
  - > the number of shares traded is a function of the actual value exchanged
    - 总结，金融市场，钱作为信息量度量可能最[[first-principle]]
      - 考虑外汇市场更明显：显然只会考察USD, Euro, yen等
      - [[tick]]和时间多多少少也有点价值？
  - empirical evidence: 计算一定时间bar数，dollar bar挺稳定，相比volume和tick
  - corporate action可能也使得volume [[non-stationary]]
  - 随时间可以动态变大小，如市值相关，或the outstanding(未偿还) amount of issued debt（固收）
    - 这本质是[[normalization]]
  - 高频可能影响不大了
## information-driven bars
- [[market-microstructure]]
- imbalanced signed volumes -> informed traders
- [[estimation]]某个量按照之前[[EMA]]等等应该是多少
  - 积累超出了，就取bar
- tick imbalance bars
  - $b$记号：根据方向给+-1，无变化承前
  - 累加得到tick imbalance $\theta_T$，就是待考察的量
- tick run bars
  - 看$b_t$正或负积累数量
  - 强调了sequence break！中间断了，总数超过就行
- volume / turnover也有类似上面的版本