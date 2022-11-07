https://oiwiki.org/lang/csl/sequence-container/
## 序列式容器
### 好处（主要相比[[array]]）
- 动态分配内存
- 重载比较和赋值运算符
- 初始化方便
  - `=`初始化
  - 列表初始化比如`vector<int> data {1, 2, 3};`
  - `vector<int> v(3, 1);`：空间3，默认值1
  - 使用两个迭代器初始化
    - `vector<int> v(it1, it2);`
    - 相当于python的`[a:b]`切片
    - 在[[23-merge-k-sorted-lists]]，[[4-median-of-two-sorted-arrays]]都用到
### 使用
- `[]`, `front()`, `back()`都是引用
  - `back()`并不是`end()`那样“在外边”，而是在最后一个元素
- `data()`指针（指向第一个元素）
- `begin()`迭代器
  - 指针和迭代器关系：[[iterator]]有
- `vector<bool>`会导致坑。可以换成`deque`等
- `back`表示末尾。如`push_back`
  - 同理对于`deque`也就有`push_front`
- `insert`例子
```cpp
   vector<int> v = {3, 4, 5};
   auto it = v.insert(v.begin(), 2);
   v.insert(it, 1);
```
得到`1,2,3,4,5`
- `erase`
  - 可以单参数（传一个迭代器）
  - 也可以双参数（传两个迭代器，得一个左闭右开区间）
```cpp
   vector<int> v = {2, 3, 4, 5};
   auto it = v.erase(v.begin());
   v.insert(it, 1);
   v.erase(it+1, it+3);
```
得到`1,5`
### 其它
- `std::array`
  - 和[[array]]性能几乎一样，但有可以用`=`等前述优点
  - 显然`size()`始终等于`max_size()`
- 典型初始化：`array<int, 3> a = {1,2,3};`
  - 和[[bitset]]联想一下：`<>`中要写大小
  - 注意`3`必须是常数，和[[bitset]]也一样
- `list, forward_list`
  - 用法没啥差别，但原理不同，故复杂度不同，且不能随机访问
  - 用访问慢换取插入快
### 应用
- [[1-two-sum]]