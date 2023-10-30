---
title: sliced score matching
type: knowledge
---
# motivation
以前的 [[original score matching]] 方法：采样计算score function的海塞矩阵(Martens et al., 2012)，开销非常大！限制只能使用低维数据；approximate backpropagation(Kingma & LeCun, 2010), denoising(Vincent, 2011)参数估计不一致，估计方差大，实现繁琐
我们的sliced score matching方法, 把高维的score场往随机方向投影之后再去比较(scalable!)，极大程度减小了开销(只需计算Hessian向量积)，使得能用在高维数据上！并且估计是一致、渐进正态的。

关于Hessian向量积：https://justindomke.wordpress.com/2009/01/17/hessian-vector-products/

# sliced #score_matching
基本思想：如果待优化的梯度场和目标梯度场是一样的，那么任何方向的投影都应该是一样的！而某一个方向的投影是个标量场，很容易优化！

