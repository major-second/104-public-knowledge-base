- [[cross-validation]]
# 7.1
- In fact, CV will contribute to [[overfit]]ting through hyper-parameter tuning.
  - [[naming#命名有时是相对的]]，你相当于把validation set也当成训练集了
# 7.2
- 讲了[[cross-validation]]基础
- 用于ml模型[[hyperparam-search]]（model development），涉及backtesting的之后再说
# 7.3
- 问题
  - 不[[iid]]（本章关注）
  - multiple testing, selection bias
- 参考[[information-leak]]
- datapoints overlapping / serial [[autocorrelation]]（不显式overlapping也有“隐式”坑），导致相近时间数据点接近
  - 注：X有overlapping, 但Y足够independent，也没关系。只有$(X_i,Y_i)\approx (X_j,Y_j)$有问题
# 7.4
- purging: 显式重合的扔掉
  - 如果不做，则$k$增大leak多，表现变好
  - 做了，可能因为增加recalibrate也变好，但不会是那种
- embargo: 隐式，[[autocorrelation]]
  - 为什么对于时间方向不对称？因为实际中train在test前的autocorrelation本就是可以利用的
    - 如果不想用短时间[[autocorrelation]]，即[[problem-decomposition-internal]]，这是另一个话题。比如可以$return:=\frac{y_{10}-y_1}{y_1}$
    - 同理：滚动“1-2训 3验证；2-3训 4验证以此类推”可以，反过来验证在训练前显然不行。这都来源于时间轴不对称性
- 实现层面
  - 实现一个python `purgedKFold`类，各种地方用
  - 讲了一些具体[[sklearn]]坑
# Exercises
- [[selection-bias]]
  - [[naming#命名有时是相对的]]