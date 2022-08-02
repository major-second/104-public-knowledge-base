充分利用机器资源进行并行提速！
- 如[[minimum]]中利用多进程`Pool`的`p.map`并行
- [[tensor-calculator]]、[[profile]]证明用GPU大规模并行可提速
  - 实际中一个例子：巧用[[indexing]]，为矩阵的上三角部分并行赋值