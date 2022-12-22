```python
from collections import OrderedDict
d = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
```
- 之后`for`循环可确保顺序
- 存取值可以和普通dict一样`[], get, update`等等
- 显然不能像数组一样下标取值，否则无法区分是键还是下标
- 但`list(d.values())[2]`这样可以