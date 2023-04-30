- 实现：可以用标准库[[algorithm]]，参考：`partial_sum(v.begin(), v.end(), back_inserter(v2));`
  - 注意定义是$S_0=a_0$
- 应用：线性空间复杂度存储所有“子串”和。每次要取出时用两个相减即可
  - 相当于一种[[encode-decode]]
# 例题
- https://www.quora.com/How-can-someone-find-the-year-with-the-most-people-alive
  - 输入很多线段，用前缀和（一阶差分）观点相当于很多+1和-1
  - 相当于利用了[[linearity]]，差分和求和交换顺序
  - 通过计算$\sum Df_i$计算$D\sum f_i$，再求和得到$\sum f_i$
  - 拓展题：每次flip一段。那实际上每个位置只要储存0或1即可。[[boolean-arithmetics]]