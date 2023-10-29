# 3.1
- [[supervised-learning]] vs [[unsupervised-learning]] （聚类等）
# 3.2
- 典型：[[bar-data#standard bars]], time bars, [[returns]]，根据涨跌阈值三分胜平负
  - [[discrete-continuous]]
- 坏处
  - 不adaptive
    - time bar坏处：信息量维度不adaptive
    - 固定阈值坏处：价格维度不adaptive
      - 可以考虑[[volatility]] [[EMA]] [[estimation]]之类，[[dimensionless]]
      - 可能就导致很多0
  - 没考虑止损
    - pm / 风控部门 / [[margin-call]]（爆仓，追加保证金通知）
    - 可以估计[[volatility]]用于这个
# 3.3
# 3.4
- The Triple-Barrier Method
- c形包围圈
  - 分成1，-1，0
  - 或者上下平分成1和-1，没有0
  - 上下horizontal barriers may be not symmetric
  - 可以取消部分barrier（比如深度套牢，233）
# 3.5
- 实践，[[pandas-multiprocessing]]地实现标记首次接触barrier（否则太慢）
# 3.6
- meta labelling：意思是第二次label，在已知side后，二分类是否bet，以分类“要bet”概率作为后续[[10-bet-sizing]]参考
# 3.7
- 讲了[[confusion-matrix]]
- meta labeling作用
  - 提升二分类性能
    - 模型先有大的 recall，取出 TP，即使很多FP
    - meta labeling再去除FP，提升precision
  - four additional reasons（总体上就是不[[end-to-end]]，[[problem-decomposition]]好处）
    - 更加白箱
    - [[overfit]]危害/风险降低，因为起码方向都是对的，你大小overfit也还行
      - [[problem-decomposition]]
    - 买卖分类讨论
      - 另一个角度[[problem-decomposition]]
    - 突出了[[10-bet-sizing]]重要性，避免只重视方向
# 3.9
- 去除太稀缺的类，原因both开发和数据层面
- 如果必须要，怎么办？[[4-sample-weights]]