- 前置
  - [[monte-carlo]]
  - [[q-v]]
- 参考
  - https://zhuanlan.zhihu.com/p/109755443
  - https://zhuanlan.zhihu.com/p/110118392
  - https://zhuanlan.zhihu.com/p/110132710
- 怎么获得$v$值？
1. 原始定义[[dp]]逐步往前倒推。缺点：计算量过大、必须完全已知环境等
2. 从一个状态开始[[monte-carlo]]，随机采一堆
  - 每个trajectory都要停了才得到数值。这是个缺点
  - 具体更新$V$的公式$V \leftarrow V + \alpha(G-V)$，可以理解成$G$是一些新的采样，估计$V$是所有采样的值平均也就是之前$V$和之后$G$的（加权）平均
3. TD
  - 不用走到最后！过程中的$V$就可以估计最终采样结果$G$，从而用来更新
  - 相比MC方法，更新公式变为$V(S_t) \leftarrow V(S_t) +\alpha(R_{t+1} + \gamma V(S_{t+1}) - V(S_t))$
  - 其实有[[self-similarity]]，[[general-principles/recursion]]等思想