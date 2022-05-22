前置：
- [[tensor-calculator]]
- [[pickle/basics]]

# 现象
我们参考[[pickle/basics]]的说法，尝试对涉及张量的对象进行`pickle.dump()`成文件对拍
尝试
```sh
echo "
import torch
from pickle import dump
a = torch.tensor(1)
b = torch.tensor(1)
print(a == b)
print(torch.eq(a, b))
with open(\"1.pkl\", \"wb\") as f:
    dump(a, f)
with open(\"2.pkl\", \"wb\") as f:
    dump(b, f)
" > 1.py; \
python 1.py; \
diff 1.pkl 2.pkl

echo "
import numpy
from pickle import dump
a = numpy.array([1])
b = numpy.array([1])
with open(\"1.pkl\", \"wb\") as f:
    dump(a, f)
with open(\"2.pkl\", \"wb\") as f:
    dump(b, f)
" > 1.py; \
python 1.py; \
diff 1.pkl 2.pkl
```
事实证明，完全相等的`torch.tensor`在`dump`后很可能二进制文件不同。但`numpy`的数组就不会这样
具体原因比较复杂。在一些版本的pytorch中是和字典`for`循环及哈希有关
# 方法
## 转成`numpy`数组
```sh
echo "
import torch
from pickle import dump
a = torch.tensor(1)
b = torch.tensor(1)
print(a == b)
print(torch.eq(a, b))
a = a.numpy()
b = b.numpy()
with open(\"1.pkl\", \"wb\") as f:
    dump(a, f)
with open(\"2.pkl\", \"wb\") as f:
    dump(b, f)
" > 1.py; \
python 1.py; \
diff 1.pkl 2.pkl
```
上面这样是`diff`不出区别的
## 直接使用`torch.equal()`方法