- `size()`
- `find(str, pos)`
- `substr(pos, len)`切片（注意若`pos`是字符串长，则切出空串。若`pos`更大，报错）
- `insert(index, str)`和`replace(first, last, str)`：和`find`不同，是`str`写后面
- 也有`insert(index, count, ch)`（注意和插入`str`区别）
  - 当然也可以用迭代器`insert`
- 也有`push_back, pop_back, empty`等通用的
- `(auto x:s)`，`x`类型是`char`，联系[[associative]]
- `+=`拼接（可以拼接字符或字符串）