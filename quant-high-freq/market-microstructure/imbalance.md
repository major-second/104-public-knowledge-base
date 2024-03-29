- 基础：$\frac{v_b^{(1)}}{v_a^{(1)}+v_b^{(1)}}$，$\frac{v_a^{(1)}-v_b^{(1)}}{v_a^{(1)}+v_b^{(1)}}$等简单表达式
  - 拓展：更多档、加权更多档、自适应设置多少档以及权
  - `bid size, ask size`
- 可以[[grid-search]]的参数
  - [[normalization]]怎么做
    - 很多时候做一下$\frac{A-B}{A+B}$就是比单纯$A-B$效果好
      - 但是也不绝对
        - 分母可能导致数值性质不好
        - 可能错误[[normalization#丢失信息]]，反而是 $A-B$就好！
    - 相比数据本身，较长的[[sliding-window]]作为分母？
    - 哪些[[normalization]]维度？例如time of the day
  - horizon长度
  - [[bar-data]]标准
- 对[[price-targets#midprice]]有一定预测作用
  - 一般靠这个不足以赚钱，因为
  1. 浅层理解
     1. 谁都知道，不够打赢手续费
     2. [[order-execution]]并不简单
  2. 本质理解：[[naming#命名有时是相对的]]
     1. 实际上price并不是一个简单的midprice
     2. 参考[[price-targets]]
        1. 现象：不同[[price-targets]]可做出的[[correlation]]大小不同，但不一定代表不同的profitability
- 拓展：有时本质上是两分布之间的差距，所以可以用[[t-statistics]]，[[hypothesis-testing]]，[[kl-divergence]]，乃至binary classification