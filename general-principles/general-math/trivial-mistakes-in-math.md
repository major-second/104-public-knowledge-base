- 参考
  - [[trivial-mistakes-in-algo]]
  - [[general-principles/special-case]]
# 范围
- 有时：“定义域”
  - 定义域内才有意义
  - 如[[nan#原因]]中的例子
## 非负
- [[markov-chebshev#Markov]]要求非负随机变量
- $1/x$积分是$ln|x|+C$，考虑负值情况
- $e^x-1-x-x^2/2$只有当$x\ge 0$才是恒非负
## 挖去坏点
### 非零
- $\int 1/x \cdot dx =ln|x|+C,x\ne 0$
- $\int tanxdx = -ln|cosx|+C,x\ne \pi/2+k\pi$
- [[trigonometric-equalities#辅助角公式]]中$\phi$表达式
# 单双侧
- 参考[[symmetry#翻转]]
- 差2倍
- [[look-up#normal]]
- [[concentration]]
- [[hoeffding#main contents]]
# 开根号
- [[variance]]和标准差
  - [[standard-error]]
  - [[variance#可加性]]中，[[iid]] $N$个，标准差是变为$1/\sqrt N$量级，不是$1/N$