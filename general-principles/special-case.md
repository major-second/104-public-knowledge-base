- 数学中
  - [[6-serial/basics]]的$\tau\equiv 0$情况
  - [[2-2-calculus-ode]]
  - [[5-brownian-motion-and-stochastic-calculus]]
- 算法题的[[algorithm/special-case]]
- 实际程序也有特例！
  - 参考[[general-principles/debug]]
  - [[finetune]]中的例子：取一段区间内的数据做[[regression]]
    - 首先，有可能取出0条数据，导致[[regression]]报错
    - 其次，那当中的“区间外”部分可能是0条，导致出现`0/0`的[[nan]]
  - [[batchnorm]]中的例子：一般都是线性，bn，激活函数。但对于简单的[[mlp]]，切记最后一层（很有可能）直接线性就行，不要再加bn和激活函数了
    - 否则现象可能是训练不正常，loss无法正常下降，因为结果强行做了batchnorm