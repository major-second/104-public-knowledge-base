- 前置
  - [[hypothesis-testing]]
  - [[confusion-matrix]]
  - [[normalization]]
  - [[bootstrap-in-stats]]
  - [[t-statistics]]
- 参考
  - [[p-value-hacking]]
  - [[overfit]]
- [参考川总知乎](https://zhuanlan.zhihu.com/p/189302345)
# 控制标准
- 是[[evaluation]]方法，目标是控制这些指标
- FWER: family-wise error rate
  - 一个都不能 FP，故[[type-i-ii-errors#type-ii-error]]太高
- 温和的：FP的期望多少、FP小于定值概率多少
# 算法
- [[bootstrap-in-stats]]时间窗，[[normalization]]后得[[t-statistics]]
  - 回忆[[t-statistics]]越大越“好”（显著）
- 总体原则
  - [[normalization]]相当于去除待考察异象的影响，考察纯凭运气[[t-statistics]]能到多少
  - 通过[[bootstrap-in-stats]]估算纯凭运气[[t-statistics]]能到多少
  - 如果运气的大于实际的，说明不靠谱