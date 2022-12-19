- 把总体拆成独立的各个部分，各个部分都可独自变动
# 数学中
- 集合的笛卡尔积。其元素个数等于各集合元素个数乘积
- 概率论中的独立。这被Durrett书称为“概率论之于测度论的开始”
  - 机器学习中的“独立”样本。不独立的样本可能导致leakage，效率降低等。但神经网络等数据需求量大的往往还是用不独立样本，例如[[rnn]]
- [[orthogonal]]
# 程序/算法中
- 和“抽象”思想常相关。反面：[[leaky-abstraction]]，不正交
- 强化学习中[[dueling-dqn]]（网络结构）和**原始版本[[dqn]]、[[double-q-learning]]、[[double-dqn]]三种可能算法**正交
  - 这样$2*3=6$种方法