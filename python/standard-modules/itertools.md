- 前置[[map-reduce]], [[iterable-iterator]]
- [文档](https://docs.python.org/zh-cn/3/library/itertools.html)
# 基础
- `from itertools import *`
- `print(list(chain([1,2],[3,4],[5])))`
  - 这时经常就需要`chain(*my_2d_list)`了
- `print(list(starmap(pow, [(2,5), (3,2), (10,3)])))`
- `print(list(product('abc','de',[1,2])))`
# 无穷迭代器
```python
from itertools import *
for itertool, arg in zip((count, repeat, cycle), (7, 'a', 'bcd')):
    lst = []
    iter = itertool(arg)
    for i in range(20):
        lst.append(next(iter))
    print(lst)
```
注意小心死循环或导致调试不便等（见下文）
# 一个实际例子
```python
from itertools import *
my_list = [0, 1, 3, 4]
SYMBOLS_COUNT = 3
for i in product(
    chain(
        zip(repeat(0), my_list, repeat(2)),
        product([1, 2], range(2), [4, 8, 20])
    ),
    range(SYMBOLS_COUNT)
    ):
    print(i)
```
注意`my_list`必须有限，否则就会死循环
# 一个更复杂例子
```python
from itertools import *
for a, (tup, b) in product(
    range(3),
    zip(
        zip(count(), repeat(1), cycle('abc')),
        '1234'
    )):
    print(a, tup, b)
```
- 这个实际场景是需要`tup`是元组，所以没有一次性`zip(count(), repeat(1), cycle('abc'), '1234')`
- 你在调试[[iterable-iterator]]时，经常[[debug-console]] `a = list(a); print(a)`防止`a`元素一次被用光
- 可是这里`zip(count(), repeat(1), cycle('abc')`全是无穷，就没办法了，必须`list(zip(zip(count(), repeat(1), cycle('abc')), '1234'))`这样调试
- 可以看出无穷迭代器用多了会对调试产生困难！