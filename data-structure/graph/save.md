- https://oi-wiki.org/graph/save/
- 邻接表
  - 一般用链表方便增删。如果不变，可以使用数组，例如[[210-course-schedule-ii]]，其中可以看到`const`图
- 无需额外储存
  - 例如[[shortest-path]]中从$(0,0)$到$(i,j)$最短路例子，只需根据特定规则知道哪些相邻即可
  - 例如[[329-longest-increasing-path-in-a-matrix]]，同样是哪些点之间连边直接通过规则可得到
# 矩阵
- [[hungarian]]用到