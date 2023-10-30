## 一般的聚类（点分布在某个$n$维空间）
todo
## 只知道相似度矩阵，使用谱聚类
- 交互模式尝试
```python
from sklearn.cluster import SpectralClustering
import numpy as np
help(SpectralClustering) # q退出帮助
s2 = SpectralClustering(n_clusters=2, affinity='precomputed')
s3 = SpectralClustering(n_clusters=3, affinity='precomputed')
s4 = SpectralClustering(n_clusters=4, affinity='precomputed')
matrix = np.array([[1.,1,1,0,0,0,0,0,0]] * 3 + [[0,0,0,1,1,1,0,0,0]] * 3 + [[0,0,0,0,0,0,1,1,1]] * 3) # 注意小数点
matrix[0][-1] = matrix[-1][0] = 0.1
matrix
s2.fit(matrix).labels_
s3.fit(matrix).labels_
s4.fit(matrix).labels_
```
- 结果分别为
  - `array([1, 1, 1, 0, 0, 0, 1, 1, 1], dtype=int32)`
  - `array([2, 2, 2, 1, 1, 1, 0, 0, 0], dtype=int32)`
  - `array([3, 0, 0, 1, 1, 1, 2, 2, 3], dtype=int32)`