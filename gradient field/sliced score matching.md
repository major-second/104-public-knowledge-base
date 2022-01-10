---
title: sliced score matching
type: knowledge
---
# sliced score matching
## motivation
以前的 #score_matching 方法：采样计算score function的海塞矩阵(Martens et al., 2012)，开销非常大！限制只能使用低维数据；approximate backpropagation(Kingma & LeCun, 2010), denoising(Vincent, 2011)参数估计不一致，估计方差大，实现繁琐
我们的sliced score matching方法, 把高维的score场往随机方向投影之后再去比较(scalable!)，极大程度减小了开销(只需计算Hessian向量积)，使得能用在高维数据上！并且估计是一致、渐进正态的。

关于Hessian向量积：https://justindomke.wordpress.com/2009/01/17/hessian-vector-products/
简而言之就是，