- 参考
  - [[naming#convention]]
- 前置
  - [[hypothesis-testing]]
- 针对$H_0,H_1$两个假设
# type-i-error
- 真实是$H_0$，错误地否定了（错杀）
- 对应[[power-level#水平]]
  - 一般较小。一般不要错杀
  - 书上说`like a legal trial`
# type-ii-error
- 真实是$H_1$，错误地肯定了（放过）：第二类错误
- 对应[[power-level#功效]]
# criteria
- 对超出两个的情况（如参数$\theta$有很多种取值）则对不同的$\theta$可能有不同的错误概率
  - 这些第一类错误概率如果被[[forall#一致]]考察，就引出了[[power-level]]水平概念
  - 在指定水平下，第二类错误再被[[forall#一致]]考察，就引出了[[UMP]]概念
  - 所以[[power-level]]，[[UMP]]定义是“不对称”的
# compared-to-confusion-matrix
- 两个假设，一共有四个数值
  - 参考[[2-eval]]的$TP, FP, TN, FN$
  - 但这里的$H_0,H_1$两者间如果没有概率的说法（不是[[bayesian-inference]]）
  - 那么就只有两个概率可以实际计算
  - [[2-eval]]的“准确率”算不了
  - 注：[[2-eval]]召回率对应[[power-level]]功效