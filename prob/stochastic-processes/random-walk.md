- 定义
  - [[iid]]随机变量列$z_i$，而$Z_n = \sum_{i=1}^n z_i$
- 前置
  - [[停止法则]]
# Wald引理
- $EZ_\tau = EZ_1\cdot E_\tau$
- 证明的核心：$I(\tau\ge i)$和$z_i$相互独立（因为“未来”了）
  - 所以$Ez_i^+= EI_{\{\tau\ge i\}}\cdot z_i^+$（因为如果$\tau< i$则显然$z_i=0$）
  - $^+$意思是一个trivial的分正负的技巧，并不是核心思想
# gambler's ruin
- 赌徒和对方（无限筹码）赌，看何时输光
- 如果$p$（赢的概率）大于$\frac 12$则有概率无限增长不输光，否则概率1输光
# 物理模拟
- 如果正负对称，加一减一概率$p$，不动概率$r$，相当于离散版本[[brownian-motion]]
- 吸收态
- 反射态
## Ehrenfest model
- $P_{ij}=\frac{a-i}{2a},j=i+1$
- $P_{ij}=\frac{a+i}{2a},j=i-1$
- 两边反射，中间回复力
# 其它
$EZ_1=0,EZ_1^2<\infty,E\tau<\infty$则$EZ_\tau^2=EZ_1^2\cdot E_\tau$
- 还是$I(\tau\ge i)$和$z_i^2$相互独立
  - 且根据$EZ_1=0$及独立性得到交叉项为0
- 证明的另一个核心是“取极限”，技术细节略

Stein：$\tau^* = inf\{n:n\ge 1,Z_n\notin (a,b)\}$，则$P(\tau^*>n)\le Me^{-rn}$
- 核心是一次“打包”$m$个，这$m$个不能偏差太多才有可能不停止
  - 而这$m$个偏差太多的概率大于0
- 那么很多个“$m$个的包”，每一个都不能偏差太多，就形成了指数衰减

可以拓展到[[high-dimension]]