- 参考[[2-eval]], [[overfit]]
- 可以用train, val, test上性能差异量化
  - 正式训练前可以搞几个toy models进行某种层面[[general-programming/debug]]，看看数据量和“密度”是否达到要求
# covariate-shift
- [参考](https://zhuanlan.zhihu.com/p/339719861)
- 相比一般domain gap，这个是条件分布不变，输入分布变
- 不同batch之间：[[batchnorm#internal-covariate-shift]]