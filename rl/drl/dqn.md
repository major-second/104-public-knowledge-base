- 前置：[[q-learning]], [[deep-learning-basics]]
- [参考](https://zhuanlan.zhihu.com/p/110620815)
- 在[[q-learning]]中
  - 维护Q table，即$S,A$组合得到$Q$值
  - 更新目标：如对q-learning，$Q(S,A)$的更新目标是$R+\gamma max_a Q(S',a)$
  - 在那里，直接把表中相应元素$Q(S,A)$变成$Q(S,A)+\alpha(目标-Q(S,A))$即可
- 现在对于连续[[spaces]]情况
  - 无法列表，而使用神经网络作为函数$Q$
  - 更新时也无法更新单个点，而是把$目标-Q(S,A)$作为loss传给神经网络的[[deep-learning/optimization]]
# 拓展
- [参考](https://zhuanlan.zhihu.com/p/110769361)
- experience replay: 把之前state, action, next state, reward, done都存起来，以后可以不断回放，即可使用更多数据
- fixed Q-targets: 简单地[[general-principles/recursion]]可能造成不稳定等，故$max_a Q$那个$Q$作为target，定期从正在训的Q网络中复制过来。不训target