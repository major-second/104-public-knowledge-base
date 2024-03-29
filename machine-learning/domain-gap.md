- 参考[[2-eval]], [[overfit]]
- 可以用train, val, test上性能差异量化
  - 正式训练前可以搞几个toy models进行某种层面[[general-programming/debug]]，看看数据量和“密度”是否达到要求
- domain gap不大也可称为 homogeneity, 反之 heterogeneity
  - 联系：[[heteroskedasticity]]
# covariate-shift
- [参考](https://zhuanlan.zhihu.com/p/339719861)
- 相比一般domain gap，这个是条件分布不变，输入分布变
- 不同batch之间：[[batchnorm#internal-covariate-shift]]
- 一个例子：
  - $A(-3,4),B(-4,3),C(3,-4),D(4,-3)$
  - 则$ABABABCDCDCD$，看前6或总共12，[[correlation]]不同。也导致“不能泛化”，out-of-sample decay等
  - 本质就是covariate shift
  - 参考[[stationary-processes]]
# [[tradeoff]]
- 数据量小：显然“集中”，密度大，gap小，资源占用小（有时这是硬约束）
- 数据量大：数据量大本身可训练更复杂模型