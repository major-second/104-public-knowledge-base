- 基础用法`df = df.dropna()`
  - 括号里填`0`或`1`指定是“凡是有`NaN`的行都去除”还是“列”
  - 通过concat操作（参考[[time-series]]）或`DataFrame(...)`生成更大的对象，可以实质上实现“或”关系，即“任何一个`NaN`都导致整行/列删除”