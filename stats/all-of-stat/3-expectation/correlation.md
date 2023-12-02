- 定义：协方差[[cov]]除以两个随机变量的标准差
  - 注意不是除以两个[[variance]]
    - [[dimensionless]]
  - $\rho = Cov(X,Y)/\sigma_X\sigma_Y$
## 与[[cov]]关系
- 对于两个标准正态，[[iid]]则$\rho=0$，否则由于[[variance]]和标准差都是1，则[[cov]]矩阵就是$[[1,\rho],[\rho,1]]$
- 对于一般情况随机变量也可[[normalization]]，之后用cov表示corr，方便计算等
  - 此时$\alpha X_1 + \beta X_2$就会经常出现$\alpha^2+\beta ^2=1$条件，经常用到[[ball-tangent-optimal]]
## 与[[r-squared]]关系
- $\rho^2=R^2$不是总成立，参考[[unary#$R^2$]]
  - 样本内成立
- correlation去除bias，[[r-squared]]没有去除
  - 参考[[unbiased]]
  - 参考[[correlation#information-leak]]
  - 所以预测结果corr r（但不一定是[[ols]]预测出的），则$R^2\le r^2$，如果偏得多则可能到$-\infty$
## correlation matrix
- 联想协方差和协方差矩阵
- numpy中有[[numpy-basics#Array Mathematics]] `np.corrcoef(arr)`
- 实操
  - [[pandas]]中有`df.corr()`
  - 得到矩阵可以[[seaborn]] `sns.headmap(..., annot=True)`
## spearman
- 先[[data-science/normalization#排序]]再求相关
- 实现：如参考[[scipy-correlation]]
## [[information-leak]]
- 相比[[r-squared]]，测试集上correlation作为评价指标，根据你的定义，可能用到了测试集均值/方差等
  - 你的定义当然要根据实际操作来。比如实际操作对结果不[[normalization]]，你corr计算定义减去了均值，就会无法体现问题
- 本质上，完全不看测试集，还是[[unary#$R^2$]]自然
- [[unary#$R^2$]]负，你leak一下均值或方差，可能corr还不错
  - 当然，这个不错可能确实也是能用的。比如交易涨跌，你整个方差不对没啥关系，趋势对了就行