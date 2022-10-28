# 栈
- `#include <stack>`
- 定义方式和[[sequence]]类似
- 且也有复制构造
- 常见：`top(), push(), pop(), size(), empty()`
# 队列
- 头文件`<queue>`
- 像人排队，当然是队首`front`“露出”，马上被取出啦。不要老是记反
- 除了`front()`代替`top()`其它很像`stack`
# 优先队列
- 头文件还是`<queue>`，用法也很像`<queue>`
- 默认从小到大，`top()`是最大，并没有`front()`
  - `top`这个当然很直观，肯定是大的
  - 相比之下，[[associative]]中`map`是从小到大排（这个理由也很好理解，你脚标从0开始）
  - 因此`top`可以理解成“最后一个元素”，类似于栈顶
- “比较类型”
  - 比较类型是一个类型不是一个函数，参考[[associative]]里的指定比较方向
  - 默认从小到大，则默认的“比较类型”是`less<T>`
  - 不可跳过`Container`参数（底层容器）直接传入`Compare`参数
  - 也就是想要小根堆需要`priority_queue<int, vector<int>, greater<int> > pq;`
- 直接调包解题：[[215-kth-largest-element-in-an-array]]