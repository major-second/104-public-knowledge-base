- 参考
  - [[discretize]]
  - [[general-principles/special-case]]
  - [[forall#微元]]
# 用离散理解连续
- [[random-variable-functions#discrete]]和[[random-variable-functions#pdf-continuous]]关系
- [[random-walk]]和[[brownian-motion]]
- [[poisson-process]]小数定律
  - [[nega-binom#geometric]]几何和[[gamma-distribution#指数分布]]
  - 此时参考[[bernoulli-binom]], [[poisson]]
- $y=x^3$这条线在$[0,1]$，$x$均匀，问[[cov#corr]]
  - $\rho = \frac{\overline{xy}-\bar x\bar y}{\overline {x^2}\bar x^2}$
  - 平均值当然可以用积分代替
- [[1-first-look]]第三题
- [[gamma-function]]和[[factorial]]关系
# 取整
- [[float]]有提到，[[停牌]]
- 100次投篮，第一次失败，总共90次成功，证明其中有一时刻成功率80%
  - 考察所有整5点，拉出一条“斜线”
  - 你实际的失败次数也拉出一条线，从1到10，根据[[介值定理]]得结论
# 实际应用
- [[dl-regression-classification]]讲过连续导致问题
- [[lob]] [[tick-size]]
- 朴素贝叶斯怎么处理连续特征
  - https://blog.csdn.net/u013597931/article/details/81705718
  1. 直接bin
  2. 建模做[[2-estimation]]如高斯
# 思维方式
- [[spectrum]]，程度问题，不是非黑即白
- 模糊数学：隶属度、命题正确程度
- “你需要多少钱财富自由”？可以是连续的函数，而不是一个threshold