简单来说i.i.d.随机变量列$z_i$，而$Z_n = \sum_{i=1}^n z_i$
停止法则$\tau$：是随机变量，且是否大于$n$只由观测值$X_1,\cdots,X_n$决定，和“未来”无关

Wald引理$EZ_\tau = EZ_1\cdot E_\tau$
- 证明的核心：$I(\tau\ge i)$和$z_i$相互独立（因为“未来”了）
  - 所以$Ez_i^+= EI_{\{\tau\ge i\}}\cdot z_i^+$（因为如果$\tau< i$则显然$z_i=0$）
  - $^+$是一个trivial的分正负的技巧，并不核心

$EZ_1=0,EZ_1^2<\infty,E\tau<\infty$则$EZ_\tau^2=EZ_1^2\cdot E_\tau$
- 还是$I(\tau\ge i)$和$z_i^2$相互独立
  - 且根据$EZ_1=0$及独立性得到交叉项为0
- 证明的另一个核心是“取极限”，技术细节略

Stein：$\tau^* = inf\{n:n\ge 1,Z_n\notin (a,b)\}$，则$P(\tau^*>n)\le Me^{-rn}$
- 核心是一次“打包”$m$个，这$m$个不能偏差太多才有可能不停止
  - 而这$m$个偏差太多的概率大于0
- 那么很多个“$m$个的包”，每一个都不能偏差太多，就形成了指数衰减