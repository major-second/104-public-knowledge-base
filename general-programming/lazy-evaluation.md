- [[map-reduce]]
- 常见模式：先定义计算图，检验，优化，小规模试跑，再大规模
  - [[general-programming/debug]]思想！
- 例子
  - python [[map-reduce]]，可能一堆map和[[itertools]]，最后`list()`一下才实际执行
  - [[spreadsheets]], [[omegaconf-interpolation]]: 先不知道值，但是知道公式，去哪里找（“计算图”），也是这个意思
- 应用：对于[[pandas]] df，存储 incoming column name 和他的[[pandas-eval-expr]]，先不实际算