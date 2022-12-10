- 前置[[q-learning]]
- [[q-learning]]的[[estimation]]：高估了
  - q-learning中，我们本意想找到最大的那个$Q$，也就是$Q$的最大值，估计（量）期望的最大值
  - 但实际中是计算估计（量）的最大值
  - 参考[[estimation]]，这高估了
    - 即：**多个随机变量估计（量）的最大值期望**近似作为**估计（量）期望的最大值**
    - 这里的**多个**在强化学习中实际意义是多个可能action
  - 后果：$Q$越更新越高估，影响性能
- [double q-learning](https://paperswithcode.com/method/double-q-learning)
  - 不直接使用$max_a Q$，而是两个$Q$，且每次“交错”，用其中一个网络argmax得到$a^*$，用另一个网络计算$Q(s',a^*)$
  - ![](double-q-learning.png)
    - 注意对应两个网络，有两种可能情况
  - 有两个要点
  1. 首先是“顺序”问题。即先选定action，再出值，而不是先出所有值，再挑一个最大的。如果这样选第一步总是选出正确的$a^*$扔给第二步，那结果就是估计（量）期望的最大值，无偏
  2. 在此基础上，第一步不一定每次选对，那就低估
- 加深理解：一个退化[[general-principles/special-case]]：所有随机变量iid
  - 则baseline方法（称为single estimate）高估了
  - 现在的方法（称为double estimate）无偏
    - 显然。因为第一步计算$a^*$实际上取什么都没区别