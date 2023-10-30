# 19.1
- [[market-microstructure]]
- > Market microstructure studies “the process and outcomes of exchanging assets under explicit trading rules”
- > The main source is Financial Information eXchange (FIX) messages, which can be purchased from exchanges
# 19.5
- [[sequential-trade-models]]
- [[PIN]]
- [[VPIN]]
# 19.6
- 相比19.5 either 有一套 or 编出一套理论解释一个很直观的feature $\frac{\sum_{\tau=1}^n|V^B-V^S|}{nV}$，这里不需要理论了，直接提取feature
- "mouse" / GUI traders: 整数大小，abnormally frequent
  - 监控比例，和trend 程度有关
- cancellation rates, limit orders, market orders
  - attempt to [[adverse-selection]] market makers
    - quote stuffers: latency arbitrage, DDOS骚扰交易所
    - quote danglers
    - liquidity squeezers: 跟大单，吃大单想要流动性，overshoot
    - pack hunters
  - 通过以上指标，empirically判断这些参与者
- 整数秒，[[twap]]算法，机构单。可以薅他们羊毛
- stock / options 信息传递/套利
  - quote
    - 后者 spread is derived from put-call parity
    - 两者spread disagree
    - 前者dominate后者
  - trade
    - 后者具有额外信息，如PM used to trade options (illiquid products)
  - todo
- signed [[order-flow]] [[autocorrelation]]: herding and order splitting
  - less than a few hours, 主要后者