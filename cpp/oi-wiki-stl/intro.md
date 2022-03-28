- 前置：[[array]]

https://oiwiki.org/lang/csl/container/
![](intro.png)
序列、有序（用树维护）、无序（哈希）
有序无序都有可能有重复或无重复
栈、队列：
> ”适配器是使一种事物的行为类似于另外一种事物行为的一种机制”，适配器对容器进行包装，使其表现出另外一种行为。

声明：`containerName<typeName,...> name`

- 迭代器

https://oiwiki.org/lang/csl/iterator/
注意`begin()`和`end()`左闭右开
```cpp
for (vector<int>::iterator iter = data.begin(); iter != data.end(); iter++)
  cout << *iter << endl;  // 使用迭代器访问元素
// 在C++11后可以使用 auto iter = data.begin() 来简化上述代码
```
注意迭代器当然也可以`+1`，`+2`这样

关注迭代器分类（不互斥）
指针可以看成“最强的”（满足所有条件）
`std::advance(it, n)`：移动
`std::next(it, n)`和`prev`：获得后继/前驱

`rbegin`：反向，`cbegin`：常数