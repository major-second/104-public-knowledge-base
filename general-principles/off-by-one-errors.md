## 程序中
- 注意脚标一般从0开始（python, cpp都是），所以`vec[len(vec)]`一般是越界的
- 有时从1开始和从0开始不同，会带来麻烦，比如[[awk-cut]]提到的
- 自己写程序时，占位符为0，然后又从0开始编号，则0有两种含义，可能造成麻烦
    - 你可以`UNINITIALIZE = -1`（写在类定义之类的），这样可以放心从0开始编号
    - 当然，也可以有意义的数据（label之类的）1开始，双保险
## 算法题中
- [[encode-decode]]中序列的编码特别关注差1问题！
- [[oi-wiki-basic/simulate]]中常常有trivial的差1问题
  - [[68-text-justification]]
  - 涉及余数特别注意范围是0开始还是1开始，例如[[oi-wiki-basic/recursion#约瑟夫环]]
### 差一再差一
- 考察二维数组中一个点的所有相邻点
  - 在[[329-longest-increasing-path-in-a-matrix]]这种地方有用到
  - 本身小于$长度-1$，其右边才有点（最大等于$长度-1$），不出界
- [[sklearn/transform]]中
  - 12维选10维，则10个1，1个2，1个3
    - 也就是这里ranking从1开始，已经差了1
  - 所以我们`range`右侧是4，这样`i`最大是3
    - 即python的`range`又带来了差一
## 数学中
- 小学奥数植树问题，注意端点
- [[4-probability#4.5]] card game
- 触及本质的差一
  - [[variance#unbiased估计]]
    - 从而[[t-distribution#应用]]
- 仅仅是[[naming]]问题
  - [[gamma-function]]与[[factorial]]
    - [[gamma-distribution]]
  - [[B-function]]