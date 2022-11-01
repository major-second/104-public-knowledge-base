## 基础
- derivative衍生品！一般考察衍生品，因为足够复杂，考察理解
- maturity date, current time, time to maturity, stock price at time $t$, interest rate, dividend yield, volatility, European call, put, present value of future dividends, strike price, present value
- call: 期权买方有权利买
- put: 期权买方有权利卖
- strike price: 行权价格
- stock price: 股价
- 欧式：必须到期。美式：可以提前
  - 联想记忆：美国-暴发户-急
- payoff of a call $max(S-K,0)$
  - $S-K>0$，“低买”了：本来到时$S$买，到时你$K$可买，payoff为正
  - 本来到时$S$就能买到，你就别买了，所以payoff为零
- 所以显然，strike price提升时，call价格下降（不容易低买）
## 价格影响因素
- strike price提升，不容易低买，call价格下降
- stock price提升，容易低买，call价格上升
- 现金无风险利率/股息率两者相对，相互比较！
  - 股息高，那我就没有动力之后再买，那call价格下降
- time to maturity增加
  - 更多选择，美式价格都上升
  - 欧式
    - 早卖早拿现金，有可能使得put option此时价格下降
    - 早买早拿分红，有可能使得put option此时价格下降
    - 联系刚刚的“现金分红相对”！
- volatility上升
  - 如果你strike相对stock猜对了，波动率上升，赚多！
  - 如果你strike相对stock猜错了，不买卖即可
  - 所以期权价格都上升
- 以上是单变量。但各个变量可能相关
  - 比如利率下降，可能导致很多人买股票，股价上升
## put-call parity
- $c+Ke^{-rt} = p+S-D$
  - 注意意义：随着时间$t$变化，$S$等等值会变化，每一时刻分别满足
  - 法一
    - 组合1：$c$买个call option，$Ke^{-r\tau}$买个债券
      - 到时候卖：债券获得$K$，股票获得$max(S_T-K, 0)$
      - $S_T$和$S$不同（是到时候的价格）
    - 组合2：$p$买个put option，当前的$S$买个股票（protected put）
      - 到时候卖：获得$max(S_T, K)$
    - 两者之间无套利
    - 加上D（股息分红现值）：组合2的价格、代价都减去$D$
  - 法二
    - $c-p$：买call, 卖put
      - $S_T>K$：通过call，得到payoff $S_T-K$
      - $S_T<K$：由于put，得到payoff $S_T-K$（亏损）
      - 所以相当于forward delivery：预测$T$时刻价格是$K$，现在提前说好到时候拿$K$买一股（到时候价值$S_T$）
      - 也就是同样的payoff有两种实现模式：买卖期权或使用forward delivery
    - 而执行forward delivery这种模式需要付出$S-Ke^{-r\tau}$
      - 原因：你付出$S-Ke^{-r\tau}$得到这个权限，并付出$Ke^{-r\tau}$买债券，最终是得到一股；你直接买，是花$S$得到一股
      - 所以考虑股息的话，那：付出$S-Ke^{-r\tau}-D$得到这个权限，并付出$Ke^{-r\tau}$买债券，最终是得到一股。直接买是花$S-D$得到一股
    - 所以得到$c-p = S-Ke^{-r\tau}$（如果有股息，右边再减$D$）
    - 所以$K$和forward price $Se^{r\tau}$比较决定了$c,p$关系
- 不等式
  - 根据$p\ge 0$（显然，因为到时候我可以不卖），得到$S-D-Ke^{-r\tau}\le c$
    - 当然$c\ge 0$也成立
  - $S\ge c$（显然，因为股票价格大于等于0，你费那么大劲最后买了一股，还不如现在买）
- 美式变成的不等式$S-D-K\le C-P\le S-Ke^{-r\tau}$
  - 先不考虑股息
  - 右边：forward delivery价格
  - 中间：我是无情触发机器。put对手方一卖我就同样价格用call option的权买
  - 左边：0极限情况的forward delivery
  - 也就是中间是介于0和$\tau$时间的forward delivery
  - 加上股息：左边减去0，中间减去中间，右边减去$D$即可
