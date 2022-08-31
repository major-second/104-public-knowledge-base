“魔术方法”，有时可以方便给出一些结果，但是使用时千万要慎重
以`__`开头和结尾
常见：
- `__init__`初始化对象
- `__eq__`等表示运算符怎么做
  - 比如`__getitem__`表示了`[]`下标运算符结果是什么，在[[dataset]]中必须继承
- 一些魔术方法表示`<方法名>(self)`得到什么
  - `<方法名>`可以是内置方法比如`len, str`
    - `__str__`不一定在`print()`时生效（比如打印对象组成的`list`时，就需要`__repr__`）
    - 更多详见[知乎：详解`__str__, __repr__, __format__`](https://zhuanlan.zhihu.com/p/130442206)
  - 也可能是非内置，例如[[numpy/magic]]中的`array(obj)`，在[[gym/wrapper]]中有例子

举例：
```python
class Foo:
    def __init__(self, v):
        self.v = v
        print(1)
    def __eq__(self, other):
        return self.v == 1 and other.v == 2
    def __getitem__(self, index):
        return index**2 + self.v**3
    def __len__(self):
        return self.v + 10000 # 必须是整数类型
    def __array__(self):
        import numpy as np
        return np.array([self.v, self.v, self.v])
```
典型运行结果
```python
>>> Foo(1)==Foo(2)
1
1
True
>>> Foo(1)==Foo(1)
1
1
False
>>> foo=Foo(3)
1
>>> foo[10]
127
>>> len(foo)
10003
>>> array(foo) # __array__和numpy有关，不属于“内置”的魔术方法
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'array' is not defined
>>> from numpy import array
>>> array(foo)
array([3, 3, 3])
```