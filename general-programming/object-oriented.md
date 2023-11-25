- 参考
  - [[cpp-oo]]
# py和cpp的类区别
1. 是否可以真正私有
- [[cpp-oo]]是真正私有的
- python https://blog.csdn.net/wohu1104/article/details/104460315
  - `_var`是约定，不是强制
  - 区别：`var_`是用于区分关键字，如`class_`
2. general的是否静态类型的区别
   1. 包括鸭子类型等等，都属于这点区别
3. python一切皆对象，类也是对象
4. 静态
   1. cpp有静态成员函数和普通成员函数
      1. 类名访问静态成员函数
      2. 对象访问普通
   2. py没有
      1. 不过当然有`@staticmethod`装饰器
      2. 但一般情况下，就直接`x.f()`等价于`MyClass.f(x)`
5. [[construct]]构造函数和析构函数
   1. py的GC都不是程序员控制的，自然没有
   2. 但是有[[python/magic]]方法`__init__`
# override-overload-overwrite
- [参考](https://stackoverflow.com/questions/4738315/c-overriding-overwriting)
- > In C++ terminology, you have overriding (relating to virtual methods in a class hierarchy) and overloading (related to a function having the same name but taking different parameters). You also have hiding of names (via explicit declaration of the same name in a nested declarative region or scope). The C++ standard does not use the term "overwrite" except in its canonical English form (that is, to replace one value with a new value, as in the assignment x = 10 which overwrites the previous value of x).