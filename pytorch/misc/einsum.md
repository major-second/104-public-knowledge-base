# 爱因斯坦求和约定
爱因斯坦求和约定（einsum）提供了一套既简洁又优雅的规则，可实现包括但不限于：向量内积，向量外积，矩阵乘法，转置和[张量收缩（tensor contraction）](https://en.wikipedia.org/wiki/Tensor_contraction)等张量操作，熟练运用 einsum 可以很方便的实现复杂的张量操作，而且不容易出错。

# 基础
## 矩阵乘法例子
```python
a = torch.rand(2,3)
b = torch.rand(3,4)
c = torch.einsum("ik,kj->ij", [a, b])
# 等价操作 c = torch.mm(a, b)
```
## 参数
- 其中需要重点关注的是 `einsum` 的第一个参数 `"ik,kj->ij"`，该字符串（下文以 equation 表示）表示了输入和输出张量的维度。equation 中的箭头左边表示输入张量，以逗号分割每个输入张量，箭头右边则表示输出张量。表示维度的字符只能是26个英文字母 `'a' - 'z'`.
- 而 `einsum` 的第二个参数表示实际的输入张量列表，其数量要与 equation 中的输入数量对应。同时对应每个张量的 equation 子串（例如`ik`，`kj`等）的字符个数要与张量的真实维度对应，比如 `"ik,kj->ij"` 表示输入（2个）和输出（1个）张量都是两维的，其`.shape`分别为`(i, k), (k, j), (i, j)`
## 索引
- equation 中的字符也可以理解为索引，就是输出张量的某个位置的值，是怎么从输入张量中得到的
- 分为自由索引（`Free indices`）和求和索引（`Summation indices`）
  - 自由索引，出现在箭头右边的索引，比如上面的例子就是 i 和 j；
  - 求和索引，只出现在箭头左边的索引，表示中间计算结果需要这个维度上求和之后才能得到输出，比如上面的例子就是 k.
- 比如上面矩阵乘法的输出 `c` 的某个点 $c[i, j]$ 的值是通过 $a[i, k]$ 和 $b[k, j]$ 沿着 `k` 这个维度做内积得到的。对应了矩阵乘法的定义，即$c_{ij} = \sum_k a_{ik} b_{kj}$
- 这里其实是[[forall]]思想：也就是任意$i,j$，我们都知道$c[i,j]$是怎么来的，也就明白了整个$c$怎么来
## 关于 equation 的基本规则
1. equation 箭头左边，在不同输入之间重复出现的索引表示，把输入张量沿着该维度做乘法操作，比如还是以上面矩阵乘法为例， `"ik,kj->ij"`，k 在输入中重复出现，所以就是把 a 和 b 沿着 k 这个维度作相乘操作； 
2. 只出现在 equation 箭头左边的索引，表示中间计算结果需要在这个维度上求和，也就是上面提到的求和索引； 
3. equation 箭头右边的索引顺序可以是任意的，比如上面的 `"ik,kj->ij"` 如果写成 `"ik,kj->ji"`，那么就是返回输出结果的转置，用户只需要定义好索引的顺序，转置操作会在 einsum 内部完成。
## 特殊规则
1. equation 可以不写包括箭头在内的右边部分，那么在这种情况下，输出张量的维度会根据默认规则推导。就是把输入中只出现一次的索引取出来，然后按字母表顺序排列，比如上面的矩阵乘法 `"ik,kj->ij"` 也可以简化为 `"ik,kj"`，根据默认规则，输出就是 `"ij"` 与原来一样； 
1. equation 中支持 "..." 省略号，用于表示用户并不关心的索引，比如只对一个高维张量的最后两维做转置可以这么写：
```
a = torch.randn(2,3,5,7,9)
# i = 7, j = 9
b = torch.einsum('...ij->...ji', [a])
```
## 拓展例子
- 三个矩阵相乘则还可以`torch.einsum("ik,kl,lj->ij", [a, b, c])`，联系[[multiply-chain]]
- `torch.bmm`当然可以用`torch.einsum("bik,bkj->bij", [a, b])`表示
# 实例解读
## 1. 提取矩阵对角线
```
a = torch.arange(9).reshape(3, 3)
# i = 3
torch_ein_out = torch.einsum('ii->i', [a]).numpy()
torch_org_out = torch.diagonal(a, 0).numpy()

# torch_ein_out == torch_org_out
```

## 2. 矩阵转置
```
a = torch.arange(6).reshape(2, 3)
# i = 2, j = 3
torch_ein_out = torch.einsum('ij->ji', [a]).numpy()
torch_org_out = torch.transpose(a, 0, 1).numpy() 

# torch_ein_out == torch_org_out
```

## 3. permute 高维张量转置
```
a = torch.randn(2,3,5,7,9)
# i = 7, j = 9
torch_ein_out = torch.einsum('...ij->...ji', [a]).numpy()
torch_org_out = a.permute(0, 1, 2, 4, 3).numpy()

# torch_ein_out == torch_org_out
```

## 4. reduce sum
```
a = torch.arange(6).reshape(2, 3)
# i = 2, j = 3
torch_ein_out = torch.einsum('ij->', [a]).numpy()
torch_org_out = torch.sum(a).numpy()

# torch_ein_out == torch_org_out
```

## 5. 矩阵按列求和
```
a = torch.arange(6).reshape(2, 3)
# i = 2, j = 3
torch_ein_out = torch.einsum('ij->j', [a]).numpy()
torch_org_out = torch.sum(a, dim=0).numpy()

# torch_ein_out == torch_org_out
```

## 6. 矩阵向量乘法
```
a = torch.arange(6).reshape(2, 3)
b = torch.arange(3)
# i = 2, k = 3
torch_ein_out = torch.einsum('ik,k->i', [a, b]).numpy()
# 等价形式，可以省略箭头和输出
torch_ein_out2 = torch.einsum('ik,k', [a, b]).numpy()
torch_org_out = torch.mv(a, b).numpy()

```

## 7. 矩阵元素对应相乘并求reduce sum
```
a = torch.arange(6).reshape(2, 3)
b = torch.arange(6,12).reshape(2, 3)
# i = 2, j = 3
torch_ein_out = torch.einsum('ij,ij->', [a, b]).numpy()
# 等价形式，可以省略箭头和输出
torch_ein_out2 = torch.einsum('ij,ij', [a, b]).numpy()
torch_org_out = (a * b).sum().numpy()

```

## 8. 向量外积
```
a = torch.arange(3)
b = torch.arange(3,7)  # [3, 4, 5, 6]
# i = 3, j = 4
torch_ein_out = torch.einsum('i,j->ij', [a, b]).numpy()
# 等价形式，可以省略箭头和输出
torch_ein_out2 = torch.einsum('i,j', [a, b]).numpy()
torch_org_out = torch.outer(a, b).numpy()

```

## 9. 张量收缩 (tensor contraction)
```
a = torch.randn(2,3,5,7)
b = torch.randn(11,13,3,17,5)
# p = 2, q = 3, r = 5, s = 7
# t = 11, u = 13, v = 17, r = 5
torch_ein_out = torch.einsum('pqrs,tuqvr->pstuv', [a, b]).numpy()
torch_org_out = torch.tensordot(a, b, dims=([1, 2], [2, 4])).numpy()

```

## 10.二次变换(bilinear transformation)
```
a = torch.randn(2,3)
b = torch.randn(5,3,7)
c = torch.randn(2,7)
# i = 2, k = 3, j = 5, l = 7
torch_ein_out = torch.einsum('ik,jkl,il->ij', [a, b, c]).numpy()
m = torch.nn.Bilinear(3, 7, 5, bias=False)
m.weight.data = b
torch_org_out = m(a, c).detach().numpy()

```

原帖
作者：梁德澎

链接：https://zhuanlan.zhihu.com/p/361209187
