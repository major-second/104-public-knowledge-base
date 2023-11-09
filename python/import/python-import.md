# 前置
- [[naming]]

# 内容

## 基本语法

### 导入第三方库

- 使用 `import <包名> [as <别名>]` 来导入一个包。
  - 常见的例子包括 `import pandas as pd` 和 `import numpy as np`。
  - [[aliases]]
- 使用 `from <包名> import <函数名、变量名等> [as <别名>]` 来从一个包中导入特定的函数或变量。
  - 包名通常是由 `.` 分隔的路径（不包含 `.py` 扩展名）。
  - 参考 [[module-launch]]。
  - 此规则常能找到对应源码在哪个文件
    - 比如[[conda/commands]]中“找源码位置”就要参考这点
    - 例如，`torch.nn` 对应于 `.../site-packages/torch/nn` 目录。
- 使用 `from <包名> import *` 来从一个包中导入所有的函数和变量。这种做法并不推荐，因为可能会导致命名冲突。
- 使用 `import a.b.c as d` 来以别名的形式导入一个嵌套包中的模块。
  - 常见的例子是 `import matplotlib.pyplot as plt`。参考 [[matplotlib/basics]]。

### 导入自己的文件

在 `./example` 目录下运行以下命令：

```shell
python -c "import a; print(a.a); import b; print(b.a_number); print(b.a); import c; print(c.b.a.a); import d; print(d.b); from d import b as db; print(db)"
```

输出为：

```text
1
1
<module 'a' from '<文件名>'>
1
error
2
2
```

这个输出说明：

- 可以使用基本语法，包括 `from` 和 `as`。
- 在同一目录下的 `name.py` 文件可以使用 `import name` 来导入。
- 如果导入的文件中也包含导入语句（或 `from ... import` 语句等），则可以使用 `.` 来访问导入的模块或变量。例如，`c.b` 和 `b.a_number`。
    - 当然，你`import c`后用`c.b`取出的东西和`from c import b`得到的`b`相同
- 不能使用 `import name.varname`（如上文输出中的 `error` 所示，参考 `d.py`），但可以使用 `from name import varname`。
- 文件名必须遵循某些规则。例如，它们不能以数字开头。
  - 因此，一种实践是：以数字开头的 `.py` 文件是运行入口（`__main__`），其他的是工具组件。

# 特性

## 关于路径

- 即使你导入了非本路径的东西，整个程序运行的路径仍然是本路径。
  - 例如：你导入了 `sub_dir.a`，那里面有 torch 的 [[save]] 函数等。
    - 你调用了那里的 [[save]]，相对路径基于的并不是 `./sub_dir`，而是当前路径 `./`。
  - 如果导入的文件中还有导入语句，也要注意这个规则，例如 [[sys-path]] 中的现象。

## 关于重新导入
- [[refresh]]
- 导入后再导入，已经导入的值默认不会[[online]]变化。
- 如果需要变化，那就要使用 `importlib.reload(包名)`。
  - 注意仅仅 `del 变量名` ，则确实`del`后取变量报错，但重新`import`并不[[refresh]]
  - 注意不能 `reload(变量名)`。而是要`reload(包名)`
  - 并且 `from 包名 import 变量名` 的变量也无法通过 `reload(包名)` 来重新加载。
  - 例子：

```sh
echo "from time import time; t = time()" > a.py; \
python -c "from a import t; print(t); del t; print(t); print()"; sleep 2; \
python -c "from a import t; print(t); del t; from a import t; print(t); print()"; sleep 2; \
python -c "from a import t; import a; from importlib import reload; print(t); reload(a); print(t); print(a.t)"; \
rm a.py
```

# 进阶

- 使用 [[create-python-package-for-pip]] 和 [[pip]] 来优雅地导入不直接在当前文件夹下的文件
  - [[sys-path]]直接加？太tricky！