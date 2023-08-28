- 影响market impact大小的因素：流动性，你这单占的比例，算法“侵略性”，执行时间
- timing非常重要：比如你被什么trigger，是trend follower还是mean reverter，在HFT眼里你属于什么……
# Market impact over the trading period
- 0到100执行一个order，价格向相应方向先变再撤回（但不完全撤回）
- impact和stock一些性质、order一些性质都有关
- participation rate越大、**相同participation rate**时间越长，影响越大
  - 模型$Impact$正比于$Duration^{\alpha} * Participation^{\gamma}$
  - 注意凹凸性
  - 经过calibration，$\gamma$约为0.5
# Market impact on a longer horizon: Price anticipation and permanent market impact
- 考虑更长期（日频左右）
- todo