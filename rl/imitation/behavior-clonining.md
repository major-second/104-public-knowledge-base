- 非常直接地拟合action，作为分类或回归问题
- e.g. [DeepMimic](https://dl.acm.org/doi/pdf/10.1145/3197517.3201311)
  - input: NN model, example traj, reward function (task)
  - reward: $r_{RL+IL} = r_{RL} + distance(a_{ours},a_{expert})$