- 检测
  - 对于二维张量，直接`sum(sum(tensor))`，如果有任何一个地方`nan`，结果就是`nan`
    - 其它维以此类推
  - 最后，单个数是否是`nan`用`torch.isnan`看
- 也是这个原因，所以只要一个地方`nan`，整个训练loss就`nan`了没意义了
- 数据里有`nan`的表现：`model(data)`结果是`nan`，但`model(torch.zeros_like(data))`不是（模型参数正常）
- `nan`的原因：比如手动做中心化标准化时没有考虑方差为0的情况（没有给$\sigma$强行加一个小的$\epsilon$），出现$0/0$
  - 注：$1/0$是`inf`