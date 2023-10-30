# total-probability
- 前置
  - [[conditional]]
- 思想：[[set-operations#union]]，[[enumerate#分类讨论]]
  - 例题：$51$枚硬币比$50$枚正面多的概率：直接讨论第一枚是正是反。结果根据[[symmetry]]得1/2
# bayes-theorem
- 由[全概率公式](#total-probability)和[[conditional]]共同推出
- $P(A_i|B)(后验)=\frac{P(B|A_i)P(A_i)(这是先验)}{\sum_j P(B|A_j)P(A_j)}$
- 实际意义：如患病概率等