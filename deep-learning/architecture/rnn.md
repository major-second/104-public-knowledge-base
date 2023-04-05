- [参考](https://zhuanlan.zhihu.com/p/30844905)
- 为了简单理解，先不考虑bias
- $O_t=g(V\cdot S_t)$
- $S_t = f(U\cdot X_t + W\cdot S_{t-1})$
- 其中$X$是输入，$S$是隐层
- 实际应用中有时只需要最后一个$O_t$“总结”整个序列的情况
# 对比
- 相比[[conv]]，更明确地利用了时序
- [[conv]]虽然假设[[symmetry#平移]]，但本质上还是只利用了“距离”远近确定哪些点一同出现在哪些[[conv]]处，没有显式利用时序
  - 但[[conv]]可以容易 [并行](#parallelizing)
# parallelizing
- S (Sliced) RNN：切成子序列，逐层上报，不再是原始rnn的“扁平”结构
  - [参考知乎](https://zhuanlan.zhihu.com/p/42242327)
  - [原文](https://arxiv.org/ftp/arxiv/papers/1807/1807.02291.pdf)
- 基于[[parallelism#并行计算算法]]的
  - [参考](https://openreview.net/pdf?id=HyUNwulC-)