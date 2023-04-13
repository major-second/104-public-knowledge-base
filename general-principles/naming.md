# 换元或简记
- 换元积分法
- 换元简化推导
  - [[hoeffding]]
- [[method-of-moments]]为了方便写出反函数，简记$k$阶矩为$V_k$
- 对换了的新元求导，如[[maximum-likelihood]]中[[normal]]
# 有名字作为交流基础
- [[self-similarity]]中设问题
  - 对于新定义，如果你适当定义可以简化问题，等价于不适当定义之后代数变形 [换元](#换元或简记)
    - [[4-probability#coupon collection]]拓展题
- [[induction]]中设命题
- 程序的flag
  - [[oi-wiki-stl/string]]中的`string::npos`
  - 自己写算法题常见的无意义值（如`-1`）
- [[normal#cov#corr绝对值期望]]中设一个分布$W$
# 程序中的命名
- [[2-naming]]
# convention
- "naming convention"
# 命名有时是相对的
- 没有严格的定义，定义相互转化
- 例如
  - [[factors-alphas]]
  - [[greedy]], [[dp]], [[q-learning]]
  - [[code-data]]
# exists
- 有时只要知道存在某个东西（数、向量、变量）等
  - 不需要具体知道是什么，也不需要求，也暂时求不出来
  - 但只需要知道他存在，就会很有帮助
- 例
  - [[广义逆]]中的$\forall \alpha, \exists \beta$
    - 不需要知道$\beta$具体是啥，但反正$(X'X)(X'X)^-X'\alpha - X'\alpha=(X'X)(X'X)^-X'X\beta - X'X\beta=0$
    - 于是$ (X'X)(X'X)^-X' = X'$
  - 微分中值定理的存在$\xi$，可用于证明很多关于“估计误差”的式子
    - 至少是误差量级吧
  - [[estimation#拉格朗日余项]], [[estimation#柯西余项]]
# 设常数
- [[integral-constant]]
- [[proportional]]