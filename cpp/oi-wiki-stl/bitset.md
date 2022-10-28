# 基础
- `#include <bitset>`
- 严格来说不是STL
- 一个字节8个比特用来存8位
- [[sequence]]中的`vector<bool>`是动态，这个`bitset`是静态
  - 一般用这个！
- 初始化
  - `bitset<1000> bs`，大小是1000位，全为0
    - 对比：`vector<int>`填类型
    - 这对应构造函数`bitset()`：初始化为全0
    - 参考[[construct]]，实际中不写括号！
  - `bitset<20> bs2(65535);`：4个0，16个1
    - 优先填后面，和[[array]]初始化不同
  - `bitset<20> bs3("1111");`：16个0，4个1
# 使用
- `[], ==, &, <<`运算符
- 输入输出`<<`, `>>`也行
- `count()`：多少个1
- `size(), any(), none(), all()`
- 设置：`set(), set(pos), reset(), reset(pos), flip(), flip(pos)`
- 转换：`to_string(), to_ulong()`
# 实际应用
- 没法用作[[dp]]当中的flag标记，因为输入的整数必须是常数
- 但比如对于字符串，确定有26个字母，那就可以用