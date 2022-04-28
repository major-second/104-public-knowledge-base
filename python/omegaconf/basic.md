https://omegaconf.readthedocs.io/en/2.1_branch/index.html
- 初始
  - 安装`pip install omegaconf`
  - `from omegaconf import OmegaConf`
- 输入
  - `.create()`: 可以输入
    - 空
    - 字典
    - 表
    - 嵌套结构
    - yaml字符串
  - `.load()`yaml文件名（或文件对象）
  - `.from_dotlist()`: dotlist就是扁平化的树
  - `.from_cli()`: 使用`k=v`格式的参数，参考[[simulate]]来模拟
    - `k`中可以有`.`表示层级
- 支持类型：`str, int, bool, float`和[[enum]]
- `.to_yaml()`: 序列化成yaml！
- `.merge()`合并
- `???`表示必须填（mandatory）