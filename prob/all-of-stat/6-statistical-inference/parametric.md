- 前置[[statistical-inference]]
- 要推断$F$，$F$有个范围
- 范围可以用有限个参数表示，例如[[multi-normal]]：参数模型
  - 记号：$\mathbb E_\theta, \mathbb P_\theta$等，表示某个确定的参数$\theta$下某某
- 不能，比如所有可能的[[random-variable-functions#cdf]]：非参数模型
  - 如[[分布函数估计]]
    - 非参地估计出$F$，从而估计统计泛函statistical functional $\mu = \int xdF$
  - 参数太多了，无限维，没有信息[[encode-decode]]压缩过程