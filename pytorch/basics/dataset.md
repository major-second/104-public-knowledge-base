前置：
- [[tensor-calculator]]
- 可能需要`torchvision`等`torch`相关的和数据集有关的额外包（`pip install torchvision`即可）

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
)
```
- 操作：`对象[index]`
  - 比如刚刚的`training_data[0]`，可以取出二元组（$x_i,y_i$对）
- 预处理
  - $x_i$，例如`transform=ToTensor()`，输入PIL image或numpy数组，scales the image's pixel intensity values in the range $[0., 1.]$
  - $y_i$，例如
    - 自己写一个`lambda`，并用`Lambda`包装
    - 比如一个dummy的：`target_transform=Lambda(lambda y: y * 100)`
    - 实用的：`target_transform=Lambda(lambda y: torch.zeros(10, dtype=torch.float).scatter_(dim=0, index=torch.tensor(y), value=1))`，变成浮点one-hot向量，参考[[manipulation]]