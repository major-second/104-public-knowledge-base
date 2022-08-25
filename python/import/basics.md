# 基本语句
## `import`第三方库
- `import <包名> [as <别名>]`
  - 例如经常约定俗成的`import pandas as pd`，`import numpy as np`
- `from <包名> import <函数名、变量名等> [as <别名>]`
  - 这里的包名经常是用`.`隔开的路径（且不含`.py`后缀）
  - 参考[[module-launch]]
  - 此规则常能找到对应源码在哪个文件
    - 比如[[conda/commands]]中“找源码位置”就要参考这点
    - 举例：`torch.nn`对应`.../site-packages/torch/nn`文件夹
- `from <包名> import *`（非常不推荐，很有可能导致重名）
- `import a.b.c as d`
  - 例如经常约定俗成的`import matplotlib.pyplot as plt`，参考[[matplotlib/basics]]
## `import`自己的文件
在`./example`下运行命令`python -c "import a; print(a.a); import b; print(b.a_number); print(b.a); import c; print(c.b.a.a); import d; print(d.b); from d import b as db; print(db)"`
输出
```text
1
1
<module 'a' from '<文件名>'>
1
error
2
2
```
- 说明
  - 之前的基本语句，包括`from, as`等都能用
  - 同一文件夹下的`name.py`可以用`import name`来导入
  - 如果`import`的文件里也有`import`语句（或`from ... import`语句，等等），则可用`.`取出！比如`c.b`，`b.a_number`这样
  - 不能`import name.varname`（体现在上文输出中的`error`，参考`d.py`），但是可以`from name import varname`
    - 当然，你`import c`后用`c.b`取出的东西和`from c import b`得到的`b`相同
# 特性
## 关于路径
- 即使你`import`了非本路径的东西，整个程序运行的路径也还是本路径
  - 例如：你`import sub_dir.a`，那里面有torch的[[save]]函数等
    - 你调用了那里的进行[[save]]，相对路径基于的并不是`./sub_dir`，而是当前路径`./`
  - `import`的文件里还有`import`时，也要注意此规则，例如[[sys-path]]中的现象
## 关于重新`import`
- `import`后再`import`，已经导入的值默认不会动态变化
- 如果需要变化，那就要使用`importlib.reload(包名)`
  - 注意仅仅`del 变量名`无效
  - 注意不能`reload(变量名)`
  - 并且`from 包名 import 变量名`的变量也无法通过`reload(包名)`来reload
  - 参考下面例子
```sh
echo "from time import time; t = time()" > a.py; \
python -c "from a import t; print(t); del t; print(t); print()"; sleep 2; \
python -c "from a import t; print(t); del t; from a import t; print(t); print()"; sleep 2; \
python -c "from a import t; import a; from importlib import reload; print(t); reload(a); print(t); print(a.t)"; \
rm a.py
```