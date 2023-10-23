- 前置
  - [[moment]]
  - [[variance]]
  - [[linear-transform]]
  - [[normal]]
- 参考
  - [[preprocessing]]
  - [[dimensionless]]
  - [参考preprocessing](https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing)
- 是[[feature-engineering]]方式
- 目标是使得分布满足特定形式，如均匀、[[normal]]，或[[moment]]满足指定条件……
- [参考](https://en.wikipedia.org/wiki/Normalization_(statistics))
# 丢失信息
- norm往往会丢信息，关键是这个信息是不是有用的
  - [领英泛泛而谈](https://www.linkedin.com/advice/0/how-do-you-balance-trade-off-between-data-normalization)
  - [知乎丢失信息具体例子](https://www.zhihu.com/question/395811291/answer/2141681320)
    - [[transformer]]使用 [[layernorm]]
- 举例
  - 时序数据，每个时刻有若干个对象，每个对象若干维feature
  - 如果暴力一个维度标准化，可能会抹平某一个维度信息
    - 例如 1 2和2 4两个序列可能被标准化成都是1 2，保留时序信息抹除截面信息
- 类比[[11-feature-selection]]：没用的丢弃
- [[batchnorm#Scale and Drift]]就是减少丢失信息
# 排序
- 排序，取[[character/quantile]]，强行转化成[[uniform-distribution]]
- [[time-series]]中常用的`.rank()`就是。一般`pct=True`，搞到$[0,1]$
- 单调变换时保持不变
- 小心
  - [[information-leak]]
    - 避免[[information-leak]]和不[[stationary-processes]]的方法：[[rolling]]再排序
  - [[normalization#丢失信息]]，如是否线性相关等
- 应用
  - [[spearman]]
# 减去均值
- 参考[[data-science/residual]]
# 除以标准差
- 理论
  - [[central-limit]]
  - [[asymptotically-normal]]
- 实践
  - [[ic-ir]]
  - [[sharpe]]
# min to max
- [[pil-open-convert-save]]中把$[0,255]$到$[0,1]$
# z-score
- 相当于[[normalization#减去均值]]，[[normalization#除以标准差]]结合
- 转化成均值0方差1
  - 如果认为数据有正态性[[normal]]那么就转化成标准正态了
- 也常常是在一段[[rolling]] [[sliding-window]]中看
```python
import numpy as np
def calc(z, k):
  length = len(z)
  # e.g. len(z) = 10, k = 5
  # 0th 0
  # 9th 56789
  first_sum = 0
  second_sum = 0
  window_length = 0
  result = []
  for i in range(length):
    if np.isfinite(z[i]):
      first_sum += z[i]
      second_sum += z[i]**2
      window_length += 1
    prev_index = i - k
    if prev_index >= 0 and np.isfinite(z[prev_index]):
      first_sum -= z[prev_index]
      second_sum -= z[prev_index]**2
      window_length -= 1
    print(window_length)
    print()
    if window_length == 0 or not np.isfinite(z[i]):
      result.append(np.nan)
      continue
    first_moment = first_sum / window_length
    second_moment = second_sum / window_length
    variance = second_moment - first_moment**2
    print(first_moment, variance)
    stddev = variance**0.5
    if abs(stddev) < 1e-6:
      result.append(0)
    else:
      result.append((z[i] - first_moment) / stddev)
  return result

test_input = [1,2,np.nan,3,3,3,3,3,4,4,4,4,4,np.inf,np.inf,np.inf,np.inf,np.inf,5]
test_k = 5
print(calc(test_input, test_k))
```
- 可以把本来不具可比性的数据变成可以比较的“相对值”
  - [参考](https://zh.wikipedia.org/wiki/%E6%A8%99%E6%BA%96%E5%88%86%E6%95%B8)
# 为什么
- 为什么要把均值、方差变为0，1？
- [参考](https://blog.csdn.net/rope_/article/details/107826059)
  - 标题是深度学习，其实general针对机器学习
- general原则：去除无关的共性，凸显个性，类似于[[11-feature-selection]]
- 假设球[[symmetry]]时当然必须
  - [[11-feature-selection]]中罚项
  - [[overfit]]中罚项
  - [[clustering]]
- 对[[multi-ary]] OLS影响
  - 主要[[float]]误差
  - 理论上pred一样
  - 比如$200\times 0.1, 201\times 0.1$这种，相比$1\times 0.1, 0\times 0.1$这种，显然更大误差
- 涉及梯度时，还有一个问题：单个轴scaling不[[保角]]，所以本来直接向圆心的可能变成不是
- 有时候scale无影响
  - [[4-decision-tree]]：原始的决策树算法的话没啥影响（保序即可）
  - 朴素贝叶斯当然无影响
## 深度学习中为什么
- 方便调学习率
  - 参考[[deep-learning/optimization#BGD, SGD, MBGD]]
  - [[gradient-issue]]
- 防止梯度过小的[[gradient-issue]]
  - [[activation]]两侧死亡等
- 不做[[batchnorm]]等怎么办
  - 比如多次随机[[weight-init]]，枚举多种学习率等，相当于机器筛出一个适当的东西做归一化吧
  - 其实可能最后本质差不多，但这样机器负担重一点，encode人先验少
# 其它
- https://www.zhihu.com/question/341394312/answer/2721418193
- 比如对数、倒数、幂次都可考虑
  - 例如长尾取对数后更像[[normal]]