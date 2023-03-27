是[[feature-engineering]]方式
目标是使得分布满足特定形式，如均匀或[[normal]]
# 排序
- 排序，取[[character/quantile]]，强行转化成均匀分布
- 小心丢失原有意义（线性相关等）
- 小心[[information-leak]]
  - 避免[[information-leak]]和不[[stationary-processes]]的方法：[[rolling]]再排序
- 用于[[cov#corr]]的spearman
# z-score
- 参考[[normal]]，转化成均值0方差1
  - 如果认为数据有正态性[[normal]]那么就转化成标准正态了
- 也常常是在一段[[rolling]]中看
- 可以把本来不具可比性的数据变成可以比较的“相对值”
  - [参考链接](https://zh.wikipedia.org/wiki/Z-score)
# 其它
- https://www.zhihu.com/question/341394312/answer/2721418193
- 比如对数、倒数、幂次都可考虑