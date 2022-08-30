## 参考
- [一篇知乎技巧trick总结](https://zhuanlan.zhihu.com/p/95081141)
## 列举和评论
### 动力学
- early stop（看验证集，别等验证集loss回升了才停）
  - 原理参考[[2-eval]], [[overfit]]
  - 实践参考[[tensorboard]], [[checkpoint]]等
### 结构
- 以2的倍数为间隔调MLP隐层宽度
### [[feature-engineering]]
- 对input做winsorization缩尾（参考[[12-robust]]）
  - 例如暴力看[[quantile]]，把极端值clip一下
  - 有时对线性和对MLP都能提升，但是对MLP提升多。推测可能是MLP需要数据的某种“密度”大，因此input极差大自然会boil
- input整体的normalization（当然要使用训练集的mean, std）
  - 注意小心极差/标准差极大的维度，做了反而不行（所以要和winsorize结合）