[toc]
# 几何意义
- [[imagination]]
- 圆，旋转，投影
- 欧拉公式：$e^{ix}=cosx+isinx$
## 几何意义例题
- 合适范围中，$\pi/4 >sinx(cosx-cosy) + siny(cosy-cosz)+sinzcosz$
# 基本性质
## 有界性、值域
- [[estimation#inequalities]]
- $|sinx|\le 1, |cosx|\le 1$
- $|Asinx + Bcosx|\le \sqrt{A^2+B^2}$
  - [[trigonometric#几何意义]]
## [[symmetry]]
- 关于一些直线[[symmetry#翻转]]对称
- 关于一些点[[symmetry#旋转]]对称
- 例题：$sinx$奇，$x^3$奇，因此$x^3+sinx=-y^3-siny, x,y\in [-\pi/2,\pi/2]\Rightarrow x=-y$
  - 设$f(x)=x^3+sinx$, [[naming#凑形式设函数]]
## [[monotonous]]
- 最值点、单调性、单调区间、零点
- 特殊点和[[trigonometric#symmetry]]的联系
### monotonous-例
- $x^2+y^2=k^2$何时覆盖$\sqrt 3 sin\frac{\pi x}k$的至少一个最大值点
- [[trigonometric-inequalities]]大量用到
## [[periodicity]]
- $\omega T = 2\pi$
- $\omega$：角频率
- $T$：周期
# 拓展补充
- 应用：[[lr-scheduler#cosine annealing]]