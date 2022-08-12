前置：
- [[tensor-calculator]]

## 一元
### 切片参考[[indexing]]
### `where`
- 一元`where`一个布尔张量，输出为`True`的那些指标。输出是个元组，元组每个元素对应原始张量一个维度
- 如`torch.where(torch.arange(8).reshape(2,2,2) % 3 == 0)`
- 输出三元组`(tensor([0, 0, 1]), tensor([0, 1, 1]), tensor([0, 1, 0]))`
- 也就是`[0,0,0], [0,1,1], [1,1,0]`三个地方
- 分别对应`0, 3, 6`
- 结合“切片”，容易验证`t = torch.arange(8).reshape(2,2,2); s = torch.where(t % 3 == 0); t[s]`结果就是`0, 3, 6`
## 三元
`where`和`scatter_`有点类似，都是把两个张量通过第三个张量指示进行“合并”
### `where`
- `torch.where(condition, x, y)`
逐元素判断condition是否成立，若成立，该元素取x中对应元素，否则取y中对应元素.
要求输入的condition, x, y均为相同size的tensor.
像`C`的运算符[[op]]中的`?:`三目运算符的并行版
- 如`torch.where(x > y, x, y)`
为tensor x和y逐元素的较大值构成的tensor
- 注意`x>y`的大小和类型
  - 不是布尔值，所以如果作为`if`条件会报错ambiguous
### `scatter_`
- `self(张量对象).scatter_(dim, index, src)`
- `dim=0`例子
```python
>>> x = torch.rand(2, 5)
>>> x
tensor([[ 0.3992,  0.2908,  0.9044,  0.4850,  0.6004],
        [ 0.5735,  0.9006,  0.6797,  0.4152,  0.1732]])
>>> torch.zeros(3, 5).scatter_(0, torch.tensor([[0, 1, 2, 0, 0], [2, 0, 0, 1, 2]]), x)
tensor([[ 0.3992,  0.9006,  0.6797,  0.4850,  0.6004],
        [ 0.0000,  0.2908,  0.0000,  0.4152,  0.0000],
        [ 0.5735,  0.0000,  0.9044,  0.0000,  0.1732]])
```
第0维是矩阵列，第1维是矩阵行。第0列（首列）的`0.3992, 0.0000, 0.5735`说明`0, 2`处是从`src`处的`0.3992, 0.5735`来的
- `dim=1`例子
```python
>>> src = torch.from_numpy(np.arange(1, 11)).float().view(2, 5)
>>> input_tensor = torch.zeros(3, 5)
>>> index_tensor = torch.tensor([[3, 0, 2, 1, 4], [2, 0, 1, 3, 1]])
>>> dim = 1
>>> input_tensor.scatter_(dim, index_tensor, src)
tensor([[ 2.,  4.,  3.,  1.,  5.],
        [ 7., 10.,  6.,  9.,  0.],
        [ 0.,  0.,  0.,  0.,  0.]])
```
中间那行的`[ 7., 10.,  6.,  9.,  0.]`说明`2, 0, 1, 3, 1`处依次从`6, 7, 8, 9, 10`来。`[1][1]`处的`8`被覆盖了
- 实用例子：构造one-hot向量。`lambda y: torch.zeros(10, dtype=torch.float).scatter_(dim=0, index=torch.tensor(y), src=torch.tensor(1.))`
  - 用法：可以通过`torchvision.Lambda`进一步包装，作为`target_transform`使用
## 多元
- `torch.cat([若干张量形成的list], [还可以选dim=?，在哪一维])`
  - 例如`torch.cat([torch.tensor([2]),torch.tensor([3]),torch.tensor([4])])`
  - 注意不能直接`torch.cat(torch.tensor([2]),torch.tensor([3]),torch.tensor([4]))`漏了中括号
- `torch.vstack`和`cat`总体类似。但维数不同
  - 两个`(2,)`的tensor，`cat`成`(4,)`，`vstack`则成`(2,2)`