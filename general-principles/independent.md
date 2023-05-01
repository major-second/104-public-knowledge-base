- 把总体拆成独立的各个部分，各个部分都可独自变动
# 数学中
- 集合的笛卡尔积。其元素个数等于各集合元素个数乘积
- 概率论中的[[1-prob/independent]]
  - 进一步：机器学习中的“独立”样本。不独立的样本可能导致leakage，效率降低等。但神经网络等数据需求量大的往往还是用不独立样本，例如[[rnn]]
- [[orthogonal]]
## diagonal
- 独立的表现形式往往是矩阵的对角/分块对角
- 举例
  - 矩阵求逆：对角/分块对角的逆
    - 就不用跑原始很慢的$O(n^3)$算法
  - $x^T Ax$，$A$对角，则$x$不同部分没有entanglement，就是某种独立
  - [[deep-learning/optimization#Adam]]相比[[deep-learning/optimization#二阶]]就是“对角”二阶信息，从而不是$O(n^2)$计算量
  - [[1-prob/independent]]时，[[fisher-information#参数是向量]]矩阵是对角阵，逆也好求，[[mle-delta-method]]也好算
  - [[volatility-for-portfolio]]中idiosyncratic return
# 程序/算法中
- 和“抽象”思想常相关
- 反面：[[leaky-abstraction]]，不正交
- 强化学习中[[dueling-dqn]]（网络结构）和**原始版本[[dqn]]、[[double-q-learning]]、[[double-dqn]]三种可能算法**正交
  - 这样$2*3=6$种方法