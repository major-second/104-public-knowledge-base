注意一个坑
```python
from itertools import product
inputs = range(1, 10, 2)
filters_dic = {
    'for_list': [lambda x:x == i for i in inputs],
    'map_lambda': list(map(lambda i: (lambda x:x==i), inputs))
}
for (k, v), index, input_num in product(filters_dic.items(), range(len(inputs)), inputs):
    print(k, index, input_num, v[index](input_num))
```