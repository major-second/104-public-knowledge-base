# Feynman-Kac定理
- 条件
  - $X$是$dX=\beta dt+\gamma dW$决定的Ito过程
  - $f(x)$是$x$的函数
  - $V(t,x):=E[f(X_T)|X_t=x]$显然是$x,t$函数
- 结论
  - $V(t,x)$是鞅
    - 直观意义非常显然（全期望公式）
  - 满足偏微分方程$V_t+\beta V_x + \frac 12 \gamma^2V_{xx}=0$（漂移率为0）（所以才是鞅嘛）
  - 边界条件$V(T,x)=f(x)$
- 应用
  - [[5-brownian-motion-and-stochastic-calculus]]的有漂移时算停止时间，可套结论
# discounted Feynman-Kac定理
- 条件
  - $V(t,x):=E[e^{-r(T-t)}f(X_T)|X_t=x]$显然是$x,t$函数，其余不变
- 结论
  - 其余结论不变
  - 满足偏微分方程$V_t+\beta V_x + \frac 12 \gamma^2 V_{xx}=rV$
- 应用
  - 期权的B-S-M微分方程，参考[[6-option]]