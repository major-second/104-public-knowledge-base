前置：
- [[tensor-calculator]]

- 用法
`torch.where(condition, x, y)`
指逐元素判断condition是否成立，若成立，该元素取x中对应元素，否则取y中对应元素.
要求输入的condition, x, y均为相同size的tensor.
像`C`的运算符[[op]]中的`?:`三目运算符的并行版
- 如
`torch.where(x > y, x, y)`
为tensor x和y逐元素的较大值构成的tensor。
- 注意`x>y`的大小和类型
  - 不是布尔值，所以如果作为`if`条件会报错ambiguous