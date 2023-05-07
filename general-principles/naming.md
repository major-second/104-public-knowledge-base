[toc]
- 程序中的命名：[[2-naming]]
# 换元或简记
- 换元积分法
- 换元简化推导
  - [[hoeffding]]
- [[method-of-moments]]为了方便写出反函数，简记$k$阶矩为$V_k$
- 对换了的新元求导，如[[maximum-likelihood]]中[[normal]]
- [[pdf-transform]]
# 有名字作为交流基础
- [[self-similarity]]中设问题
  - 对于新定义，如果你适当定义可以简化问题，等价于不适当定义之后代数变形 [换元](#换元或简记)
    - [[4-probability#coupon collection]]拓展题
- [[induction]]中设命题
- 程序的flag
  - [[oi-wiki-stl/string]]中的`string::npos`
  - 自己写算法题常见的无意义值（如`-1`）
- [[normal#cov#corr绝对值期望]]中设一个分布$W$
# convention
- 约定俗成
  - 数学：未知数用$x,y$，参数用$\theta$，已知数用$a,b$，复数用$z$等
  - 物理：时间用$t$，长度用$L$……
  - [[2-naming]]计算机中：循环变量`i`，python对象私有属性约定`_`开头，`CamelCase`，`snake_case`
  - 领域缩写：IB, VC, PE, FA...
    - [参考](https://zhuanlan.zhihu.com/p/42090782)
- 有时历史原因，命名稀烂，约定俗成了就一直这样
  - [[unary]]“最小二乘法”，直接翻译自日文汉字，所以“二乘”非常不好，容易误解为$2\times$
  - [[type-i-ii-errors]]，根本没任何信息量，只是为了区分而区分
    - 哈哈你自己不能干这个事，比如`if case1`
# 命名有时是相对的
- [[spectrum]]
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