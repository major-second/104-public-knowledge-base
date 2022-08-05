- 前置[[matplotlib/basics]]
- [参考](https://zhuanlan.zhihu.com/p/93423829)
  - 总结：`axes`是坐标轴的集合，相当于`plt`下属的“子”坐标系（子图）
- [文档](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html)

> The names ax and pluralized axs are preferred over axes because for the latter it's not clear if it refers to a single Axes instance or a collection of these.
```python
import matplotlib.pyplot as plt
fig, axs = plt.subplots(2, 2)
axs[1, 0].plot([1, 2], [3, 4])
plt.show()
```
- 关键字参数
  - `figsize=<元组>`设置大小，注意单位是英寸以及`dpi`问题，参考[[fig]]