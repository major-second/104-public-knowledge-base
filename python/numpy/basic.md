`import numpy as np`
- `np.array([2])`这种得到`[2]`，但`np.ndarray([2])`得到`.shape`（形状）是`[2]`的数组（一维数组，2个元素）
- `np.concatenate((a, b))`，返回拼接结果，不改变`a`，`b`
  - 注意不要少打一对括号。
  - 元组当然可以大于2个元素
- `np.vstack`
  - 把`[(1,2),(3,4)]`变成`2*2`的
  - 把`np.ndarray((2,), dtype=object)`这类的变成正常的（类型为数值）的array