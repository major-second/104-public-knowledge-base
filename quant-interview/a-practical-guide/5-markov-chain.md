- 参考[[markov-chain]]
- 前置[[4-probability]]
# 基础
- 初始分布，转移矩阵（转移图）
- 路径的概率$P(X_1=i_1,\cdots,X_n=i_n|X_0=i_0) = p_{i_0 i_1}\cdots p_{i_{n-1}i_n}$
- 本章考察有限状态
  - homogenous（转移矩阵不变）
    - 这并不是[[stationary-processes]]的意思！
# 状态分类
- accessible from, communicate
- recurrent：对于所有出去的（直接或间接可达到的），都有可能回来
  - 所以容易证明无穷步后几乎一定回来（核心：“指数衰减”）
- transient：有的出去了回不来
  - 是recurrent的反面
  - 所以无穷步后有非零概率不回来
- absorbing：永远不动了就在这
  - Absorbing MC: 有一个absorbing state，且其它都能过去（access）
  - 从一点出发，到某个absorbing state的概率？
    - 该点如果是absorbing state则显然
    - 根据定义该点显然不是recurrent，一定是transient
    - 对transient的，最终能到达某absorbing state概率：利用自相似[[self-similarity]]，[[general-principles/recursion]]列方程
    - 这里用了全概率公式[[bayes-theorem#total-probability]]分类讨论的思想！
  - 到达吸收态的次数期望：也是类似地列方程
# 问题
- gambler's ruin problem
  - 其实你只会自相似列方程就能做
  - 理解马尔可夫更清晰
- dice question
  - 画图很清晰！
  - “开始”是初始状态（和刚刚一题相比，这里的初始态之后不再出现）
  - 游戏结束当然是吸收态
- coin triplets
  - part B脑筋急转弯！必须连续三个H不出现T，才是HHH先
  - part C：比较麻烦
    - 有一个直觉：总是让自己的（长度为2）后缀是A的前缀
    - 直觉：“获胜”关系不具传递性。所以B有后发优势
- color balls
  - 对称性，假设最后是某种颜色，那么其他颜色没有本质区别
  - 对称性得到$P(F_1|x_{k}=i) = i/n$（这个和刚刚反过来，假装它们不同颜色
  - 最后需要找规律[[induction]]