- [[variance]]：$E(X-\bar X)^2=EX^2-(EX)^2$
协方差：$E(X-\bar X)(Y-\bar Y) = EXY-EXEY$
所以自己和自己的协方差就是方差
- 对于随机向量$\vec x = (x_1,\cdots, x_i)$（有限个随机变量），协方差矩阵$Cov(\xi,\eta)$显然是对称、非负定矩阵。第$i,j$元就是$Cov(x_i,x_j)$
  - 联系[[cholesky]]等
- 应用举例：cov为0称为无关
  - [[orthogonal]]中有提到，作为了导出正交表概念的直观依据
- 常用技巧：展开配对相减求cov表达式
  - 如[[orthogonal]]中求$cov(\hat \alpha_i,\hat\beta_j)$
  - 如[[linear-transform]]中求协方差矩阵变换后表达式
  - 一般地，$Cov(\sum a_iX_i, \sum b_jY_j)=\sum\sum a_ib_jCov(X_i,Y_j)$，当然可以特殊化到[[variance]]
# corr
- 相关系数：协方差除以两个随机变量的标准差
  - 注意不是除以两个方差
  - $\rho = Cov(X,Y)/\sigma_X\sigma_Y$
  - spearman: 先[[data-science/normalization]]排序
- 注意$\rho^2=R^2$不是总成立，参考[[unary#$R^2$]]