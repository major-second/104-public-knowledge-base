# 动态图
## 伪动态图
- 不停刷新，然后在[[jupyter-notebook/basics]]中能看到效果，但不保存`.gif`
- [参考](https://blog.csdn.net/Hubans/article/details/115356898)
```python
from IPython import display
import matplotlib.pyplot as plt
for i in range(10):
    plt.plot([i, i+1])
    display.clear_output(wait=True)
    plt.pause(0.01)
plt.show()
```
- 往往需要结合`plt.xlim()`或`ax.set_xlim()`方法，[参考](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html)，否则`xlim, ylim`等不停变化，导致动图效果不理想