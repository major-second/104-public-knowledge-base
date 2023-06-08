[toc]
# 概述
- `nan`是一个特殊的**浮点数**，可以用
  - `float('nan')`（python原生）
  - `np.nan`（需要[[numpy-basics]]）表示
- 注：因此：对于原本是整数类型的地方，就没法手动设`nan`
# 检测
- 单个数是否是`nan`用`torch.isnan`或`np.isnan`看
- 常用`np.any(np.isnan())`
- 求和
  - 例如对于二维张量，直接`sum(sum(tensor))`或者`tensor.sum()`
    - 如果有任何一个地方`nan`，结果就是`nan`
  - 当然，求和是`nan`还有可能是正无穷加负无穷，这时`np.any(np.isnan())`检测不到。其实不符合题意
- `numpy`、`pandas`、`torch`不同
  - `import numpy as np; import pandas as pd; import torch`
  - `example = np.array([[np.nan, 0], [1, 1]]); print(example.sum()); print(pd.DataFrame(example).sum()); print(torch.tensor(example).sum())`
- `x == x`，不等于就是`nan`
  - 从而也可以`np.where(nparray == nparray)`
# 表现
- 只要一个地方`nan`，整个训练loss就`nan`了没意义了（参考刚刚“求和”）
- 数据里有`nan`的表现
  - `model(data)`结果是`nan`
  - 但`model(torch.zeros_like(data))`不是（模型参数正常）
# 原因
## [[trivial-mistakes-in-algo#zero division]]
- 比如[[normalization]]时没有考虑方差为0的情况（没有给$\sigma$强行加一个小的$\epsilon$），出现$0/0$
- 比如出现0个数据求均值
  - 参考[[finetune]]的例子
- 注：$1/0$是`inf`不是`nan`
## $\infty - \infty$
## [[backward]]
- [[deep-learning/optimization#BGD, SGD, MBGD]]
  - 而不是Adaptive的[[deep-learning/optimization#Adam]]等
  - 可能出现[[gradient-issue#爆炸]]，导致出现nan
## 本来就有
- 实际问题中本来就有
- 新建[[series-dataframe]]时默认
  - 可能需要[[fillna]]填0等
## [[trivial-mistakes-in-math#范围]]
- [[time-series]]处理中得到
  - `diff()`
  - [[rolling]]
# 处理
- [[dropna]]
- [[fillna]]