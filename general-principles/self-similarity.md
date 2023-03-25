# 联系
- [[general-principles/recursion]]
- [[induction]]
- [[化归]]
- [[dp]]
- 从[[general-principles/special-case]]到[[forall]]的思想常用
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