- [[character/var]]：$E(X-\bar X)^2=EX^2-(EX)^2$
协方差：$E(X-\bar X)(Y-\bar Y) = EXY-EXEY$
所以自己和自己的协方差就是方差
- 对于随机向量$\vec x = (x_1,\cdots, x_i)$（有限个随机变量），协方差矩阵$Cov(\xi,\eta)$显然是对称、非负定矩阵。第$i,j$元就是$Cov(x_i,x_j)$
- 应用举例：cov为0称为无关
  - [[orthogonal]]中有提到，作为了导出正交表概念的直观依据
- 常用技巧：展开配对相减求cov表达式
  - 如[[orthogonal]]中求$cov(\hat \alpha_i,\hat\beta_j)$
  - 如[[transform]]中求协方差矩阵变换后表达式