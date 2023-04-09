[toc]
# 抢占市场先机
- [[mental-math]]
- [[fermi-estimation]]
- [[adverse-selection]]
- [[jane-street-introduction]]中[文档链接](https://www.janestreet.com/static/pdfs/trading-interview.pdf)提到knowable unknowns
  - 比如喜马拉雅山天气，确实是已知数，但是你现在不知道，需要估个概率
# 理论
- [[inequalities]]
  - 给出界（所谓“推bound”）
    - [[2-7-brain-teasers]]第16题
  - 给出[[enumerate]]范围
- 统计中
  - [[2-estimation]]
  - [[confidence-interval]]
# 算法实际应用
- 作为替代手段给出实际可行算法
  - [[q-learning]]
# 虚假规律
- 对于一些不成立的“规律”，在估计时可以用于给出估计值
- 平方的期望本来不等于期望的平方，参考[[variance]]
  - 但作为估算时，如果期望好算，平方期望不好算，可以用期望平方估计平方期望
  - 例如4次硬币，正面次数的平方，可估计为$2^2=4$
  - 正确值：$\frac 1{16} (0*1+1*4+4*6+9*4+16*1) = 5$
- 如多个随机变量估计（量）的最大值期望近似作为估计（量）期望的最大值
  - 认为等于，这就是[[q-learning]]的粗略估计
  - 实际上，估计期望的最大值就是期望的最大值，显然小于估计的最大值期望
    - 直观：多个随机变量，任何一个的估计量高估了，结果都高估
  - 这正是[[double-q-learning]]要解决的overestimation问题
  - [[general-principles/special-case]]里也提到这个