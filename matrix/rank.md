- 秩越乘越小（不会变大）：因为秩=像空间维数
- 矩阵增广，秩不会变小
  - 同理$AB$和$A(B\quad C)$这种情况（还是利用像空间）
- $rank(AA^T)=rank(A^T)=rank(A)=rank(A^TA)$
  - $Ax=0\Rightarrow A^TAx=0\Rightarrow x^TA^TAx=0\Rightarrow ||Ax||=0\Rightarrow Ax=0$因此$A$，$A^TA$核空间维数相同，像空间维数相同
- 上述综合运用：$rank(X^TX)=rank(X^T)\ge rank(X^T(X\quad Y))\ge rank(X^TX)$，在[[multi-ary]]回归证明最小二乘法解存在时用到