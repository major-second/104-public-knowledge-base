- [[numpy-basics#Subsetting, Slicing, Indexing]]
# Slicing
- 特别注意[[share-lock]]，不是原生python的浅[[general-copy]]，容易造成误解、[[python/trivial-mistakes]]
# Fancy Indexing
- `import numpy as np`
- `a = np.arange(16).reshape((4,4))`
- `print(a[[1,2,3],[1,2,3]])`
  - 联想二元函数[[py-functional-programming#map]]或者[[itertools]]中的`starmap`
- `print(a[[1,2,1]][:, [2,3,2]])`
  - 联想做两次[[py-functional-programming#map]]
# row and column
- 根据矩阵的惯常[[naming#convention]]，对于二维`(m, n)`形状的array
  - `axis=0`对应row行，从0到m-1
  - `axis=1`对应column列，从0到n-1
- [[numpy-basics#Array Manipulation]]中`vstack, r_, hstack, column_stack, c_, vsplit, hsplit`都参考这个