- 前置[[volatility-for-portfolio]]
- 作用：设置[[leverage]]等
- [[sharpe]]是$\frac{\alpha' w}{\sqrt{w'\Sigma_rw}}$
  - 联想[[3-2-conic-quadratic-modeling]]等等
- 适当[[reduction]]问题
  - $max_w \alpha' w,s.t. w'\Sigma_rw\le 1$
  - $max_w \alpha' w,s.t. w'\Sigma_rw= 1$
  - $b=\Sigma_r^{1/2}w$
  - $max_b \alpha'\Sigma_r^{-1/2}b,s.t.||b||=1$
  - [[ball-tangent-optimal]]得到$b^*=\frac{\Sigma_r^{-1/2}\alpha}{||\alpha'\Sigma_r^{-1/2}||}$
  - 代入，最佳sharpe为$\sqrt{\alpha'\Sigma_r^{-1}\alpha}$
- todo：使用[[volatility-for-portfolio]]中的模型