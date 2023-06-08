- 前置
  - [[expectation]]
  - [[variance]]：$E(X-\bar X)^2=EX^2-(EX)^2$
- 协方差：$E(X-\bar X)(Y-\bar Y) = EXY-EXEY$
  - 所以自己和自己的协方差就是[[variance]]
- 对于随机向量$\vec x = (x_1,\cdots, x_i)$（有限个随机变量），协方差矩阵$Cov(\xi,\eta)$显然是对称、非负定矩阵
  - 第$i,j$元就是$Cov(x_i,x_j)$
  - 联系[[cholesky]], [[multi-normal]]
  - 应用：线性组合的方差，特别地$X+Y, X-Y$方差
- 常用技巧：展开配对相减求cov表达式
  - 如[[orthogonal]]中求$cov(\hat \alpha_i,\hat\beta_j)$
  - 如[[linear-transform]]中求协方差矩阵变换后表达式
  - 一般地，$Cov(\sum a_iX_i, \sum b_jY_j)=\sum\sum a_ib_jCov(X_i,Y_j)$，当然可以特殊化到[[variance]]
# corr
- 定义：协方差[[cov]]除以两个随机变量的标准差
  - 注意不是除以两个方差[[variance]]
  - $\rho = Cov(X,Y)/\sigma_X\sigma_Y$
- 对于两个标准正态，[[iid]]则$\rho=0$，否则由于[[variance]]和标准差都是1，则[[cov]]矩阵就是$[[1,\rho],[\rho,1]]$
- $\rho^2=R^2$不是总成立，参考[[unary#$R^2$]]
## correlation matrix
- 联想协方差和协方差矩阵
- numpy中有[[numpy-basics#Array Mathematics]] `np.corrcoef(arr)`
## spearman
- 先[[data-science/normalization#排序]]再求[[cov#corr]]
- 实现：如参考[[scipy-correlation]]
# 无关
- cov为0称为无关
  - 是[[1-prob/independent]]必要条件
  - 可推出[[variance]]可加
  - [[orthogonal]]中有提到，作为了导出正交表概念的直观依据
- [[autoregressive]], [[multi-ary]]都有用到作为假设