栈：
`#include <stack>`
定义方式和[[sequence]]类似。且也有复制构造
常见：`top(), push(), pop(), size(), empty()`

队列：像人排队，当然是队首“露出”啦。不要老是记反
除了`front()`代替`top()`其它很像`stack`

优先队列
默认从小到大，`top()`是最大
默认比较类型`less<T>`（比较类型是一个类型不是一个函数，参考[[associative]]里的指定比较方法）
不可跳过`Container`参数（底层容器）直接传入`Compare`