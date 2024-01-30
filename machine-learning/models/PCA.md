- 前置
  - [[eigenvalue]]
  - [[variance]], [[MSE]]
  - [[dimensionality-reduction]]
  - [[orthogonal-decomposition]]
- [参考](https://zhuanlan.zhihu.com/p/342129669)
  - 注意假设了高[[SNR]]，[[variance]]大的认为有信息，而非噪声
- 举例：测试数据生成
  - ```python
    pc_0 = np.random.rand(100)
    pc_1 = np.random.rand(100)
    pc_2 = np.random.rand(100)
    x = pc_1 * .1 + pc_2 + np.random.rand(100) * .01
    y = pc_1 * .1 - pc_2 + np.random.rand(100) * .01
    ```
- Test results
   - The first principal component should align more closely with `pc_2`, as `pc_2` contributes more to the variance of `x` and `y`.
   - The second principal component should be orthogonal to PC1 and thus align more closely with `pc_1`, as `pc_1` and `pc_2` are independent and thus orthogonal.