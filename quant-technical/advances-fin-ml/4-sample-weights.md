- 前置[[iid]]
# 4.2
- 不现实的：强行使样本不重叠，浪费信息量……
- [[sampling]]
# 4.3
- binary array方便操作：$1_{t,i}$
- concurrent labels: 重叠，$t$不变看$i$变
# 4.4
- 计算uniqueness of a label $i$ at time $t$，从而 of a label $i$
- harmonic average of $c_t$ over the event's lifespan
- uniqueness按道理不会造成[[information-leak]]
  - 思考：是不是可能有极端情况，比如从uniqueness高发现被掐断得快……算了不想那么多
# 4.5
- [[ensemble#bagging]]
- 对于uniqueness低数据集的问题：
- bootstrap不[[iid]]，本质重复数据
  - 是这里考察的问题
- 验证集[[information-leak]]
  - [[7-cross-validation]]考察
- 怎么解决bootstrap不[[iid]]
  - 法一：不靠谱：暴力排除，浪费数据
  - 法二：限制`max_samples`
  - 还挺实操，randomforest没有max_samples就decision trees
## Sequential Bootstrap
- [[online]]调整，动态调整
- 简单的：until K distinct original observations appear
- 这里的：根据uniqueness动态调权
- 嘿，还有[[monte-carlo]]，还有假设检验，证明有效
# 4.6
- 刚刚是[[iid]]目的，现在再考虑本身sampling的问题
  - large absolute value of return: 还在分类问题框架下，给大权重
- 注意[[normalization]]: 总和为总label数，和[[sklearn]]默认安排相关
- 如果三分类，有neutral，再这样分权重就不自然了
# 4.7
- 时间变化[[domain-gap]]，所以也可变权
# 4.8
- weights that correct for underrepresented labels (rare occurrences)
  - [[liquidity-crisis]]这种
  - 别被当成[[outliers]]了
- [[sklearn]]实操
  - 可以take这种weight改[[loss-function]]
    - 注：总weight加不到J？可能相当于一些[[regularization]]，不那么强调眼前数据！
  - `class_weight='balanced_subsample'`，正负样本 in-bag平衡