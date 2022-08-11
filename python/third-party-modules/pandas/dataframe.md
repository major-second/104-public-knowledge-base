- 获取示例`DataFrame`
  - 本质是二维数组
  - 参考[[numpy/basic]]中创建`numpy`数组的过程，可以方便造出一些测试用的`DataFrame`
```python
import numpy as np
import pandas as pd
arr = np.random.rand(100, 5)
df = pd.DataFrame(arr)
```
- 如果需要字段名，则需`pd.DataFrame({'x': [1,2], 'y': [3,4]})`这样