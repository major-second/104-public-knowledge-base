- [[meta]] index: [numpy cheat sheets](https://www.kaggle.com/getting-started/255139)
- [本篇主要参考](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf)
  - cheatsheet已有不重复。这里只是一些补充
- 安装`pip install numpy`
- 导入`import numpy as np`
# Creating Arrays
- `np.array([2])`这种直接得到`[2]`
- `np.ndarray([2])`得到`.shape`（形状）是`[2]`的数组（一维数组，2个元素）
  - 默认随机初始化
  - 如果想不随机需要`zeros`等
- `np.arange(<类似于range()用法>)`
  - 例子
    - `np.arange(10)`
    - `np.arange(10, 0, -1)`
    - ```python
      >>> np.arange(10, 25, 2.2)
      array([10. , 12.2, 14.4, 16.6, 18.8, 21. , 23.2])
      ```
  - 应用
    - 结合[[numpy/reshape]]得到想要的形状，从而可方便[[general-programming/debug]]，探索numpy用法等
  - 注意
    - [[float]]
    - [[off-by-one-errors]]
- `np.linspace()`等差数列
  - ```python
    >>> np.linspace(0, 10, 11)
    array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.])
    >>> np.linspace(0, 10, 10) 
    array([ 0.        ,  1.11111111,  2.22222222,  3.33333333,  4.44444444,
            5.55555556,  6.66666667,  7.77777778,  8.88888889, 10.        ])
    ```
    - [[off-by-one-errors]]
  - 应用例如[[color]]
# I/O
- [[save-load]]
# 操作
- `np.concatenate((a, b))`，返回拼接结果，不改变`a`，`b`
  - 注意不要少打一对括号
  - 元组当然可以大于2个元素
  - 除了接受元组，当然也能接受`numpy`数组（例如输入二维数组，就是对一列一维数组作concatenate）
- `np.vstack`
  - 把`[(1,2),(3,4)]`变成`2*2`的
  - 把`np.ndarray((2,), dtype=object)`这类的变成正常的（类型为数值）的array
  - [各种stack](https://blog.csdn.net/csdn15698845876/article/details/73380803)
- `np.max`和`np.amax`分别求最大值的值和下标
- array做`< > ==`等运算得到布尔的array
  - 直接用作判断条件是“ambiguous”，会报错，也就是不能直接`if <array>`
    - 你想想，你这个`if <array>`到底是表示是否空还是是否全`False`，还是什么呢，确实不清楚嘛
  - 可以`(a > 0) * a`得到`a`的正的部分
  - 可以`np.where()`筛出为`True`的那些下标，这些下标排成一列
  - 注意不能使用一元`-`变成`-1`和`0`组成的数组！
    - 但可用一元`~`否定，二元`&`、`|`（不是`&&`，`||`）
  - 结合[[quantile]]，`max`等可以找到分位数位置
    - 求分位数时会在靠近的数间作插值，所以必须先用`<`，不能一来就用`==`
- `np.clip([1,2], 0, 1.5)`输出`array([1. , 1.5])`
- `np.power(底数, 指数)`
  - 注意妥善处理涉及负数的问题。比如`np.power((a > 0) * a, alpha) - np.power((a < 0) * -a, alpha)`
- `arr`有`.mean(), .min(), .max(), .sum()`等常用方法可以直接求常用值
- `np.linalg.norm(向量)`求模长，也可以`np.linalg.norm(a - b)`求距离
- `np.unpackbits(arr[:, np.newaxis], axis=1)`
  - [[encode-decode]]二进制布尔值手段
  - 用到了[[numpy/reshape#newaxis]]
  - 需要`uint8`之类的，具体就跟底层[[encode-decode#计算机编码]]有关
# 特性
- 速度快，更靠近底层
  - 所以会有
  - [[overflow]]问题！碰到很大的数做运算时小心
    - 一个中招的例子：使用`isnan`然后沿一条轴`sum()`，非0整数，就是有nan的行，这个没问题吧
    - 接下来，我想要过滤出那些自己是nan或者往前看若干时刻内有nan的
    - 于是就不停地`x[1:] += x[-1:]`
    - 啊这，就有可能溢出！
    - 应该用`|=`
  - [[float]]误差、精度问题
- 切片和原来共享同样的内存，改一个就全改。这点容易导致[[python/trivial-mistakes]]类似的错误
  - 而且这个更容易误导人造成坑……毕竟python原生list可不会切片了还共享内存
  - 甚至原生list的`l[:]`还是浅拷贝的一种方式