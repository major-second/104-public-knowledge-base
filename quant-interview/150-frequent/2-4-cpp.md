1. 
   1. 原始
      1. 栈区`T a[10];`
      2. 栈区`T a[] = {list};`
      3. 堆区`T* a = new T[10];`
   2. 拓展`std::array<int, 常数>`，参考[[array]], [[sequence]]
2. `&x`
   1. 具体：`T* ptr = &var;`
3. `int* p[10];`
   1. 拓展：`int* p[] = {...};`
   2. `int** p = new int*[10];`
      1. 这个比较复杂参考[[pointer-array]]
4. 参考[[const]]
5. 这个动态不是[[sequence]]的大小可变，而是`T* a = new int[10];`堆区数组，之后可以`T* a = nullptr;`或者`delete[] a;`等操作
6. 例子：`int my_sum(int a, int b);`
   1. 参考[[func]]
7. 函数声明中，`int& x`
8. `const int& x`
   1. 联系[[const]]
   2. 联系第4题
9.  几点
    1.  指针可以重新制定指向的位置，引用总是一个位置
    2.  指针可以指向`nullptr`，引用不行
        1.  这两点看，引用像`*const`
    3.  引用没有地址，指针可以取址
    4.  引用没有算术计算
10. 和python类似，比如括号里`int a = 1`
    1.  有默认值的必须放后面
11. 
    1.  基础
        1.  定义`template<typename T> T f(T a, T b){ return a+b+1; }`
        2.  使用`cout<<f(1,2)<<' '<<f(0.5,0.1)<<endl;`
    2.  `typename`还是`class`只是为了可读性（`typename`一般是原始类型）
12. 函数名整个变成`(*identifier)`，使用也要`(*p)`
    1.  `int f(int a, int b){return a+b;} int g(int a, int b){return a-b;}`
    2.  `int (*p) (int, int) = &f; cout<<(*p)(2, 3); p = &g; cout<<(*p)(2,3);`
13. 
14. 
    1. 函数中：直至程序结束占据固定位置
    2. 类中变量/函数：所有同一个类对象共享一个位置
    3. 全局变量：文件scope中private 
15. 
    1.  `const`修饰函数，不能修改`*this`的非`mutable`变量
    2.  `static`对类定义，没有`*this`概念！
16. 参考[[construct]]，[[initializer-list]]
17. 参考[[oo/copy]]
18. 刚刚说过了，共享指针，传值拷贝，结合造成了野指针
19. 
    1.  `struct A{int a; A(int a): a(a){} int operator+(A y){return a+y.a+1;}};`
        1.  加法是二元运算符，但参数传一元，另一元是自己
    2.  `A a(3); A b(4); cout<<a+b;`
20. [[smart-pointers]]，自动维护数量，没人引用自己删
    1.  `#include <memory>`
    2.  `shared_ptr<int> foo(new int(3)); shared_ptr<int> bar = foo;`，结果就两次引用
21. 封装，露接口，使实现不可见。往往通过access modifier（public等）实现
    1.  [[general-principles/recursion]]中需要你有这种思想
22. 多态：a set of classes, all be referenced through a common interface
23. 继承：extend, sub-classing
    1.  相比“封装”（“黑箱”re-use），这个称为“白箱”re-use
24. 虚函数：找子类的相同signature的实现，函数声明前加`virtual`
    1.  纯虚：必须找子类，基类变抽象，不可初始化。类比python的[[abstract-method]]装饰器，除了前加`virtual`，还有函数声明后面加`=0;`
25. 析构虚挺好的
    1.  构造函数不能虚！因为要知道要创建什么对象
26. 略
27. [[7-algorithms]]有maximum contiguous array讲到了
28. [[enumerate]]
    1.  注意利用“平方”剪去不需要的
29. 
    1.  用移位和`&`取位，讨论是否相同
    2.  注意使用按位异或`^`
30. 注意单向！先画图再[[oi-wiki-basic/simulate]]
31. 略
32. 遍历或[[oi-wiki-basic/recursion]]，略