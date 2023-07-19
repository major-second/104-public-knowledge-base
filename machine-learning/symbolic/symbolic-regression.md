- [wiki](https://en.wikipedia.org/wiki/Symbolic_regression)
# [[genetic]]
# bayesian
- 前置[[bayesian-inference]]
- [bayesian](https://arxiv.org/pdf/1910.08892.pdf)
  - 说一个词你就大概懂了：prior of tree structure
# neuro
- [Neural Symbolic Regression that Scales](https://arxiv.org/pdf/2106.06427.pdf) survey
  1. 把[[activation]]直接换成符号，例如`+, sin, exp`
     1. 显然不本质，需要太多先验，[[gradient-issue]]
  2. [[encode-decode]]到连续空间, [[VAE]]
     1. [Grammar variational autoencoder](http://proceedings.mlr.press/v70/kusner17a/kusner17a.pdf)
- [neuro](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7159912/pdf/aay2631.pdf)
  - [[deep-learning-basics]]用在哪了？
  - 相当于超级“插值”interpolate方法，给出函数取值再寻找[[symmetry]]等等好性质
  - 这里就有“物理学中常见哪些对称性”这种inductive bias