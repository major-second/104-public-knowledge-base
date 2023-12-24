- 参考
  - [[functional-programming]]
  - [[parallelism]]
- 实例
  - [[numpy-basics]]
    - [[apply-along-axis]]
  - [[tensor-calculator]]
  - [[pandas/installation]]
    - [[pandas-apply]]
- 可能造成思维上麻烦，操作的局限，不细粒度
  - 这时可考虑[[numba]]等
# 实际性能
- [编译中的向量化优化](https://blog.csdn.net/qq_36287943/article/details/105202721)
- SIMD (Single Instruction, Multiple Data)
# 综合应用例题
- [[manipulation]]和[[indexing]]综合应用例题
  - 需求
    - 输入形如`i = torch.tensor([[1,0], [1,1], [0,1]])`
    - 输出`3 x 3`矩阵（`i.shape[0]`是3）
    - `i[0], i[1]`有（至少）一个共同的1，故输出矩阵的`[0, 1], [1, 0]`位为1
    - `i[1], i[2]`同理
    - `i[0], i[2]`没有共同的1，故输出矩阵`[0, 2], [2, 0]`为0
    - 特判：输出矩阵对角线为0
  - 一种解法：
    - 此处`r`表示row，`c`表示column
  ```python
  def f(i):
      n = i.shape[0]
      matrix = torch.zeros(n, n)
      true_r, true_c = torch.where(i)
      p = true_c.shape[0]
      c_mask = true_c.reshape(p, 1).expand(p, p) == true_c.expand(p, p) - torch.eye(p)
      c_mask_true_r, c_mask_true_c = torch.where(c_mask)
      r_repeat_r, r_repeat_c = true_r.reshape(p, 1).expand(p, p), true_r.expand(p, p)
      r_enumerate = torch.cat((r_repeat_r.unsqueeze(2), r_repeat_c.unsqueeze(2)), 2)
      indices = r_enumerate[c_mask_true_r, c_mask_true_c]
      r_indices, c_indices = indices[:, 0], indices[:, 1]
      matrix[r_indices, c_indices] = 1
      return matrix
  ```
- 实际需求：统计连续出现的数字
  - [[ffill-bfill]]
  - ```python
    import numpy as np
    import pandas as pd

    def get_continuous(arr):
        len_arr = len(arr)
        raw_cumsum = np.arange(len_arr) + 1
        staircase_init_points = np.where(arr[:-1] - arr[1:] != 0)[0] + 1
        staircase = np.zeros((len_arr,))
        staircase[staircase_init_points] = raw_cumsum[staircase_init_points] - 1
        staircase = pd.Series(staircase).replace(0, np.nan).ffill().replace(np.nan, 0)
        return raw_cumsum - staircase

    arr = np.array([1, 1, 1, 2, 2, 1, 1, 3, 3, 3, 3])
    print(get_continuous(arr))

    arr = np.array([1, 1, 1, 1, 2, 1, 2, 2, 2, 3, 2, 3, 3])
    print(get_continuous(arr))
    ```