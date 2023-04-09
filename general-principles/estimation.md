[toc]
# 抢占市场先机
- 很多时候靠快速反应，mental power
- [[mental-math]]
- [[fermi-estimation]]
- [[adverse-selection]]
- [[jane-street-introduction]]中[文档链接](https://www.janestreet.com/static/pdfs/trading-interview.pdf)提到knowable unknowns
  - 比如喜马拉雅山天气，确实是已知数，但是你现在不知道，需要估个概率
# 数学中
## [[inequalities]]
  - 给出界（所谓“推bound”）
    - [[2-7-brain-teasers]]第16题
  - 给出[[enumerate]]范围
## 统计
- [[2-estimation]]
- [[confidence-interval]]
## 泰勒
- 物理常用估计式（$x$小）
  - $sinx\approx x$
  - $cosx \approx 1-x^2/2$
  - $(1+x)^n \approx 1+nx$
  - $ln(1+x)\approx x$
  - $e^x \approx x$
## 虚假规律
- 一些不成立的“规律”可以用于给出估计值
### $Ef(X)\approx f(EX)$
- 不等号方向参考[[convexity]], [[jensen]]
- 平方的期望本来不等于期望的平方，$E(X^2) \ge  (EX)^2$
  - 他们相差就是[[variance]]
  - 如果期望好算，平方期望不好算，可以用于估计
  - 4次硬币，正面次数的平方，可估计为$2^2=4$
  - 正确值：$\frac 1{16} (0*1+1*4+4*6+9*4+16*1) = 5$
- [[q-learning-overestimation#single estimator]]
- [[normal#cov#corr绝对值期望]]，例如$f(x)=\sqrt x$等
## 其它
- [[normal#cov#corr绝对值期望]]，忽略截距
- [[gamma-function]]中$\Gamma (a+1/2)/\Gamma(a)$
### 牛顿余项
### 拉格朗日余项
### 柯西余项
# 算法实际应用
- 作为[[workaround]]给出实际可行算法
  - [[q-learning]]
    - 虽然有[[q-learning-overestimation]]问题