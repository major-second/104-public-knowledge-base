- 单边情形下（统计量$\phi$大于某$C$就否定）样本值$x$
  - $\alpha$：对于所有接受域里的$\theta$，统计量大于某值$C$的概率小于等于$\alpha$
  - $p$：对于所有接受域里的$\theta$，统计量大于$\phi(x)$的概率小于等于$p$
    - 所以在好的情况下，否定的充要条件就是$p$值小于$\alpha$
    - 甚至可以先计算$p$，再指定合适的$\alpha$
    - $p$值低，和$H_0$相容程度低（“古怪”）。$p<\alpha$拒绝，引起错误概率不超过$\alpha$
  - 也可以理解成：拒绝某个点所需最小的可能[[power-level#水平]]
    - 回忆：[[power-level#水平]]越小越好
- 双边情形$p$值就更有人为定义的意味。还是所有接受域里的$\theta$，统计量大于$\phi(x)$的概率小于等于“某”。但这个“某”要$*2$，再看是否超过1. 这就显得很人为
  - 注意要通过估计、常识等，判断“是在哪边”