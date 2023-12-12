- 前置
  - [[symmetry#轮换]]

[toc]
## 定义
- 从小到大排列$X_i$，得到$X_{(1)}\cdots X_{(n)}$
- 对称性[[symmetry]]得到一个简单性质
  - 针对$[\theta,\theta+1]$上均匀分布
    - 显然有$E (min-\theta)=E(\theta+1-max)$
    - 中间的各个序列统计量也有类似的对称性式子
  - 由此可找无偏估计（参考[[unbiased]]）
## 数字特征
### 一般情况
- [[iid]]，共同分布函数$F(x)$
    - $P(X_{(i)}\le F(x))$，实质上可以看作均匀分布中的$P(X_{(i)}\le p)$
    - 因此就有了先算密度函数再算分布函数的思路
    - 密度函数显然是$C_n^{i-1}\cdot (n-i+1)x^{i-1}(1-x)^{n-i}$
      - 为啥显然？参考[[4-probability#4.6 order statistics]]
      - $n-i+1$种谁是重点的可能性，其余的有$C_n^{i-1}$种可能
      - 然后重点自己$f=1$一下，剩下的给面子$x^{i-1}(1-x)^{n-i}$一下
    - 从而$F(x)$可算出
### [[uniform-distribution]]
- 均值$i/(n+1)$
- 方差$i(n+1-i)/((n+1)^2(n+2))$
  - 计算方差：参考[[variance]]的$EX^2 - (EX)^2$
    - $(EX)^2 = i^2/(n+1)^2$
    - $EX^2 = i(i+1)/(n+1)(n+2)$
  - 这里积分是不停使用[[integral-by-parts]]
  - 或者直接调用[[B-function]]结论
#### [[multivariate]]
- [[uniform-distribution]] [[multivariate]] [[random-variable-functions#cdf]]
- $F(s_1,\cdots,s_n):=P(X_{(i)}\le s_i,\forall i)=n!\int_0^{s_1}\int_{x_1}^{s_2}\cdots\int_{x_{n-1}}^{s_n}dx_n\cdots dx_2 dx_1$
  - [[conditional]]
  - [[symmetry#轮换]]
- 应用[[poisson-process#截面]]
#### min-max-correlation
- [[correlation]]
- Let the infinitesimal element (n vars) be: $a<min<a+da, b<max<b+db, a<b$.
- Then $dP=dadb\cdot (b-a)^{n-2}\cdot const$.
- We need to calculate the integral: $Y:=$ min of n vars, $Z:=$ max of n vars, then $EY=\frac{\int adP}{\int dP}=\frac{\int_0^1 \int_0^b a(b-a)^{n-2}dadb}{\int_0^1\int_0^b (b-a)^{n-2}dadb}$.
- So we should calculate these first:
  - $\int_0^1 \int_0^b a^pb^q(b-a)^{n-2}dadb=\int_0^1\int_0^1c^p(1-c)^{n-2}dcdb\cdot b^{p+q+n-2+1}(here\quad c:=a/b)=\int_0^1 B(p+1,n-1)b^{p+q+n-2+1}db=B(p+1,n-1)/(p+q+n)=\frac{p!(n-2)!}{(p+n-1)!(p+q+n)}$
- We get $EY=\frac{\frac{1!(n-2)!}{n!(n+1)}}{\frac{0!(n-2)!}{(n-1)!n}}=\frac 1{n+1}$.
  - Remark: This is order statistics, $k/(n+1)$.
- We get $EZ=\frac{\frac{0!(n-2)!}{(n-1)!(n+1)}}{\frac{0!(n-2)!}{(n-1)!n}}=\frac n{n+1}$.
- We get $EY^2=\frac{\frac{2!(n-2)!}{(n+1)!(n+2)}}{\frac{0!(n-2)!}{(n-1)!n}}=\frac 2{(n+1)(n+2)}$.
- We get $EZ^2=\frac{\frac{0!(n-2)!}{(n-1)!(n+2)}}{\frac{0!(n-2)!}{(n-1)!n}}=\frac n{n+2}$.
- We get $VarY=\frac{2n+2-n-2}{(n+1)^2(n+2)}=\frac{n}{(n+1)^2(n+2)}$.
- We get $VarZ=\frac{n(n+1)^2-n^2(n+2)}{(n+1)^2(n+2)}=\frac n{(n+1)^2(n+2)}$.
  - This makes sense, $VarY=VarZ$.
- We get $EYZ=\frac{\frac{1!(n-2)!}{n!(n+2)}}{\frac{0!(n-2)!}{(n-1)!n}}=\frac 1{n+2}$.
- We get $Corr(Y,Z)=\frac{EYZ-EYEZ}{\sqrt{VarY VarZ}}=\frac{1/(n+2)-\frac{n}{(n+1)^2}}{\frac{n}{(n+1)^2(n+2)}}=\frac{1}{n}$.
- We get $EY=1/(n+1),EZ=n/(n+1), Corr(Y,Z)=1/n$.
- Given this result, it dawns on me that one can use $E(Y/z_0|Z=z_0)=1/n$ for a more intuitive solution.
## [[symmetry#轮换]]
- 参考[[4-probability]]中card game
- 如何直观记忆$i/(n+1)$
  - 比如$[0,1]$中随机取$n$个点
  - 你不妨看成一个圈上除了12点钟方向，随机取$n$个点
  - 或者整个圈上随机取$n+1$个点（12点钟那个点也是一个一般的点）
    - 本质上是发现了$n+1$个点的不显然的[[symmetry#轮换]]
  - 那不就出现了$i/(n+1)$吗
- 利用轮换对称性的直觉还有更多等式，例如$Emin(x_1, x_2)=E|x_2-x_1|=E(1-max(x_1,x_2))$
### 多边形概率
- 一根棍子随机切$n$段能构成多边形？
- 法一[[symmetry#轮换]]
  - $P(不能) = n\cdot \int_{1/2}^1 (n-1) (1-p)^{n-2}dp = n / 2^{n-1}$
- 法二[[self-similarity]]
  - $P_n(p)$表示$n$段分，长度为$p$的棍子，最长一段大于$1/2$概率，$p>1/2$
  - $q^{n-1}P_n(q)=\int_{1/2}^q (n-1)(q-p)^{n-2}dp + \int_0^{q-1/2} (n-1)(q-p)^{n-2} P_{n-1}(q-p)dp=(q-1/2)^{n-1}+ \int_0^{q-1/2} (n-1)(q-p)^{n-2} P_{n-1}(q-p)dp$
  - $P_1(p)=1$
  - $pP_2(p)=(p-1/2) + (p-1/2)$
  - 验证：$P_2(p)=2(p-1/2)/p$，正确
  - $P_3(1)=1/4 +\int_0^{1/2} 2(1-p)(1-2p)/(1-p)dp=1/4+1/2=3/4$，后面不想算了
## 应用
### 德军坦克
以下这里序列统计量记为$k_i$
利用德军坦克$n$个序列号估计总数：直接使用计数原理计算$P(k_n=i)$这种值，并利用组合恒等式得到$Ek_1,Ek_n$，从而证明某些统计量是某些东西的无偏估计
进一步，已知$Ek_1=\frac {N+1}{n+1},Ek_n = \frac{(N+1)n}{n+1}$，如何使得无偏，方差最小？（参考[[优良标准]]）
此处课本有个初等证明。核心思想是
- 统计量$\psi$在确定$k_n=l$时的期望作为统计量，正是估计量$W_2$（只和$k_n$有关）
- 证明最优的方法：$E_N(\psi-N)^2=E_N(\psi-W_2)^2+E_N(W_2-N)^2$

注：这里$Ek_1$表达式计算思想和序列统计量的数字特征是一样的。都是计数原理一下！
### L-statistics
序列统计量的线性组合称为L-statistics，在[[12-robust]]中有应用