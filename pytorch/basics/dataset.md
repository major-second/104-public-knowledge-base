[toc]
## 前置
- [[tensor-calculator]]
- 可能需要`torchvision`等`torch`相关的和数据集有关的额外包（`pip install torchvision`即可）
## 现成数据集
我们看[微软教程](https://docs.microsoft.com/en-us/learn/modules/intro-machine-learning-pytorch/)
到[这一步](https://docs.microsoft.com/en-us/learn/modules/intro-machine-learning-pytorch/3-data)
- 获取（可能需要下载）封装好的数据集，比如
```
import torch
from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda
training_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor(),
    target_transform=Lambda(lambda y: y * 100)
) # 注：如果在本地运行，会在./data下载数据
```
- 操作：`对象[index]`
  - 比如刚刚的`training_data[0]`，可以取出二元组（$x_i,y_i$对）
- 预处理
  - $x_i$预处理，例如`transform=ToTensor()`，输入PIL image或numpy数组，scales the image's pixel intensity values in the range $[0., 1.]$
  - $y_i$预处理，例如
    - 自己写一个`lambda`，并用`Lambda`包装
    - 比如一个dummy的：`target_transform=Lambda(lambda y: y * 100)`
    - 实用的：`target_transform=Lambda(lambda y: torch.zeros(10, dtype=torch.float).scatter_(dim=0, index=torch.tensor(y), value=1))`，变成浮点one-hot向量，参考[[manipulation]]
## 自己的dataset
常见的：[map式数据集](https://zhuanlan.zhihu.com/p/105507334)，本质上抽象成一个数组（“索引”）
- 继承`torch.utils.data.Dataset`
- 至少要重载`__getitem__, __len__`
## 个人理解：dataset的作用
- 防止一开始构造时不必要的耗时太长
  - 典型操作：一开始`__init__`只读取一个图片路径列表，之后需要时再[[open-convert-save]]中的open和convert图片。而不是一开始打开所有图片
- 由现有数据online生成数据时不要offline占用太多硬盘空间
  - 例如[[transforms]]在`__getitem__`中才进行，而不要读取时就offline进行全部存下来
  - 例如由$k$条数据组合出$C_k^2$条配对数据（如手写数字比大小）
    - 当然此时`__len__`就要相应改
  - `__getitem__`过程可能添加随机性，但这有时会带来困扰。所以做好注释！