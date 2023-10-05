- 参考
  - [[归一化]]
  - [[naming]]
  - [[齐次性]]
- 先判断和什么成正比
  - 然后计算[[归一化]]系数
  - 可以直接[[待定系数法]]
- 重要符号：$\propto$，正比于
  - 其实相当于$y=Cx$这种，$C$为常数
  - 和[[naming#设常数]]一个新的常数是等价的方法
# 等车例题
- 人和车来都是[[poisson-process]]，常数分别是$a$和$b$，车上人数分布？
  - $P(n)\propto \int e^{-C(a,b)t}\cdot \frac{(D(a,b)t)^n}{n!e^{D(a,b)t}}dt$
  - 你不需要知道$C,D$是啥，只知道他们和$t$无关，这就是[[naming#exists]]思想
  - 参考[[gamma-function]]则$P(n)\propto \frac{\int (E(a,b))^nt^n e^{-F(a,b)t}dt}{n!}=(G(a,b))^nH(a,b) \frac{\Gamma(n+1)}{n!}$
  - 所以是[[nega-binom#geometric]]，不用具体算各种东西，先定性知道分布种类
  - [[待定系数法]]代一个[[general-principles/special-case]]，比如车上0个人就是车比人快
  - 根据[[poisson-process]]无记忆性，$P(0)=\frac{b}{a+b}=q(几何分布性质)$
  - $p=\frac a{a+b}$，分布列$\frac b{a+b},\frac {ab}{(a+b)^2},\cdots$