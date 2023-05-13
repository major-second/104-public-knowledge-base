# 定义
- 周期$T$是**正**，常数
- $\forall x\in D(定义域),x+T\in D$
- $f(x)=f(x+T)$
# 最小正周期
- 可能不存在（如常函数）
## 最小正周期-例
- $sin(cosx)$的最小正周期
  - 首先$2\pi$是一个周期
  - 其次考察[[general-principles/special-case]] $f(T')\ne f(0), 0<T'<2\pi $
- $sinx+sin\omega x$何时是周期函数
  - $\forall n,x,sin(x+nT)-sinx + sin(\omega(x+nT))-sin\omega x\propto cos (x+nT/2)sin(nT/2)+cos(\omega (x+nT/2))sin(\omega nT/2)=0$
  - [[enumerate#pruning]]
    - 不妨设$|\omega|\ne 1$
    - 如果$\exist n, sin(nT/2)\ne 0, sin(\omega nT/2)\ne 0$则两次求导[[trigonometric-derivative]]，联立得$\forall x, cos(x+nT/2)=0,cos(\omega(x+nT/2))=0$，矛盾
  - 综上$\forall n, sin(nT/2)=0$或$sin(\omega nT/2)=0$
  - 再讨论：如果$\exist n$，上面两项只有一项为0，那也不行
  - 因此$\forall n, nT/2=k\pi, \omega nT/2 = k'\pi,k,k'\in \mathbb Z$
  - 因此要求$\omega \in \mathbb Q$
  - 且可证明充要