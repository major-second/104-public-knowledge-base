直观几何思想：正交变换，伸缩同时升降维，再正交变换
- 例题：$A_{m\times n}A^T=I,m<n$，证明$||Ax||\le ||x||$
  - $A$几何上相当于$n$维空间中$m$个正交单位向量
  - 现在$Ax$这样弄，结果直观上相当于把正交坐标系“弄歪”，然后每一维求和，然后每一维依次$x_i$的比例伸缩
  - 那么你就把它扶正，也就是$$\left (\begin{matrix} A\\B \end{matrix}\right )$$是正交方阵，记为$T$，那么$Ax$就是$$\left(\begin{matrix}I&0\end{matrix}\right)Tx$$
  - 所以$||Ax||\le ||Tx||=||x||$
  - 当然，这里是[[primitive-operations]]. 你也可以直接调奇异值分解包，认为$A = U\Sigma V$，那么$||Ax||=||\Sigma Vx||\le ||Vx||=||x||$