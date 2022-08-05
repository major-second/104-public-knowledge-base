- 基础：[参考](https://matplotlib.org/stable/tutorials/colors/colors.html)
  - 示例：如[[plot]]加关键字参数`c`或`color`，里面可能写`'b'`，`'black'`，`(1, 0.5, 0.2)`等多种格式
  - 还可以`plt.scatter([1,2], [4,5], c=['r','b'])`这样（[[plot]]不行）
- 应用：[[visualization]]
- `cmap`和渐变色应用（使用内置`cmap`把0到1数映射到颜色）
  - [参考](https://www.codenong.com/8500700/)
  - 参考[[line-collection]]
  - 这里的代码也是从那里调整来的
```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection

x = np.arange(20) / 20
y = np.array([0.4, 0.5] * 10)

points = np.array([x, y]).T.reshape(-1, 1, 2)
print(points.shape)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
print(segments.shape)

ax = plt.axes()
# 只需要增加`array`表示数值，`cmap`表示数值映射到颜色，即可画一系列不同颜色的线段
ax.add_collection(LineCollection(segments, array=np.linspace(0, 1, 20), cmap=plt.get_cmap('copper')))

plt.show()
```
- 自定义`cmap`
  - [官方文档](https://matplotlib.org/stable/tutorials/colors/colormap-manipulation.html)
  - 最简单的方式
    - `from matplotlib.colors import ListedColormap`
    - `cmap = ListedColormap(["darkorange", "gold", "lawngreen", "lightseagreen"]) # 无渐变`
  - 有渐变的简单方式
    - `from matplotlib.colors import LinearSegmentedColormap`
    - `cmap=LinearSegmentedColormap.from_list('foo', ['y', 'r', 'b']) # foo是名称`
  - 复杂的
    - `from matplotlib.colors import LinearSegmentedColormap`
    - 需要定义`cdict`，参考文档说明如下
    - 定义`cmap`的方法：`newcmp = LinearSegmentedColormap('testCmap', segmentdata=cdict, N=256)`
```text
            cdict = {'red':   [(0.0,  0.0, 0.0),
                               (0.5,  1.0, 1.0),
                               (1.0,  1.0, 1.0)],

                     'green': [(0.0,  0.0, 0.0),
                               (0.25, 0.0, 0.0),
                               (0.75, 1.0, 1.0),
                               (1.0,  1.0, 1.0)],

                     'blue':  [(0.0,  0.0, 0.0),
                               (0.5,  0.0, 0.0),
                               (1.0,  1.0, 1.0)]}

        Each row in the table for a given color is a sequence of
        *x*, *y0*, *y1* tuples.  In each sequence, *x* must increase
        monotonically from 0 to 1.  For any input value *z* falling
        between *x[i]* and *x[i+1]*, the output value of a given color
        will be linearly interpolated between *y1[i]* and *y0[i+1]*::

            row i:   x  y0  y1
                           /
                          /
            row i+1: x  y0  y1

        Hence y0 in the first row and y1 in the last row are never used.
```