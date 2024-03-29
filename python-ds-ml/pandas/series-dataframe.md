pandas的两类最基础对象：`Series`（一维）, `DataFrame`（二维）
#  `Series`
- `pd.Series([3,-5,7,4], index=['a','b','c','d'])`
  - 是一维的，这样是`a`对应`3`以此类推
  - 当然，也可以用[[numpy-basics]]一维数组
- `pd.Series([3,-5,7,4])`
  - 不设置`index`则自动`0`开始数字作为`index`
- `pd.Series(3)`
  - 输入标量
- `pd.Series(3, index=['a'])`
  - 此时如果使用index则使用单元素表
- `sr.describe()`给出基本信息
# `DataFrame`
- 二维
- 基本信息
  - `df.info()`输出基本信息（不是返回）
  - `df.describe()`返回一个有基本统计量的df
  - `df.head(<n>)`
  - `df.to_string()`变为可读字符串
    - 小心太大！这个不像 `print(df)`会自动省略给出一部分
- `pd.DataFrame([[1,2],[3,4]])`
  - 自动生成`index`为`0, 1`
  - 这样生成的，`1,3`为一般认为的“时间维”（用于`.loc`等），是一个`column`，和之后“字典”方法需要区别
  - 当然，也可以用[[numpy-basics]]二维数组
- `pd.DataFrame([[1,2],[3,4]], columns=['x','y'])`
- `pd.DataFrame({'x': [1,2], 'y': [3,4]})`
  - 字典键表示字段名
- `pd.DataFrame({'x': 1, 'y': 2}, index=[1])`
  - 即：也可以输入标量字典：但需要`index`
- `df = pd.DataFrame(index=..., columns=...); df.fillna(0, inplace=True)`
  - 参考[[nan]]
  - [[fillna]]
- 迭代`for k in df`时可以迭代字典的键
  - 相比之下`Series`迭代的是`index`，如`0,1`等
- 参考[[pd-read-csv]]
## `dtype`
- 创建时`dtype=...`参数
- `df.astype(...)`
  - `...`可以是单个类型，也可以是dict表示一部分的转换类型
- 对于`df`，没有`dtype`但有`dtypes`表示每一列的类型