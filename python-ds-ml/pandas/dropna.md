- 前置[[nan]]
- 基础用法`df = df.dropna()`
  - 括号里填`0`或`1`指定是“凡是有`NaN`的**行**都去除”还是“**列**”
  - `subset=<list>`表示只考察这些（此时注意`how`是`any`还是`all`）
  - `how='all'`表示只有全部`NaN`才删除
- 填充参考[[pandas-fill]]