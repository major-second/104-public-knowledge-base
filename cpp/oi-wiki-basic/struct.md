前置[[oi-wiki-basic/var]]

https://oiwiki.org/lang/struct/

- C++和C的结构体不同

```cpp
struct Object {
    int w;
    int v;
} e[length];
// 然后也可以
Object a;
Object b[l];
Object *c;
```
`a.b`
`a->b`相当于`(*a).b`（这里`a`是指针）

- 设置构造函数的例子
```cpp
#include <iostream>
using namespace std;
struct Object {
  int i;
  double d;
  Object(int i, double d): i(i), d(d) {}
};
int main() {
  Object o(2.1, 3.1);
  cout<<o.i<<endl<<o.d;
} // 输出2和3.1
```
- 应用：[[dp]]中，让返回输出解过程更清晰
  - 如[[368-largest-divisible-subset]]