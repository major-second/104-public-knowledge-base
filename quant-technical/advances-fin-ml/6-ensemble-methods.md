- 前置
  - [[ensemble]]
# 6.2
一来讲到[[bias-variance-tradeoff#bias-variance-noise]]
# 6.3
- [[ensemble#bagging]]
- 6.3.1
  - 理论上计算到底减少多少var
  - 容易看出希望 bagged estimator [[correlation]]不能太高
    - [[4-sample-weights]] sequential bootstrapping
- 6.3.2
  - improved accuracy参考[[2-eval]]
  - $p>1/k$，即对$k$分类，相比随机猜，有一定效果。则$N$大时ensemble结果accuracy更高
  - 但p本身不够大，结果也不行
- 6.3.3