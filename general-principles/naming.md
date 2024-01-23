[toc]
- 程序中的命名
  - [[2-naming]]
  - [[object-oriented#override-overload-overwrite]] overload
# 换元或简记
- 换元积分法
- 换元简化推导
  - [[hoeffding]]
- [[method-of-moments]]为了方便写出反函数，简记$k$阶矩为$V_k$
- 对换了的新元求导，如[[maximum-likelihood]]中[[normal]]
- [[pdf-transform]]
- [[first-order-linear#常数变易法]]
  - [[poisson-process]]
  - [[pure-birth-process]]
## 一般换什么
- 根号下
  - $cos(\sqrt{1-\sqrt{x^2+5x+7}}+\sqrt{x^2+5x+6})=cos(\sqrt{1-t}+\sqrt{t^2-1})$
    - $t\ge 0,t\le 1,t^2\ge 1,t=1$
- 分母
  - $\frac{x^2+y^2+2(x+1)(1-y)}{x-y+1}=\frac{(x-y)^2+2(x-y)+2}{x-y+1}=t+1/t,t=x-y+1$
## 三角代换
- 刚刚是“被动技能”，现在往往是“主动技能”
  - 请熟悉[[trigonometric-equalities]]，特别是[[trigonometric-equalities#六边形图]]
- $abc+a+c=b$
  - 先排除[[general-principles/special-case]] $ac=1\Rightarrow a+c=0$无解
  - 故$b=\frac{a+c}{1-ac},tan\beta = tan(\alpha+\gamma)$
  - $\frac 1{1+a^2}+\frac 1{1+c^2}-\frac 1{1+b^2}=cos^2\alpha+cos^2\gamma-cos^2(\alpha+\gamma)$
  - 此时可以考虑初等地二倍角等等
  - 或者直接[[monotonous]]求导要求$sin2\alpha=sin(2\alpha+2\gamma)$
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
- 循环变量命名常用`i, j`，未知数用$x$，[[binary-search]]命名上下界用`ub, lb`或`hi, lo`
- [[pep8]]这类规范
## 约定俗成
- 数学：未知数用$x,y$，参数用$\theta$，已知数用$a,b$，复数用$z$等
- 物理：时间用$t$，长度用$L$……
- [[2-naming]]计算机中：循环变量`i`，python对象私有属性约定`_`开头，`CamelCase`，`snake_case`
- 领域缩写：IB, VC, PE, FA...
  - [参考](https://zhuanlan.zhihu.com/p/42090782)
- 计算机：[[numpy-indexing#row and column]]
## 历史遗留
- https://www.zhihu.com/question/276016774/answer/385381844
  - [[heap-堆区]]和[[heap]]的关系
## 有误导性
- 可能让人误解，但是不是命名的锅，是你自己水平不够
  - [[non-parametric]]，英文名non翻译成中文非
  - 然而如果你中文水平不行，会以为非参数是“无参数，参数维数为0”，实则不是。反而是维数接近无穷
- 历史原因，命名稀烂，约定俗成了就一直这样
  - [[unary]]“最小二乘法”，直接翻译自日文汉字，所以“二乘”非常不好，容易误解为$2\times$
  - [[type-i-ii-errors]]，数字区分，根本没任何信息量，只是为了区分而区分
    - 哈哈你自己不能干这个事，比如`if case1`
      - [[2-naming]]
# 命名有时是相对的
- [[spectrum]]
- 没有严格的定义，定义相互转化
- 例如
  - [[factors-alphas]]
  - [[greedy]], [[dp]], [[q-learning]]
  - [[code-data]]
  - [[dimensionless#无量纲是相对的]]
- 换个名字，变相，逃避监管
  - [[senior-mezzanine-equity-优先-劣后-夹层]]
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
## exists extreme value
- 设最大最小
  - 逻辑：反正都存在，你为啥不取最值设个字母？
  - 设了之后可以有额外性质
- [[gcd-lcm]]
- [[指数#应用]]设“最小素因子”
# 设常数
- [[integral-constant]]
- [[proportional]]
# 凑形式
## 凑形式设函数
- 设某个东西为$f$，然后$f$出现不止一次，用于单调性比较大小或取等……
- 结合[[monotonous]]
  - [[trigonometric#symmetry]]例题
  - [[trigonometric-inequalities#trigonometric#几何意义]]例题
## 裂项
- $f(n)=g(n)-g(n-1)$，是特殊的凑形式
- $\frac 1{n(n+1)}$
- $\frac 1{n(n+1)(n+2)(n+3)}$
- $\frac 1{cosncos(n+1)}\Rightarrow \frac{sin(n+1-n)}{cosncos(n+1)}=tan(n+1)-tann$
  - 不过注意[[general-principles/special-case]]，0等
- $arcsin\frac{\sqrt{(n+1)^2-1}-\sqrt{n^2-1}}{n(n+1)}=arcsin \frac 1n - arcsin \frac 1 {n+1}$
  - 两边求sin，通过[[trigonometric-equalities#和角公式]]证明