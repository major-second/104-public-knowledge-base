- 前置[[markov-chain]]
- 定义：任何时候成功加一概率$q_n$，失败减一概率$p_n$
# expected rounds to success
- 硬币连续丢出10个正面需要多少次？
  - [[induction]]
  - [[general-principles/recursion]]
  - $p_i=q_i=\frac 12$
  - $E_{10}=0$
  - $E_{9}=1+\frac 12(E_0+E_{10})=\frac 11+\frac 12 E_0$
  - $E_{8}=1+\frac 12(E_0+E_{9})=\frac 32+\frac 34 E_0$
  - $E_{7}=\frac 74 +\frac 78 E_0$
  - $\cdots$
  - $E_{0}=\frac {1023}{512}+\frac{1023}{1024}E_0$
- $E_0=2046, E_1=2044, E_2=2040\cdots, E_{10}=0$
- 拓展：参考[[poisson-process#例题]]