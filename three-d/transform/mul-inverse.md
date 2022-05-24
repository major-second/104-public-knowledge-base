前置
- [[quaternion]]. 理解三元组和四元数的复合和逆可以表示三维变换的复合和逆
- 这里用了[[pybullet]]中两个有关四元数的函数
- https://zhuanlan.zhihu.com/p/78987582
  - 这样你才能看懂四元数表示什么旋转
  - 核心：对于$(x,y,z)$作旋转变换，则记$P$为$(x,y,z)$对应的实部0四元数，$qPq^{-1}$就是结果。例如$i\cdot i \cdot (-i)=i,i\cdot j\cdot(-i)=-ki=-j$等

回忆[[quaternion]]中`pybullet`是`w`在最后
`pip install pybullet`
`python`
```python
>>> import pybullet as p
pybullet build time: May 20 2022 19:39:21
>>> tf1 = [[1,2,3],[0,1,0,0]]
>>> tf2 = [[4,5,6],[0,0,1,0]]
>>> tf_mul = p.multiplyTransforms(tf1[0], tf1[1], tf2[0], tf2[1])
>>> tf_mul
((-3.0, 7.0, -3.0), (1.0, 0.0, 0.0, 0.0))
```
- 注意到$jk=i$等运算规则
- 根据$qPq^{-1}$容易看出$x=1$的四元数就对应$x$轴不动，$y,z$反转。以此类推
  - 所以这里首先`tf1`相对原点走$1,2,3$，再$x,z$反转，接着再`tf2`走到$-3,7,-3$，再$x,y$反转，结果是$y,z$反转
- 总之这个`multiplyTransforms`的定义就是“一步一步来”，即首先写“b2a”，再写“c2b”

```python
>>> p.invertTransform(tf1[0],tf1[1])
((1.0, -2.0, 3.0), (0.0, 1.0, 0.0, 0.0))
```
逆的意义，验证也很显然
注意左逆、右逆是相同的（即一个变换和它的逆变换可交换）