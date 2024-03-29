# Random Walk
- 第$n$个随机变量是$n$个i.i.d.随机变量求和
- 随机变量$p$为1其余$-1$：simple
- 随机变量一半为1一半-1：symmetric
  - 其期望方差等都很好求，用一些基础的[[variance]]计算技巧
# martingale
- 任何时刻绝对值期望有限
- 下一时刻（从而归纳得未来任意时刻）期望是当前值
  - [[4-probability]]中basketball scores就是
- 对称随机游走，$S_n, S^2_n-n$都是（后者只要条件化一下就看出来）
## 停止
- stopping rule：只看前面时间的各个事件就能确定的正整数随机变量
  - [[6-serial/basics]]也提到
- wald's equality
  - $ES_N = EXEN$
  - 全期望公式！
  - 也可以考虑$E[X_nI_n] = E[X_n]E[I_n] = E[X]E[I_n]$，本质差不多
  - 注意条件：随机游走即可成立，不一定是鞅，不一定对称
- 在一定stopping rule标准停下的鞅还是鞅
  - 直观上也是全期望公式显然
## drunk man
  - 算概率
    - 法一：直接说出：$a_i = \frac{a_{i-1}+a_{i+1}}2$，所以从0到1等差数列，于是答案显然
      - 这个也可以用[[5-markov-chain]]理解
    - 法二：刚刚说过的martingale在一定停止规则下也是martingale，所以直接“杠杆原理”反比
  - 算步数期望
    - 法一：可以[[5-markov-chain]]
    - 法二：$S_n^2-n$是鞅
- dice game
  - 是随机游走，不是鞅，但wald's equality仍成立，$7/2*2$
## ticket line
  - has no change没零钱
  - 联想括号串
    - [[32-longest-valid-parentheses]]，[[22-generate-parentheses]]
  - [[reflection-principle]]，一一对应思想
    - 经过了-1最终到0的，一一对应最终到-2的
## coin sequence
  - 法一：[[5-markov-chain]]结合[[induction]]
    - 用到[[general-principles/recursion]]思想：不具体管怎么到倒数第二步的
  - 法二：鞅
    - 每次投掷加入一个赌徒，每个赌徒都是连续翻倍下注，连续n个才赢$2^n$，否则任何情况赌注都无了
    - 所以total bankroll每轮期望稳定加一，$x_i-i$是鞅
    - 停下时奖池内数量$Ex_i$固定，所以可算出$Ei$
    - 可以拓展到一般序列
    - 参考[[3-prob]]题8，9