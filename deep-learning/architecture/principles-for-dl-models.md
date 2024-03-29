- 前置
  - [[eda]]
- 是否适用神经网络？选择什么模型？
# inductive bias
- 参考[[1-intro-NFL]]
- 个性
  - [[symmetry]]
  - [[equivariant-invariant]]
    - 平移：[[conv]]
    - 置换：[deep sets](https://zhuanlan.zhihu.com/p/612736617)
      - invariant: $y = f(g(x_1)+g(x_2))=f(g(x_2)+g(x_1))$
      - equivariant: $(y_1,y_2) = (y+g(x_1),y+g(x_2)), where \quad y = f(g(x_1)+g(x_2))=f(g(x_2)+g(x_1))$
    - SE(3)：*Leveraging SE(3) Equivariance for Learning 3D Geometric Shape Assembly*
  - 有了[[equivariant-invariant]]，可少做些[[augment]]
    - 否则你有inductive bias, underlying assumptions按道理就可以[[augment]]
- 共性
  - 神经网络本身具有inductive bias：利用non-[[linearity]]
    - 单变量自身
      - 例如[[1x1conv]]
    - 多变量entanglement
# 数据量
- 可以[[augment]]
- [[domain-gap]]
- [[SNR]]
- 某种“密度”
  - 所以可以[[preprocessing]]，[[12-robust]]