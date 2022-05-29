# 内置resolver示例：`oc.select`
相比`${}`，`${oc.select:<字段>,<默认值>}`可以在字段不存在时返回默认值。还有转义冒号的用途
但这个还是有一定局限，比如“键不存在”的错误不能传递。只能干脆一点：你有就有，没有就没有，别让我找了半天最后告诉我没有！
# 自定义resolver示例：`eq`（是否等于某个）
py中
```python
# 开头import的时候
from omegaconf import DictConfig, OmegaConf
OmegaConf.register_new_resolver('eq', lambda x, y: x.lower()==y.lower(), replace=True)
```
yaml中
`${eq:${...pipeline},"gpu"}`
即：`${<resolver名>:<逗号隔开参数>}`
- `...`就是回溯两级
- `$`可以嵌套（或者说对于`eq`这个resolver，不嵌套有何意义？233）