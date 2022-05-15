[toc]
# 把pytorch当高级计算器使用
前置：
- 有 #GPU
  - 或者使用在线的，[比如微软](https://docs.microsoft.com/en-us/learn/modules/intro-machine-learning-pytorch/)
- [[pytorch/basics/installation]]
  - 当然，也可直接使用[[深度学习镜像deepo]]。这样非常方便，开箱即用

## pytorch初体验
[[pytorch/basics/installation]]完了之后就可以（你的版本可能不同）
```sh
$ python
>>> import torch
>>> torch.__version__
'1.9.0+cu102'
```
本篇对pytorch的计算功能做简单上手
不涉及神经网络的训练，只是把pytorch当成高级计算器，即只涉及正问题，不涉及反问题
## 获得张量（tensors）
来到官网教程tensors一节
https://pytorch.org/tutorials/beginner/basics/tensor_tutorial.html
> Tensors are similar to NumPy’s ndarrays, except that tensors can run on GPUs or other hardware accelerators

- 常见构造方法：
  - 来自其它对象。例如`list`（这个效率低下），`numpy`数组，其它tensor，等等。总之就是`torch.tensor(<对象>)`
    - 注：反向操作：`my_tensor.cpu().numpy()`把GPU张量变成numpy数组
  - `torch.ones_like`，`torch.zeros_like`，`torch.zeros`等
    - 形状来自实参，内容根据函数名确定
    - 注意有没有`like`是不一样的。有`like`的生成张量和实参的大小相同，而没有`like`的实参是直接写大小是多少（比如`(2,2)`这种就表示2*2）
    - 另可指定数据类型`dtype=某`
    - 常见坑：直接`tensor(0)`，0后面没有小数点，当然是整型
- 张量的常见属性
  - `dtype`数据类型
  - `shape`形状
  - `device`所处设备（CPU，还是第几号GPU等）
  - 这些属性直接用`<变量名>.shape`这样取用即可
  - 更详见[[device]]

举例
```python
>>> import torch
>>> a = torch.tensor(((1.,2.),(3.,4.)))
>>> (a.dtype, a.shape, a.device)
(torch.float32, torch.Size([2, 2]), device(type='cpu'))
>>> b = torch.zeros_like(a, dtype=int, device=0)
>>> (b.dtype, b.shape, b.device, b[0][1])
(torch.int64, torch.Size([2, 2]), device(type='cuda', index=0), tensor(0, device='cuda:0'))
>>> a = torch.tensor((2,2))
>>> torch.zeros_like(a)
tensor([0, 0])
>>> torch.zeros(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: zeros(): argument 'size' (position 1) must be tuple of ints, not Tensor
```
注意`size`类型和`tensor`类型是不同的
- 这一点是一个良好规范的设计
- “洗脸布和擦脚布分开”，同一种数据结构不同“本质”的不放到一个类
## 当成高级计算器
```python
>>> mat_A = torch.tensor(([1,2],[3,4.]))
>>> mat_A * mat_A #逐元素相乘
tensor([[ 1.,  4.],
        [ 9., 16.]])
>>> mat_A @ mat_A.T #矩阵转置与相乘运算
tensor([[ 5., 11.],
        [11., 25.]])
>>> (mat_A.sum(), mat_A.sum().item()) #对单元素张量，用item()获得数值
(tensor(10.), 10.0)
```
就地（in-place）操作：例如`tensor.add_(5)`，用`_`标记
> In-place operations save some memory, but can be problematic when computing derivatives because of an immediate loss of history. Hence, their use is discouraged.