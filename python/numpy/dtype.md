- 用`dtype=`指定类型
- `numpy.int64`这种和`int`不同。不能高精，**且`isinstance`会报不同结果**
  - 而且一些IDE中并不会显式体现不同，比如`numpy.bool_`和`bool`的真都显示为蓝色的`True`，这个比较坑人

