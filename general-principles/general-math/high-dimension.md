- 前置
  - [[general-principles/special-case]]
  - [[recurrence]]
  - [[induction]]

[toc]
# 代数理解
- 纯代数理解高维。你想象不出四维（乃至三维）空间那也没关系
- 标量拓展到向量
  - [[normal]], [[multi-normal]]
  - [[2-linear-optimization]]中的
  - [[2-4-duality-in-linear]]中的
  - [[multivariate#transforms]]中从乘以某个导数（绝对值）变成某个雅可比行列式（绝对值）
- 向量拓展到矩阵
  - [[linear-transform#多元随机变量multivariate]]
- entanglement带来额外思维复杂度，且往往使得需要用矩阵书写
  - [[cov]]相比[[variance]]多了交叉项
  - [[jacobian]]交叉项
  - [[hessian]]交叉项
  - [[multi-normal]]的$(x-\mu)^T\Sigma^{-1} (x-\mu)$相比[[normal]]的$(x-\mu)^2/\sigma^2$
  - [[multi-mle-delta-method]]的$\sqrt{(\hat \nabla g)^T \hat J_n(\hat \nabla g)}$相比[[mle-delta-method]]的$|g'|\hat {se}(\hat \theta_n)$
# 几何理解
- 这个往往需要[[general-principles/special-case]]
  - 低维才能[[imagination]]
## 球
## 单纯形
- [[general-principles/special-case]]：三角形
- 体积：超立方体的[[factorial]]分之一
- 例题：写算法给出构成单纯形的顶点，不重不漏覆盖超立方体
  - 三维：从$(0,0, 0)$出发
  - $x=1,y=1,z=1$三个超平面，各自2个二维单纯形（三角形）
  - “打过去就行了”
  - [[self-similarity]]
## [[recurrence]]
### 超空间被超平面分
- 全超空间被$n$个超平面分成几块
  - 一维：$n$个点，分成几段
    - 0: 1
    - 1: +1
    - 2: +1
    - $\cdots$
    - $f(1,n)=n+1$
  - 二维：$n$条线，分成几块
    - 0: 1
    - 1: +1，其实是$f(1,0)$
    - 2: +2，其实是$f(1,1)$
    - 3: +3
    - $f(2,n)=\frac{n(n+1)}2+1$
  - 三维
    - 0: 1
    - 1: +1，其实是$f(2,0)$
    - 2: +2，其实是$f(2,1)$
    - 3: +4，其实是$f(2,2)$
    - 4: +7，其实是$f(2,3)$
    - $f(3,n)=\frac{(n-1)n(n+1)}{6}+n+1$
# [[general-principles/independent]]
- 利用[[general-principles/independent]]分解化简问题
  - [[fisher-information#参数是向量]]中
    - [[iid]]直接$I(\theta)$变为$nI(\theta)$
    - [[1-prob/independent]]不同分布那也是[[general-principles/independent#diagonal]]
- 不[[general-principles/independent]]会带来额外麻烦（entanglement）
  - 参考[[high-dimension#代数理解]]
# 其它
- [[symmetry#旋转]]可以看成高维的[[symmetry#翻转]]，从[[normal#symmetry#旋转]]可以看出