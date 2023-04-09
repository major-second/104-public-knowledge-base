# 联系
- [[general-principles/recursion]]
- [[induction]]
- [[reduction]]
- [[dp]]
- 从[[general-principles/special-case]]到[[forall]]的思想常用
- [[5-markov-chain]]
# 例子
- 强化学习[[calculate-v]]中TD方法也是类似思想
  - 利用自相似（转变完后下一步的$V$）
  - 相比MC方法，不需要走到出口！
- [[q-learning]]也是
  - 这个递归不是“完美”的，而是“略有差别”，即取了下一步的最大的$Q$
  - 进一步地，为了防止不稳定，可以使用fixed Q-targets
# 例题
1. [[jane-street-introduction]]色子题
2. [[poisson-process]]到2爆仓题
    - $F(x_0,2):=一次取数取到之间=e^{-x_0}-e^{-2}$
    - $P(x_0,2):=加和至少一次取到之间=F(x_0,2)+\int_0^{x_0}e^{-x}P(x_0-x,2-x)dx$
    - $Q(x):=P(x_0-x,2-x)=e^{x-x_0}-e^{x-2}+\int_0^{x_0-x}e^{-t}P(x_0-x-t,2-x-t)dt=e^{x-x_0}-e^{x-2}+\int_0^{x_0-x}e^{-t}Q(x+t)dt=e^{x-x_0}-e^{x-2}+\int_x^{x_0} e^{x-r}Q(r)dr$
      - 从$P(x_0,2)$到$P(x_0-x,2-x)$泛化：必须！参考[[forall]]
    - $Q'=e^{x-x_0}-e^{x-2}-Q(x)+\int_x^{x_0}e^{x-r}Q(r)dr=0$
    - $Q=const$（无后记忆性），$待求=Q(0)=Q(x_0)=1-e^{x_0-2}$
3. 轮流取数
   - A, B take turns to pick number from $U[0,1]$
   - the game stops when the sum of all picked numbers is >1
   1. Expected value of rounds?
       - $E(1)=\int \rho(c)\mathbb E(总和|a_1=c)dc=\int (1+E(1-c))dc$
       - $E(x)=\int_0^x(1+E(1-c))dc+(1-x)*1=1+\int_{1-x}^1E(c)dc$
         - 从$E(1)$到$E(x)$泛化：必须！这就是[[forall]]思想
       - $E'_x(x) = E(1-x)$
       - $E(1-x)=f(x),f(x)=-f'(x),f(x)=Ae^{-x},E(x)=A'e^x,E(0)=A'=1,E(x)=e^x,E(1)=e$
   2. the last one picked will win. what is P(A win)?
        - $P(x):=剩余x,当前的人赢概率$
        - $待求=P(1)$
        - $P(x)=(1-x) + \int_0^x (1-P(x-c))dc=1-\int_0^x P(x-c)dc=1-\int_0^x P(c)dc$
        - $P'_x = -P, P(x)=Ae^{-x},P(0)=A=1,P(x)=e^{-x},P(1)=e^{-1}$
4. [[5-markov-chain]]中，“达到某吸收态的概率”
5. [[2-2-calculus-ode]]中一大堆自相似（极限题、积分题都有）
6. [[high-dimension#单纯形]]