- 基本语句
  - `import <包名> [as <别名>]`
  - `from <包名> import <函数名、变量名等> [as <别名>]`
    - 这里的包名经常是用`.`隔开的路径（且不含`.py`后缀），能找到对应包源码的文件
    - 参考[[module-launch]]
    - 例如`torch.nn`对应`.../site-packages/torch/nn`文件夹，参考[[commands]]安装第三方包后的源码
  - `from <包名> import *`（非常不推荐，很有可能导致重名）
  - `import a.b.c as d`，例如经常约定俗成的`import matplotlib.pyplot as plt`，参考[[matplotlib/basics]]
- 特性
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