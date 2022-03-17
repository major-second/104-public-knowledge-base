## `sys.path`
可以`append`或者`insert`在首位，来确保`import`时搜索路径
常见snippet
```python
import sys
path_old = sys.path.copy()
sys.path.remove('')
sys.path.insert(0, '你需要的路径')
from utils.reformat import omegaconf_to_dict, print_dict # 以改变过的path变量做import
sys.path = path_old
```

## 上面做法的应用
因为https://zhuanlan.zhihu.com/p/64893308
所以，如果你发现现象：下级目录的**文件之间**`import`时，把下级目录视为了根目录
- 即：`./sub_dir/a.py`在导入`./sub_dir/b.py`时，使用的是`import b`

那么我们在上级（`.`）这里就应该`sys.path.insert`下级目录`sub_dir`，并且模仿下级**文件之间**`import`时的写法，写`import b`，像上一节说的一样
- vscode没法解析，但是这反而是对的
- 如果不这样，而是直接`import sub_dir.b`，vscode能解析，但是下级文件之间导入时就报错了