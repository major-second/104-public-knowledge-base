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