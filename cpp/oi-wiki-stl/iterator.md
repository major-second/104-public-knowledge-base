- 前置：[[container-intro]]
- [原文](https://oiwiki.org/lang/csl/iterator/)
- 常用`begin()`和`end()`，左闭右开
```cpp
for (vector<int>::iterator iter = data.begin(); iter != data.end(); iter++)
  cout << *iter << endl;  // 使用迭代器访问元素
// 在C++11后可以使用 auto iter = data.begin() 来简化上述代码
```
- 其它获得迭代器的函数
  - `.rbegin()`：反向的开始（即最后一个），和`.end()`不同
  - `.cbegin()`：常数
- 迭代器有`++`，`*`（自增，解引用）这些类似指针的运算
- 关注：迭代器分类（各类不互斥）
  - 指针可以看成“最强的”（满足所有条件）
- 一些常见操作
  - `std::advance(it, n)`：移动（正数向后）
  - `std::next(it, n)`和`std::prev(it, n)`：获得后继/前驱
    - `n`可省略
    - `prev`当然需要双向迭代器