是[[feature-engineering]]方式
目标是使得分布满足特定形式，如均匀或[[normal]]
# 排序
- 排序，取[[character/quantile]]，强行转化成均匀分布
- 小心丢失原有意义（线性相关等）
- 小心[[information-leak]]
  - 避免[[information-leak]]和不[[stationary-processes]]的方法：[[rolling]]再排序
- 用于[[cov#corr]]的spearman
# z-score
- 前置
  - [[normal]], [[moment]], [[variance]]
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
  - [参考链接](https://zh.wikipedia.org/wiki/Z-score)
# 其它
- https://www.zhihu.com/question/341394312/answer/2721418193
- 比如对数、倒数、幂次都可考虑