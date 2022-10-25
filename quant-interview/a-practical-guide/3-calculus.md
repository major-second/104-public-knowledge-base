# 3.1 Limits and Derivatives
- 可以两边同时求对数，去除指数上的丑陋项，方便求导
- 用于比较大小，求极值最值
- 洛必达
  - 把分子变成分母再洛必达：$lnx/x^{-2}$
# 3.2 Integration
- 积分实际应用。例如两个圆柱相交部分体积
- 扫雪题：合理理解题意，得到$v(t+T)=常数$，并注意$\int vdt = x$
# 3.3
- 多元
- 直角坐标与极坐标
- 正态分布的积分
# 3.4
- 泰勒
- 拉格朗日余项
  - 应用：$(1+x)^n \ge 1+nx$，当$x>-1, n\ge 2$
- 牛顿法
  - $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$
- 泰勒或牛顿法都可用于估算
  - 其它估算法：二分，secant（割线），比牛顿慢
- 拉格朗日乘子法
  - $f+\lambda g$，对未知数求导0，对$\lambda$求导也0
  - 道理很简单：反正第二项都是0，所以对未知数求导0也就是第一项求导0. 然后再加上对$\lambda$求导0（也就是约束）
# 3.5
- separable
- first-order linear
  - $y'+Py=Q$
  - $Iy' + IPy = IQ$
  - $(Iy)' = IQ, I=e^{\int Pdx}$
- homogeneous
  - characteristic equation
  - 背三种解
  - nonhomogeneous：找特解