## 美式call永远不会before maturity执行
- 没有股息，为什么美式call永远不会before maturity执行？
- 法零：刚刚说过了$S-D-K-P\le S-K\le  C$
- 法一：$c = (S-K)+(K-Ke^{-r\tau})+p$
  - 第一项是：intrinsic value, 假设现在马上$K$低买
  - 第二项time value of the strike：拖延买，也相当于低买省钱
  - 第三项$p$：protection against falling stock price
    - 如果股价下跌太多，你可以到时候不用期权买，而是直接买
    - 你不能凭空得到这个好处，付出$p$！
  - 第二三项正，欧式期权价值大于intrinsic value
  - 美式期权价值肯定更高
    - 所以提前行权是亏的
- 法二
  - 不急着买（行权）钱放着生利息多好
  - 具体地：你行权得到$S-K$现金，不行权也可以做空股票得$S$现金，借出$K$
  - 到$T$时候你获得现金$Ke^{r\tau}-min(S_T,K)$
  - 画现金流表，则：你$t$还是$S-K$，$T$又多了一份大于0的收入！好！
- 法三
  - $S<K$，那当然不行权
  - $S>K$，行权payoff关于$S$是凸（下凸）函数（$max(x,0)$）
  - 在（假设）行权时刻，行权payoff $C(S_t-K)$，否则$E[e^{-r\tau} C(S_T)]$（假设风险中性）
  - 根据[[jensen]]不等式得$e^{-r\tau} E[C(S_T)]\ge e^{-r\tau} C(E[S_T])$
  - 这个相比法一法二有额外假设$E[S_T] = e^{r\tau} S_t$
  - 最后根据[[jensen]]，$\lambda C(S)$和$C(\lambda S)$的关系得结果
  - American put不能套用同样的，因为$P(0)=K$，而非等于0
  - 有分红则American call只有可能分红日之前行权
## 例题：欧式期权套利
- 画payoff相对股价的图，0处$K$，$K$处0，之后0
- 画两条曲线，看相对关系，$y$方向压缩一条即可
## Black-Scholes-Merton
- 直接推导
  - $dS=\mu Sdt + \sigma SdW$
  - 使用[[5-brownian-motion-and-stochastic-calculus]]，得到
  - $dV=(V_t + \mu SV_S + \frac 12 \sigma^2 S^2 V_{SS})dt + \sigma SV_S dW$
    - 这个$V_S$表示那一瞬间的，看作常数，而$V(S(t)), S(t)$都随时间变化
    - 也就是$\Pi = V(t, S(t)) - \frac{\partial V}{\partial S}|_{t = t_0, S = S(t_0)} S(t)$
  - BSM方程：$V_t + rSV_S +\frac 12 \sigma^2 S^2 V_{SS} = rV$
  - 推导：买一单位衍生品，价值$V$，做空$V_S$单位股票，价值$-V_S S$
  - $d\Pi = dV-V_S dS = (伊藤得到那些项) - V_S (\mu Sdt + \sigma SdW) = (V_t + \frac 12 \sigma^2S^2 V_{SS})dt$
  - 它没有diffusion (涉及布朗的)项，risk-free，应该有无风险利率$d\Pi = r(V-V_S S)dt$
- 是[[feynman-kac]]定理特例
  - 风险中性假设：直接得到漂移项应该是$rS$，也就是$dS=rSdt + \sigma SdW$
  - 之后没看懂todo
## Black-Scholes formula
- 欧式期权，连续分红
- $c = Se^{-y\tau} N(d_1) - Ke^{-r\tau} N(d_2), p=Ka^{-r\tau} N(-d_2)-Se^{-y\tau} N(-d_1)$
- $N$是正态分布cdf，$d_1,d_2$是算出来的值
- 假设
  1. 原始版本无股息。扩展版本可以有
  2. 常数已知无风险利率
  3. $dS=\mu Sdt + \sigma SdW$，$\mu,\sigma$为漂移、波动率（常数）
  4. 没有交易成本，做空没有障碍
  5. 证券无限可分
  6. 不能无风险套利
- todo