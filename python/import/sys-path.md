## `sys.path`
`import sys`后就可以使用`sys.path`变量。典型作用是确保`import`时搜索路径可用、正确
手动设置`import`的路径：可以`append`，或者更保险地，`insert`在首位
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
- 不可能三角：避免动态改变`path`、原来目录能运行、新目录能运行。或者说：如果要在两个目录都能运行，那就必须动态改变`path`（听起来搁这搁这）
  - 动态改变`path`，vscode没法解析。但可以保证两个目录都能运行
  - 如果`.`中直接`import sub_dir.a`，vscode能解析，但是下级文件之间导入（`a`中导入`b`）时就报错了
    - 参考[[module-launch]]，所以说`python -m subdir.a`也会遇到同样的问题
  - 如果不想动`path`，那就要在下级那里`import b`的`b`前面用`.`分隔，写出根目录到那儿的相对路径（即改成`import sub_dir.b`）。这样vscode能解析，导入也不报错，但缺点是原来下级目录那里能跑的程序现在不能跑了
## 和[[6-env]]的联系
- linux中的`PYTHONPATH`环境变量对应着python脚本里的`sys.path`
  - 区别于`shell`脚本运行时的`PATH`
  - 但可以看到两者的确有共同点：“去哪里找程序/脚本”
- 拓展：使用vscode中的[[launch]]自动加`PYTHONPATH`