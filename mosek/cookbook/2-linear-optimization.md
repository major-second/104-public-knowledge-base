- 前置[[1-preface]]
[toc]
# Introduction
## Basic notions
- 关键词
  - linear constraints
    - linear equalities and inequalities
  - linear objective function
  - feasible set
  - matrix notation
  - The standard form of a linear minimization problem
    - $minimize\quad c^Tx, \quad s.t. Ax=b, x\ge 0$
    - 向量的$\ge$号表示逐个分量$\ge$
- 通过适当辅助变量[[reduction]]，可以包含$Ax=b, Ax\ge b, l\le Ax \le u$等情况
## Geometry of linear optimization
- 等式
  - hyperplane超平面
  - 线性空间陪集
  - “点斜式”$a^T(x-x_0)=0$
  - “斜截式”$a^Tx=\gamma$
  - 很多个写到一起变成$Ax=b$，其中$A$有$m$行则$m$个超平面相交
- 不等式
  - halfspace
  - $Ax\le b$，向量小于等于表示各个分量小于等于
  - polyhedron
- 几何直观：端点或棱或面……是最优
- 一些相对概念
  - nonempty / empty
  - feasible / infeasible
  - bounded / unbounded
# Linear modeling
## Maximum (piecewise linear)
- piecewise linear很多时候 $max\{a_i^T x+b_i\}$
- 而$max\{\cdots\} \le c$可以表示成一系列表达式都$\le c$
  - 反过来$\ge $不行，这涉及“凸”本质
- 可用piecewise-linear逼近一般凸函数
## Absolute value
$|x|\le t \Leftrightarrow -t\le x\le t$
## The $l_1$ norm
$||x||_1\le t\Leftrightarrow |x_i|\le z_i, \sum z_i=t$
- 应用：参考[[11-feature-selection]]中LASSO思想，优化 cardinality （非零有用维数）
  - 关键词
    - underdetermined linear system
    - basis pursuit
## The $l_\infty$ norm
$||x||_\infty :=max|x_i|\le t \Leftrightarrow -t\le x_i\le t$
### dual norms
- 定义：$||\cdot||$的对偶范数$||\cdot||_*:=max\{x^T v|||v||\le 1\}$
- 例子：[1范数](#the-l_1-norm), [无穷范数](#the-l_infty-norm)互为对偶范数
- 对偶两次回到自身
## Homogenization
- 是一种[[reduction]]技巧
- 我们用一维[[general-principles/special-case]]方便理解
  - 原问题$min\quad \frac{ax+b}{cx+d}\quad s.t. cx+d>0, Fx=g$
  - 核心：记$(cx+d)^{-1}=z$，就有$min\quad axz+bz\quad s.t. z>0, Fxz=gz$，再记$xz=y$
- [[reduction]]后不完全等价，因为平时的不等式（[参考](#basic-notions)）都是含等号的，也就是会把$z>0$改写成$z\ge 0$了
## Sum of largest elements
是一个特殊的linear optimization问题，其实只需关注$u_i \ge max\{x_i-t, 0\}$即可
# Infeasibility in linear optimization
优化之前，其实还先应关心是否至少有可行解
## Farkas’ lemma
- 回忆[basic notations](#basic-notions)，$x\ge 0$
- 因此左边各$x_i$系数全非正（形成的向量$A^Ty\le 0$），右边正（$b^T y>0$）将导致infeasible
- Farkas' lemma: 这是充要条件
- 关键点
  - $\{Ax|x\ge 0\}$ is a closed convex cone
  - hyperplane passing through 0，几何意义上也就是$y^T b =0$，那么可以把点和锥分开
  - certify this fact (infeasibility) by providing a certificate of infeasibility
## Locating infeasibility
刚刚那个$y$可以有很多个分量为0，也就是问题很小的一部分已经造成了不可行，能给出certificate了