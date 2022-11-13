## 参考
- [一篇知乎技巧trick总结](https://zhuanlan.zhihu.com/p/95081141)
- [正则化总结](https://zhuanlan.zhihu.com/p/69025058)
## 列举和评论
### 正则化
- 原理参考[[2-eval]], [[overfit]]等
- early stop（即：看验证集，别等验证集loss回升了才停）
  - 其实践参考[[tensorboard]], [[checkpoint]]等
- 增加正则化惩罚项作为损失函数
  - 参考[[11-feature-selection]]中LASSO，岭回归
  - l1: 可以导致稀疏性
  - l2
    - 类似岭回归。比较常见一般的罚项
    - 由于$x^2$导数正比于$x$，所以最简单的情况，weight decay和l2正则化损失是对应的
      - 当然，对于复杂一些的优化器如Adam就不一定了
      - 参考[[deep-learning/optimization]]
      - torch实践：在[[basics/optimization]]中实现，如`SGD(其它参数, weight_decay=1e-2)`
### 结构
- 以2的倍数为间隔调MLP隐层宽度
### [[feature-engineering]]
- 对input做winsorization缩尾（参考[[12-robust]]）
  - 例如暴力看[[quantile]]，把极端值clip一下
  - 有时对线性和对MLP都能提升，但是对MLP提升多。推测可能是MLP需要数据的某种“密度”大，因此input极差大自然会boil
- input整体的normalization（当然要使用**训练集**的mean, std）
  - 注意小心极差/标准差极大的维度，做了反而不行（所以要和winsorize结合）