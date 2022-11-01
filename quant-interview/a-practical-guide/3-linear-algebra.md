# 3.6 Linear Algebra
- inner product
- Euclidean norm
  - 相关系数[[cov]]就可以看成某种正规化后的余弦，所以可以回答：$\rho_{x,y}, \rho_{x,z}$已知，那么$\rho_{y,z}$如何？
- QR分解
  - 非奇异矩阵，$Q$正交，$R$正三角且对角线正
  - 于是很容易解$Ax=b$，$A$非奇异，$A=QR, QRx=b,Rx=Q^{-1}b$
  - 应用：手撕OLS
    - 先推出$X^TX \hat \beta = X^TY$，可以矩阵求导，当然参考[[multi-ary]]也挺好
    - 再解$ \hat \beta$
- 回忆OLS条件
  - $Y=X\beta +\epsilon$
  - 误差期望0，方差恒定，不相关，和$x$独立
  - 没有相关系数为1的regressor对（否则系数解不唯一）
- $A-\lambda I$的行列式就是特征多项式characteristic polynomial，等于0就是characteristic equation
  - 特征多项式显然是$\prod (\lambda_i - \lambda)$
  - 由此结合行列式计算的定义，容易证明特征值乘积是行列式，和是trace
- 对角化，矩阵幂
- n个特征值相异且实，则特征向量无关independent，矩阵可对角化
- 正定半正定
  - 实对称矩阵可正交对角化
  - 特征值都是实数，特征向量正交
  - 半正定：“内积”非负/特征值非负/所有左上角的行列式非负
    - 所以必要条件：对角线无负
  - 应用：xyz三变量相关性的问题
矩阵
$$\left(\begin{matrix}1&0.8&0.8\\0.8&1&\rho\\0.8&\rho&1\end{matrix}\right)$$
半正定
- LU分解，Cholesky分解
  - 分解成下三角L上三角U
  - 可用于解方程组/算行列式
  - Cholesky：对于对称正定矩阵，$A=R^TR$，$R$是上三角对角线正的矩阵，唯一
    - 举例：由正态分布发生器生成相关的两个正态
      - 这个可以直接想到$z_1, \rho z_1+\sqrt {1-\rho^2} z_2$
      - 更多？那就依据上述思路弄三角矩阵呗
- 奇异值分解
  - $X=UDV^T$
  - 正交对角化是特殊情况
  - 于是$\Sigma  = UDU^T = UD^{1/2}(UD^{1/2})^T$，这也可以用来解这题
    - 回忆[[transform]]中的[[cov]]即可