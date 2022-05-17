前置[[var]]

https://oiwiki.org/lang/struct/

- C++和C的结构体不同


```cpp
struct Object {
    int w;
    int v;
} e[length];
```
`a.b`
`a->b`相当于`(*a).b`

Bonus：如何设置构造函数
```cpp
struct MyListNode{
    pair<int, int> pa;
    MyListNode* prev;
    MyListNode* next;
    MyListNode(pair<int, int> a, MyListNode* p, MyListNode* n): pa(a), prev(p), next(n){};
}; // 一句话记忆：括号内呼应括号内（都是a, p, n）
```