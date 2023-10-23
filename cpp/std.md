- 此处收集`std::`中杂项
  - `max(a, b)`, `min(a, b)`可得最大/最小值，在[[11-container-with-most-water]]中使得代码简洁
  - `optional`
    - https://zhuanlan.zhihu.com/p/64985296
    - 用于可能失败时
    - 用法
      ```cpp
      cout << (*ret).out1 << endl; 
      cout << ret->out1 << endl;
      // 当没有 value 时调用该方法将 throws std::bad_optional_access 异常
      cout << ret.value().out1 << endl;
      // 当没有 value 调用该方法时将使用传入的默认值
      Out defaultVal;
      cout << ret.value_or(defaultVal).out1 << endl;
      ``` 