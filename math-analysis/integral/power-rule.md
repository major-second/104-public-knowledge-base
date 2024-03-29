# 基本
- 求导$(x^n)'=nx^{n-1}$
- 积分
  - $\int x^{n-1}dx = x^n/n+C, n\ne 0$
  - $\int x^n dx = x^{n+1}/(n+1)+C,n\ne -1$
# 速算应用
- $\frac{\int_0^t x^n dx}{t\cdot t^n}=\frac 1{n+1}$
- $\frac{\int_{-t}^t x^{2n}dx}{2t\cdot (2t)^{2n}}=\frac 1{n+1}$
  - [[symmetry#翻转]]
- $n=1$，相当于[[linearity]]，直接参考[[linearity]]
- $n=2$
  - 三角形重心距顶点$a = \frac{\int_0^H h\cdot khdh}{\int_0^H khdh}=\frac 23 H$
  - 棱锥体积
  - 线段绕一端转动惯量$ml^2/3$
    - 绕中点$m(l/2)^2/3 =ml^2/12$
  - 抛物线下面积
    - “凹那端”是长方形1/3，“凸那端”是长方形2/3
    - [[symmetry#轮换]]圆上弦相交题
  - [[bayesian-inference]]中硬币，抛出一次正面，看后验
- $n=3$
  - 圆盘绕圆心转动惯量$\frac{\int \rho r\cdot r^2dr}{\int \rho rdr}=\frac{1/4}{1/2}mr^2=mr^2/2$
    - 圆环周长是一次幂，转动惯量本身是两次
  - 棱锥重心（3/4）
  - 四维单纯形体积（之后以此类推）
- $n=4$
  - 实心球绕过球心轴转动惯量
    - 垂直轴定理得$3X=2Y$
    - 其中$Y=\frac{\int \rho r^2 r^2dr}{\int \rho r^2dr}=\frac 35 mr^2$
    - $X=\frac 25 mr^2$