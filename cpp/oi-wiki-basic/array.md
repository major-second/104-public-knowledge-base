- 前置[[var]]

https://oiwiki.org/lang/array/
- 大小固定（`const int`才行）
  - 如果数组长度编译期未知，那就还是参考[[sequence]]吧，比如`vector<int> v(n);`
  - 当然，`int v[n];`不保证一定报错。这是g++扩展，不是标准化的一部分，不保证所有地方能用（但OI有时恰好可以用）。总之别指望。参考：https://zh.wikipedia.org/zh-cn/%E5%8F%AF%E5%8F%98%E9%95%BF%E6%95%B0%E7%BB%84
- 不能直接用`=`复制
- 静态（堆）区创建，否则容易爆栈