# 概述
- `nan`是一个特殊的**浮点数**，可以用
  - `float('nan')`（python原生）
  - `np.nan`（需要[[numpy/basics]]）表示
- 注：因此：对于原本是整数类型的地方，就没法手动设`nan`
# 检测
- 单个数是否是`nan`用`torch.isnan`或`np.isnan`看
- `np.any(np.isnan())`
- 求和
  - 例如对于二维张量，直接`sum(sum(tensor))`或者`tensor.sum()`
    - 如果有任何一个地方`nan`，结果就是`nan`
  - 当然，求和是`nan`还有可能是正无穷加负无穷，这时`np.any(np.isnan())`检测不到。其实不符合题意
- `numpy`、`pandas`、`torch`不同
  - `import numpy as np; import pandas as pd; import torch`
  - `example = np.array([[np.nan, 0], [1, 1]]); print(example.sum()); print(pd.DataFrame(example).sum()); print(torch.tensor(example).sum())`
# 表现
- 只要一个地方`nan`，整个训练loss就`nan`了没意义了（参考刚刚“求和”）
- 数据里有`nan`的表现
  - `model(data)`结果是`nan`
  - 但`model(torch.zeros_like(data))`不是（模型参数正常）
# 原因
- 数学操作
  - $0/0$
    - 比如手动做中心化标准化[[normalize]]时没有考虑方差为0的情况（没有给$\sigma$强行加一个小的$\epsilon$），出现$0/0$
    - 比如出现0个数据求均值
      - 参考[[finetune]]的例子
    - 注：$1/0$是`inf`不是`nan`
  - $\infty - \infty$
- 实际问题中本来就有
- [[time-series]]处理中得到
  - 例如`diff()`，[[rolling]]
- 比如[[deep-learning/optimization]]中选用SGD（非Adaptive的），可能出现[梯度爆炸](https://stackoverflow.com/questions/65654279/nan-values-with-sgd-optimizer-in-keras-for-regression-nn#:~:text=The%20NaNs%20in%20the%20loss%20function%20is%20mostly,long%20as%20you%20don%27t%20have%20a%20specific%20reason.)
# 处理
[[dropna]]