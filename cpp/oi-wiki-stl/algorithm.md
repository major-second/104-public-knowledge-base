# 有起止点的
- 传入起止[[iterator]]
- `sort, reverse, unique`
  - `stable_sort`：稳定
- `next_permutation`：从小到大是第一个全排列，于是“下一个全排列”
- `unique`去除**相邻**重复的，返回去重后末尾迭代器
  - 迭代器可以减法，所以`unique(a, a+n) - a`表示去重后多少个元素
  - 如果一开始没排序可能要先排序
```cpp
  vector<int> v {1,6,5,3,5};
  auto b = v.begin();
  reverse(b+1, b+3);
  sort(b+2, b+5);
  for (auto it=v.begin(); it!=v.end(); it++) cout<<*it;
  cout<<endl;
  auto end = unique(b, b+5);
  for (auto it=v.begin(); it!=end; it++) cout<<*it;
  cout<<endl;
  sort(b, b+5);
  for (auto it=v.begin(); it!=v.end(); it++) cout<<*it;
  cout<<endl;
  end = unique(b, b+5);
  for (auto it=v.begin(); it!=end; it++) cout<<*it;
  cout<<endl;
```
- 结果
```text
15356
15356
13556
1356 #todo
```
# 除了起止点还有其它参数
- 第三个参数表示值
  - `find`：查找，返回迭代器
    - `find_end`：逆序查找，返回迭代器
  - `binary_search`：二分，有就说有
  - `upper_bound, lower_bound`
    - 和[[associative]]的行为、含义类似，返回迭代器
    - 不是数学上的“上界，下界”
    - 对于[[associative]]，请用内部封装的`s.upper_bound(x)`，不要外部调用，否则不是对数复杂度
- `shuffle`
  - `std::mt19937 rng(std::random_device{}());`
  - 然后把`rng`作为第三个参数
# 存到其它地方的
- `partial_sum`
  - 第三个参数是`back_inserter(dst)`，表示不断在后面插入
  - 求前缀和存到`dst`中
  - 位于头文件`<numeric>`而非`<algorithm>`
- `merge`
  - 前四个参数是两个“片段”，最后也是`back_inserter(dst)`，表示不断在后面插入

结合前两节的例子
```cpp
  vector<int> v {1,6,5,3,5};
  auto b = v.begin();
  auto it = find(b, b+5, 5);
  cout<<it-b;
  sort(v.begin(), v.end());
  if (binary_search(v.begin(), v.end(), 1)) cout<<'t';
  cout<<upper_bound(v.begin(), v.end(), 3) - v.begin();
  vector<int> v2, v3;
  partial_sum(v.begin(), v.end(), back_inserter(v2));
  merge(v.begin(), v.end(), v2.begin(), v2.end(), back_inserter(v3));
  cout<<endl;
  for (int n:v3)cout<<n<<' ';
```
结果
```text
2t2
1 1 3 4 5 5 6 9 14 20
```
# 其它
- `nth_element`, `inplace_merge`, todo