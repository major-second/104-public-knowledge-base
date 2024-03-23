- [[naming]]
- [[ontological-engineering]]
- [[renaming]]
- [[2-naming]]
# general
- [[object-oriented#override-overload-overwrite]] overload
- 写repo时，设定convention，概念设计，[[ontological-engineering]]
  - 例如
    - [[numpy-indexing#row and column]]
    - [[xarray]] [基础术语](https://docs.xarray.dev/en/stable/user-guide/terminology.html#term-Broadcasting)
# 具体规范例子
- [[binary-search]]命名上下界用`ub, lb`或`hi, lo`
- [[pep8]]这类规范
- python对象私有属性约定`_`开头
- 开头表示某种“类别”（可能是程序意义的class，也可以是自己的标记一个子集）
# 可能影响
- [[linting]]
  - 例如是否通过指定规则
    - `CamelCase`
    - `snake_case`
  - `_`开头标记没被用到的形参等
- 是否可以使用
  - 有[[leaky-abstraction]]嫌疑
  - [[pandas-eval-expr]]中显然不能用python关键字或者奇怪的column name等
  - python文件数字开头例如`0_abc.py`显然就无法[[python-import]]
    - 但可以作为一种convention，表示他是必须作为`__main__`的“脚本”
- [[syntax-highlighting]]
  - 例如是否大小写，颜色不同
- [[auto-completion]]
  - 例如私有`_`开头不被检测
# 重名
- [[python-import]] `*`一般要不得
- [[python]]中[[sys-path]]靠前路径下有一些名字（比如`utils`是最常见的坑）可能造成问题
- 作用域，函数
  - 因此通用做法：小作用域名字短
  - [[ide-automation]]能识别作用域，方便重名时[[renaming]]想要的部分
  - 但有时也会[[leaky-abstraction]]
    - 例如[[wikilinks]]
      - 在202403，识别作用域并不成熟，经常出问题
      - 所以最好做法还是文件名层面就不同，而不是让他必须通过作用域，`[[dir/name]]`这样区分