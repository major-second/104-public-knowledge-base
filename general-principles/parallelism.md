- 参考
  - [[map-reduce]]
  - [[vectorized-operation]]
# [[tradeoff]]
- 速度：GPU > CPU的[[numpy-basics]]运算 > python的完全`for`循环串行（臭名昭著慢）
- 所能承载的数据量：一般相反。例如服务器上显存往往在10G量级，内存[[memory]]往往在100G量级
# 并行计算算法
- [[fourier-transform#FFT]]
- [parallel scan](https://www.zhihu.com/question/27547892/answer/336421027)
# 机器学习中
- 神经网络与并行
  - batch维度上肯定可以，这是深度学习算法的巨大优势
  - 序列维度
    - [[conv]], [[transformer]]可
    - 原始[[rnn]], [[lstm]]不可所以慢
    - 所以有[[rnn#parallelizing]]
- [[ensemble]]中，[[ensemble#boosting]]一大劣势就是不能并行
# shell
- `command1 & command2 & command3 & wait`
  - 如果不wait，则[[13-loop]]不方便
    - `bash -c 'sleep 1; echo 1' & bash -c 'sleep 2; echo 2' & echo 3`对比
    - `bash -c 'sleep 1; echo 1' & bash -c 'sleep 2; echo 2' & wait; echo 3`
    - `for i in {1..4}; do bash -c "sleep $i; echo $i" &; done; wait; echo 5`
# python
- for循环非常慢。但很多时候可以先写一个慢的然后让[[cursor-so]], [[chatgpt]]改
- 调包并行
  - 如[[multiprocessing-minimum]]中利用多进程`Pool`的`p.map`并行
  - 如[[numpy-basics]]可以`np.random.randint()`并行生成随机数
  - [[time-series]]可做时间序列相关处理
  - [[line-collection]]可并行画很多线段
- `torch`中[[tensor-calculator]]、[[profile]]证明用GPU大规模并行可提速
  - 一个实际例子：巧用[[indexing]]，为矩阵的上三角部分并行赋值
- [[vectorized-operation]]