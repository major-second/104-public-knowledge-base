充分利用机器资源进行并行提速！
- 如[[minimum]]中利用多进程`Pool`的`p.map`并行
- [[tensor-calculator]]、[[profile]]证明用GPU大规模并行可提速
  - 实际中一个例子：巧用[[indexing]]，为矩阵的上三角部分并行赋值
- 调包并行
  - 如[[numpy/basic]]可以`np.random.randint()`并行生成随机数
  - [[time-series]]可做时间序列相关处理
  - [[line-collection]]可并行画很多线段