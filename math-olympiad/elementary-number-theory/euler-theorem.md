- [wiki](https://en.wikipedia.org/wiki/Euler%27s_theorem)
- 前置
  - [[eulers-totient-function]]
- 应用
  - [[rsa-cryptosystem]]
- 描述
  - $(n,a)=1, a^{\phi(n)} \equiv 1(mod\quad n)$
- [[general-principles/special-case]]
  - $p$是质数，$a^{p-1}\equiv 1, a^p\equiv a$
- 证明
  1. 法一：大小为$\phi(n)$乘法群$G$任何元素阶整除$|G|=\phi(n)$
  2. 法二
     1. $ab\equiv ac$则$a(b-c)|n,(b-c)|n,b\equiv c$
     2. 因此$a1\cdots a(n-1)\equiv 1\cdots(n-1)$（此处两侧各$\phi(n)$个因子）
     3. $a^{\phi(n)}\equiv1$