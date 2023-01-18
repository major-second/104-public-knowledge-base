充分利用机器资源进行并行提速！
- 调包并行
  - 如[[multiprocessing-minimum]]中利用多进程`Pool`的`p.map`并行
  - 如[[numpy/basics]]可以`np.random.randint()`并行生成随机数
  - [[time-series]]可做时间序列相关处理
  - [[line-collection]]可并行画很多线段
- `torch`中[[tensor-calculator]]、[[profile]]证明用GPU大规模并行可提速
  - 一个实际例子：巧用[[indexing]]，为矩阵的上三角部分并行赋值
- shell中：`command1 & command2 & command3 & wait`
  - 如果不wait，则[[13-loop]]不方便
    - `bash -c 'sleep 1; echo 1' & bash -c 'sleep 2; echo 2' & echo 3`对比
    - `bash -c 'sleep 1; echo 1' & bash -c 'sleep 2; echo 2' & wait; echo 3`
    - `for i in {1..4}; do bash -c "sleep $i; echo $i" &; done; wait; echo 5`
- [[tradeoff]]
  - 速度：GPU > CPU的[[numpy/basics]]运算 > python的完全`for`循环串行（臭名昭著慢）
  - 所能承载的数据量：一般相反。例如服务器上显存往往在10G量级，内存往往在100G量级
- 一个“算法题”示例：[[manipulation]]和[[indexing]]综合应用
  - 需求
    - 输入形如`i = torch.tensor([[1,0], [1,1], [0,1]])`
    - 输出`3 x 3`矩阵（`i.shape[0]`是3）
    - `i[0], i[1]`有（至少）一个共同的1，故输出矩阵的`[0, 1], [1, 0]`位为1
    - `i[1], i[2]`同理
    - `i[0], i[2]`没有共同的1，故输出矩阵`[0, 2], [2, 0]`为0
    - 特判：输出矩阵对角线为0
  - 一种解法：
    - 此处`r`表示row，`c`表示column
```python
def f(i):
    n = i.shape[0]
    matrix = torch.zeros(n, n)
    true_r, true_c = torch.where(i)
    p = true_c.shape[0]
    c_mask = true_c.reshape(p, 1).expand(p, p) == true_c.expand(p, p) - torch.eye(p)
    c_mask_true_r, c_mask_true_c = torch.where(c_mask)
    r_repeat_r, r_repeat_c = true_r.reshape(p, 1).expand(p, p), true_r.expand(p, p)
    r_enumerate = torch.cat((r_repeat_r.unsqueeze(2), r_repeat_c.unsqueeze(2)), 2)
    indices = r_enumerate[c_mask_true_r, c_mask_true_c]
    r_indices, c_indices = indices[:, 0], indices[:, 1]
    matrix[r_indices, c_indices] = 1
    return matrix
```