- 前置[[sequence]], [[iterator]]等
- [原文](https://oi-wiki.org/lang/csl/string/)
# 基本
- `std::string`
- 可以`string s = "123"`
- 能`cout<<`输出，`cin>>`输入
- `+, +=`拼接（可以拼接字符或字符串），有字典序比较
# 典型操作
- `size()`
  - 必须取了这个才能做判断条件。不能直接做
- `find(str, pos)`
  - 默认从`pos=0`开始，从头开始找
  - 没有出现：返回`string::npos`
    - `string::npos`是`-1`转化成`unsigned long`的值，但是具体多少不重要，有这个东西才重要，参考[[exists]]思想
- `substr(pos, len)`切片
  - 注意若`pos`是字符串长，则切出空串
  - 若`pos`更大，报错
- `insert(index, str)`和`replace(first, last, str)`
  - 和`find`不同，是`str`写后面
    - 对这个的理解记忆：可能因为`find`可以省略`pos`参数，只写`find(str)`？
  - 也有`insert(index, count, ch)`
    - 注意和插入`str`区别
    - 当然，可以用迭代器而不是`index`脚标插入
- 当然也有`push_back, pop_back, empty`等通用的东西
- `(auto x:s)`，`x`类型是`char`
  - 回忆[[loop]]
# 示例
```cpp
string s="123123";
cout<<s<<endl;
cout<<s+"45"<<endl;
cout<<s.size()<<s.find(s.substr(4, 2))<<endl;
s.insert(1, 4, 'x');
s.insert(2, "y");
s.replace(s.begin(), s.begin()+1, "zz");
s.push_back('w');
cout<<s;
```
输出
```text
123123
12312345
61
zzxyxxx23123w
```