https://zhuanlan.zhihu.com/p/64893308
所以，如果下级目录的**文件之间**`import`时，把下级目录视为了根目录
- 即：`./sub_dir/a.py`在导入`./sub_dir/b.py`时，使用的是`import b`

那么我们在上级（`.`）这里就应该`sys.path.append`下级目录`sub_dir`，并且模仿下级**文件之间**`import`时的写法，写`import b`
- vscode没法解析，但是这反而是对的
- 如果不这样，而是直接`import sub_dir.b`，vscode能解析，但是下级文件之间导入时就报错了