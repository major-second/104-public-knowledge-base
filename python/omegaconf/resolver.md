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