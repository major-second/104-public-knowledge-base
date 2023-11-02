- 前置
  - [[bayesian-inference]]
# loss function
- 和深度学习[[loss-function]]区别参考[[loss-function]]
- $\Theta \times \Theta \to \mathbb R$，例如
  - [[ln-loss]]
  - [[entropy#KL Divergence]]
  - 非0即1
- action
  - 可称estimator（统计量，一套计算手段）为decision rule
  - 计算结果：action $a$，也就是$\hat\theta$
  - 损失和$\theta$、$a$有关，即$L(\theta,\hat\theta),L(\theta,a)$
  - 比如
    - [[point-estimation]]的误差（绝对值或平方）就可以是“损失”，这样导出贝叶斯估计
    - [[hypothesis-testing]]中，选择错误的分类也可以指定损失（甚至可以错得越离谱损失越大这样），这样导出贝叶斯检验
# risk
- 无论[[frequentist-bayesian]]，给定$\theta$时，$\hat\theta,a,L(\theta,\hat\theta)$都是个概率分布
- 所以无论[[frequentist-bayesian]]，都可以求$E_\theta(L)$称为risk
# 无法[[forall#一致]]
- [[estimation-in-stats]]估计里面经常需要一致
  - 比如[[优良标准]]
- 然而现在[[statistical-decision#risk]]很难（对参数）一致最小，那
  - 可以保守
    - 最小化maximum risk
    - minimax rule
  - 可以引入“期望”（Bayes risk）
    - 就要认为$\theta$有（先验）概率分布
    - [[bayesian-inference]]
    - 这时的估计问题：在后验分布上risk期望（也就是[[statistical-decision#loss function]]期望）应当最小
    - 得到[[bayes-estimator]]