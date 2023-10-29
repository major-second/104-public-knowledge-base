- [参考](https://zhuanlan.zhihu.com/p/149889323)
    - 仅供参考，可能有不准确的
# 10.1
- 联系德扑哈哈哈，trader打德扑
# 10.2
- 一条原则：希望有“余地”能抓住连续机会
- $c_{t,l}$这里没介绍清楚
    - 表示有多少个区间覆盖了当前点
    - 对比[[4-sample-weights]]
      - [[4-sample-weights]]中是多少个label涉及price path覆盖某点
      - 这里是多少个prediction (bet)的holding period涉及
        - 参考10.4第一句话
    - 用处
      - 可以用来混合不同频率信号，多策略等
        - [参考](https://zhuanlan.zhihu.com/p/149889323)知乎笔记强调了多策略
      - 退化[[algorithm/special-case]]
        - 如果简单处理，一种频率，一个策略，holding period都相同
        - 相当于某种对于前一段时间该策略bet的[[moving-average]]
          - 例：连续相同方向预测将导致bet $m$往一个方向上升
- 法一
  - 计算信号强度$c_t= c_{t,l} - c_{t,s}$
  - 拟合模型（设信号强度分布满足两个[[gaussian-mixture]]）
  - 使用模型，计算分位数，得$m$
- 法二
  - 计算某种[[normalization-internal]]加权后信号强度$m_t = c_{t,l}/max_i(c_{i,l}) - c_{t,s}/max_i(c_{i,s})$
  - $max_i(...)$数值来自历史数据
- 总结
  - 信号强度决定仓位（零阶）而不是仓位变化（一阶）
  - [[moving-average]]思想，连续相同prediction可能导致一阶变化
# 10.3
- 法三
  - 前置
    - [[3-labeling]]计算的概率
    - [[central-limit]]
  - 利用[[central-limit]]的思想计算$\frac{p-1/n}{\sqrt{p(1-p)}}$，常见$n=2$，其满足正态分布[[normal]]，于是根据分位数给出$[-1,1]$数值
    - 例如，若$p=1/n$，则在正态分布 0.5 分位数，对应数值$2*0.5-1=0$
  - 好处
    - [[3-labeling]] meta labeling方法可专门处理 FP等
    - 相比法一法二，转换直接方便
# 10.4
- [[moving-average]]防止太高[[turnover-换手]]
- 刚刚法一、法二有了，这里可能针对法三
# 10.5
- [[discrete-continuous]]问题。变化太小就别动了，同样减少[[turnover-换手]]
- 以上只讲了bet sizing得到仓位，没有讲[[order-execution]]. 可以先最简单[[twap]]之类执行
# 10.6
- 本节讲了一种具体的同时得到仓位和[[order-execution]]的算法