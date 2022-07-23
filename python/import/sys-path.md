## `sys.path`
`import sys`后就可以使用`sys.path`变量。典型作用是确保`import`时搜索路径可用、正确
手动设置`import`的路径：可以`append`，或者更保险地，`insert`在首位
常见snippet
```python
import sys
path_old = sys.path.copy()
sys.path.remove('')
sys.path.insert(0, '你需要的路径')
from utils.reformat import omegaconf_to_dict, print_dict # 根据改变过的path变量做import
sys.path = path_old
```
这样做
- 可以确保你想要导入的模块优先级最先
  - 而不是`''`对应的优先级最先
- 是一种动态改变
  - 就无法做静态分析(lint)
  - 所以`pylance`插件识别不了
- 是确保实际运行中可以找到
  - 相比之下，[[vscode/settings]]是让`pylance`插件看起来可以找到，但实际运行时不能保证
## 上面做法的应用
- 如果你发现现象：下级目录的**文件之间**`import`时，把下级目录视为了根目录
  - 即：`./sub_dir/a.py`在导入`./sub_dir/b.py`时，使用的是`import b`
  - [参考](https://zhuanlan.zhihu.com/p/64893308)
- 那么我们在上级（`.`）这里就应该
  - `sys.path.insert`下级目录`sub_dir`
  - 并模仿**下级文件之间**`import`时的写法
    - 即写`import b`，像上一节说的一样
    - 而不是写`import sub_dir.b`
- 不可能三角
  - 避免改变/增加`sys.path`
  - 原来目录能运行
  - 新目录能运行
- 或者说：如果要在两个目录都能运行，那就必须改变/增加`sys.path`（听起来废话）
  - 若改变/增加`sys.path`
    - 可以保证两个目录都能运行
    - `pylance`没法解析，除非参考[[vscode/settings]]，直接告诉`pylance`你需要额外的`sys.path`条目
  - 如果`.`中直接写`import sub_dir.a`
    - `pylance`（无需额外设置即可）解析此句
    - 但是下级文件之间导入（`a`中`import b`）时就报错了
    - 参考[[module-launch]]：我们知道`python -m subdir.a`也会遇到同样的问题
  - 如果不想动`path`，那就要在下级那里`import b`的`b`前面用`.`分隔，写出根目录到那儿的相对路径（即改成`import sub_dir.b`）
    - `pylance`（无需额外设置即可）解析此句
    - `.`中`import sub_dir.a`也不报错
    - 但缺点是原来下级目录`sub_dir`那里能跑的程序现在不能跑了
## 和[[6-env]]的联系
- linux中的`PYTHONPATH`环境变量对应着python脚本里的`sys.path`
  - 区别于`shell`脚本运行时的`PATH`
  - 但可以看到两者的确有共同点：“去哪里找程序/脚本”
  - 只不过一个针对shell，一个针对python
- 拓展：使用vscode中的[[launch]]自动加`PYTHONPATH`