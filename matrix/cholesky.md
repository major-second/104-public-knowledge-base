- https://en.wikipedia.org/wiki/Cholesky_decomposition
- 这里是下三角乘上三角
- cholesky算法：直观的算法！
  - 每一步，对角线非负，直接求出对角线元素$\sqrt a_{i,i}$
  - 然后可以唯一计算出“边上是啥”，最后计算出“右下角那块是啥”
  - 一步一步[[general-principles/recursion]]来
  - 应用：[[2-2-linear-algebra]]中，3阶做一步得到2阶，判断这个2阶是否半正定就知道3阶是否半正定