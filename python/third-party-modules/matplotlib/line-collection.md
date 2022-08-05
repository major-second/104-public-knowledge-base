- 前置
  - [[axes]]
  - [[numpy/basic]]
- 需要渐变色（参考[[color]]）等等的时候，每段线段性质不同，为了[[parallelism]]提高效率，需要使用`LineCollection`
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
ax.add_collection(LineCollection(segments))

plt.show()
```