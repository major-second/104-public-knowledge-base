前置[[oi-wiki-basic/var]]

https://oi-wiki.org/lang/func/

- 若先声明再定义。声明只需要`int some_function(int, int);`这种
- 也可以声明和定义放一起
- 注意：
  - 传值vs**传引用**：`foo(int& x, int& y)`
    - [[backtrack]]中常见传引用，积累所有可能结果
  - `main`的参数和返回值和外部（`shell`调用之类）有关
    - 比如命令行参数，命令行返回值
    - 例如用于[[12-condition]]判断
  - 非`void`函数，必须每个路径都有返回值（否则编译不通过）
    - 比如[[1-two-sum]]中，即使你知道不会运行到那，也要补充写上
  - 返回：只要运行到`return`，后面的就都不管
    - 所以可以少很多`else`
    - 尽量减少`else`的典型例子：[[10-regular-expression-matching]]
    - 联系[[4-decision-tree]]思想！