- 前置[[statistical-inference]]
- 参考[[encode-decode]]
- 要推断分布$F$，$F$有个范围
# [[parametric]]
- 范围可以用有限个参数表示，例如[[multi-normal]]
- 记号：$\mathbb E_\theta, \mathbb P_\theta$等，表示某个确定的参数$\theta$下某某
- 参数模型+无监督学习：混合高斯（聚类）等
# non-parametric
- 范围不能用有限个参数表示，比如所有可能的[[random-variable-functions#cdf]]
- 参数太多了，无限维，没有信息[[encode-decode]]压缩过程
- 如
  - [[empirical-distribution-function]]非参地估计出$F$
  - 从而估计统计泛函[[statistical-functionals]]$\mu = \int xdF$
  - [[bootstrap-in-stats]]估计[[standard-error]], [[confidence-interval]]