- 基础
  - `a = torch.tensor([[1,2], [3,4]]); print(a[0, 0], a[:, 0], a[0])`
  - 输出`tensor(1) tensor([1, 3]) tensor([1, 2])`
- 所谓“映射”
  - `a = torch.tensor([5, 6, 7, 8]); print(a[[1,2,3,0,1]])`
  - 输出`tensor([6, 7, 8, 5, 6])`
  - `a = torch.tensor([[[1,2],[3,4]], [[5,6],[7,8]]]); print(a[[1,0], :, [0,1]])`
  - 输出`tensor([[5, 7], [2, 4]])`
  - 即
    - 本来`[]`中填一个数的，现在变成填一个list
    - 本来填3个数的，现在变成填三个长度相同的list
    - 也可以有`:`
- 上下三角矩阵
  - `a = torch.zeros(3, 3, dtype=torch.long)`
  - `a[list(torch.triu_indices(3, 3))] = torch.arange(6) # 即上三角处依次0至5`
  - `a[list(torch.triu_indices(3, 3, 1))] = torch.arange(7, 10) # 偏离1，即对角线不算入`
    - 注：`list()`一下感觉是个tricky issue，反正一些版本pytorch如`1.1.0`中不`list()`会导致结果不是预期的上三角部分
  - `a`结果为
```python
tensor([[0, 7, 8],
        [0, 3, 9],
        [0, 0, 5]])
```