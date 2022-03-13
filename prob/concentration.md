引入：iid伯努利，样本均值和$p$的差“收敛速度”如何
- 伯努利非负，则满足[[ineq]]中的切诺夫的条件
- 则$P(\sum x_i \ge n(p+\epsilon)) \le inf_t \{e^{-nt(p+\epsilon)}Ee^{t\sum x_i}\}$
- 期望可以显式写出来，最后变成了$\le inf\{ e^{-nt(p+\epsilon)}(pe^t+1-p)^n\}$
- 求极值（方法：考察$-t(p+\epsilon) + ln(pe^t+1-p)$，平凡地求导和考察极值性质等等）
  - 结果：$\le e^{-n D_B^{(e)}(p+\epsilon ||p )}$，其中$D_B^{(e)}$表示伯努利分布的KL divergence（参考[[entropy]]）
  - 这个也称为切诺夫
  - 这个bound可以称为concentration
## general
- 拓展1
伯努利情形：拉到两侧，相当于最坏情形
一般情况按道理应该由伯努利情形推出：凹凸性直接$Ee^{tx}\le pe^t+1-p$
- 拓展2
不一定iid，但是还在01区间，$\sum p_i/n=p$，那还可以模仿刚刚的证明，只需要$\prod (p_ie^t+1-p_i)$和$(pe^t+1-p)$的关系比较一下即可
## 推论
$D_B^{(e)}(p+\epsilon||p)\ge 2\epsilon^2$，因此可以简化
p离1/2远误差大
称为additive chernoff bound
## 独立性是否一定必要？
直接去掉肯定不行。比如所有变量都一样显然没有concentration了
但是可以调整：有放回和无放回：直觉上无放回concentration更强
证明：由$EX_iX_j$和$EY_iY_j$的关系看出母函数的关系
## 霍夫丁
不就是区间拓展一下呗
## McDiamond Lemma
$|f(...)-f(...)|\le \beta_i$，则$P(f-\sum f\ge \epsilon)\le e^{...}$，前面的concentration是特殊情况
利用了鞅