- intro
  - 不指定特定语言（和语言无关）
  - 如[[sort-intro]]，数值积分，[[newton]]法，[[2-brain-teasers]]等
1. 最简单的是矩形积分。可以考虑减少[[loop]]数量
2. 略
3. [[divide-and-conquer]]中的“倍增”
   1. 当然标答没那么fancy. [[looped-array]]就挺好
4. 总和，不断减即可
5. [[oi-wiki-basic/simulate]]
   1. 注意问：是否需要非常非常高效，hhh
   2. 写模拟当然要模块化
   3. 更多问题，例如[[tradeoff]]空间换时间，存万年历
6. [[divide-and-conquer]]中的“倍增”
   1. 并可结合特征值特征向量
7. [[oi-wiki-basic/simulate]]
   1. 有些tricky点：比如最小的左侧，最大的右侧，等等
8. 
   1. 0附近防不稳定可判[[special-case]]
   2. 其他地方同余化归，并可用[[taylor-expansion]]
   3. 标答：可以用标准库的sin，但是0附近手动泰勒展开
   4. 不连续性？使用[[bump-function]]，线性组合思想
9.  略（之前有解析解）
    1.  注意随机生成的小数乘以整数再取整得到生成随机整数
    2.  但有点不可靠：本来就伪随机了，而且小数点后面很长的部分更不稳定hhh
10. [[dp]]优中选优
11. [[sort-intro]]
    1.  $n!\approx (n/e)^n$中可能，用$n$次最多区分$2^n$种
12. [[7-algorithms]] random permutation
13. 注意太大超过整数了，截去后面就合理了（浮点操作）
14. [[7-algorithms]] search algorithm
15. todo
    1.  简单想法
        1.  先排序，则空间常数，时间nlogn
        2.  存储所有状态，则空间n了
16. 略
17. 回忆$\mathbb Z \times \mathbb Z$与$\mathbb Z$一一对应，我们分别考察静止，左移1，右移1……等等
18. 先一起龟速，然后碰到降落伞就开始“追”
19. [[oi-wiki-basic/recursion]]
    1.  注意[[special-case]]