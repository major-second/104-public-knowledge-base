[toc]
# 抢占市场先机
- 很多时候靠快速反应，mental power
- [[mental-math]]
- [[fermi-estimation]]
- [[adverse-selection]]
- [[jane-street-introduction]]中[文档链接](https://www.janestreet.com/static/pdfs/trading-interview.pdf)提到knowable unknowns
  - 比如喜马拉雅山天气，确实是已知数，但是你现在不知道，需要估个概率
# 抓大放小
- [[estimation#泰勒]]
- [[normal#cov#corr绝对值期望]]，“集中赤道附近”
- 六面色子，丢出点100次方期望，约等于$6^{100}/6=6^{99}$
# 数学中
## [[inequalities]]
- 给出界（所谓“推bound”）
  - [[2-7-brain-teasers]]第16题
- 给出[[enumerate#pruning]]范围
- 解决关于“取值范围”题，如[[trigonometric]]
## 统计
- [[2-estimation]]
- [[confidence-interval]]
  - [[asymptotically-normal]]
  - [[LLN]], [[central-limit]]，例如$1000$个[[iid]]伯努利[[bernoulli-binom#bernoulli]]分布求和
## 虚假规律
- 一些不成立的“规律”可以用于给出估计值
### $Ef(X)\approx f(EX)$
- 不等号方向参考[[convexity]], [[jensen]]
- [[variance#与$EX^2$关系]]
  - 当然根据实际情况不同有两种情况，一种是$EX^2\approx (EX)^2$，一种是$EX^2\approx VarX$
- [[q-learning-overestimation#single estimator]]
- [[normal#cov#corr绝对值期望]]用到例如$f(x)=\sqrt x$情况等
## 泰勒
- [[小量近似]]
  - 例如[[转动惯量#平行轴定理]]例题
### 牛顿余项
### 拉格朗日余项
### 柯西余项
## 其它
- [[normal#cov#corr绝对值期望]]，忽略截距
- [[gamma-function]]中$\Gamma (a+1/2)/\Gamma(a)$
# 算法实际应用
- 作为[[workaround]]给出实际可行算法
  - [[q-learning]]
    - 虽然有[[q-learning-overestimation]]问题