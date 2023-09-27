# 指针
- `int`可以变成`const int, int const`两种
- `*`只能变成`*const`一种
- 一句话记忆：指针后置`const`修饰，变量类型可以后置或前置`const`
- [[2-4-cpp]]有这题

```cpp
// *后无const，指针可动，指向的东西不能动
const int*
int const*

// *后有const，指针不可动
int *const

// 指针和指向的东西都不可动
const int *const
int const *const
```
# [[func]]常参数
- 不可修改
- 可以与引用共同使用。节省拷贝，且避免改动
- [[2-4-cpp]]也有这题
# 类的常成员
- 和指针一样定语后置
```cpp
  void func() { std::cout << "General Function" << std::endl; }

  void constFunc1() const { std::cout << "Const Function 1" << std::endl; }

  void constFunc2(int ss) const {
    // func(); // 常成员函数不能调用普通成员函数
    constFunc1();  // 常成员函数可以调用常成员函数

    // s = ss; // 常成员函数不能改变普通成员变量
    // p = &ss; // 常成员函数不能改变常成员变量
  }
```
- `mutable`易变：可以被`const`成员改变
# `constexpr`
- 编译期可以求得
- `constexpr int a=10;`
- 实际上这个理解成数学中“常数”，`const`理解成“只读”挺好的
# 其它
- [[associative]]，const的map操作方法有不同，需要`.at()`