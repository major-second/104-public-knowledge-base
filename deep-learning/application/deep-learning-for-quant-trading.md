# 概述
- 量化，[[tabular-data]]，不一定直接打过[[decision-tree]]数据，但在[[decision-tree]]类模型上往往有[[marginal-utility]]，例如 [optiver比赛记录](https://zhuanlan.zhihu.com/p/678286556)
  - > 根据赛后分享的solution以及请教参赛者的信息，public 如果提交全0为540，开源特征工程可做到533，提升七个千分点，然后在线学习和深度学习模型融合分别可以提升一个千分点，达到531，其中在线学习在private效果会更佳，因此比起在开源基础上继续辛苦挖掘因子，还是上述的技巧好用，也足以抵挡后续的shake，预计后续的更新采用在线学习的名次还会进一步提升。
  - > 上面也提到了，特征工程做出的因子很难拉开区分度了，通常来说，在没有强特的比赛中，模型融合就变得很重要了，在树模型和开源相当的基础上，如果能融合上一个靠谱的NN模型，那么也可以带来稳定一个千分点的收益，这在非常内卷的比赛在就非常有益了。当然靠谱的NN模型也不容易得到，目前看前排的几位都是擅长NN模型的。
# DIN
- [DIN解说](https://mp.weixin.qq.com/s/YdcmB_7z1xp4YOMP8r_Asg)
  - deeplob等是一个部分
  - [原文](https://arxiv.org/pdf/2307.05522.pdf)
- interpretability
  - LIME, SHAP可解释性：不适用，主要因为
    - 金融不是[[stationary-processes]]
    - 太高维了，你逐特征看不出东西
  - 提供的可解释性
    - attention，主要表示不同时间点的相似度
    - variable selection network，主要表示哪些特征（每个特征都属于某个symbol）重要，以及重要事件时发生变化
    - 总之和[[barra]]那种传统的风控不同
    - 不过可以说对逐个asset（symbol）/feature 有风控
# deeplob
- [deeplob库](https://github.com/zcakhaa/DeepLOB-Deep-Convolutional-Neural-Networks-for-Limit-Order-Books)
- [deeplob arxiv](https://arxiv.org/abs/1808.03668)
  - 前置[[lob]]
  - 讲到[[domain-gap]], [[normalization#z-score]]
  - labelling
    - smoothing (using average)
    - use threshold, label datapoints as +1/-1/0
  - [[conv]] (inception其实也是[[conv]])
    - 废话有点多
    - stride, 1*2, 整合同一档pv
    - 4*1：时间维度卷一下
    - 1*10：一个时间戳所有档，类比 micro price 思想
      - 参考[[price-targets]]
    - 连zero padding, [[activation]]超参啥的都讲，233
    - [[1x1conv]]
  - [[lstm]]