- 常用：在（往往是`dim=1`）进行`torch.cat`，参考[[manipulation]]
- 注意点
  - 可以考虑cat的位置（早合并还是晚合并）（或说：合并之前有什么预处理？合并之后进一步怎么做？）
- 犯过的不合理的东西：cat前没激活函数，cat后也没，导致有一个分量连续过两层线性没有激活，导致和预想的层数不同