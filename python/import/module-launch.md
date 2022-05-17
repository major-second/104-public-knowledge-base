```sh
python xxx.py # 直接运行
python -m xxx # 相当于import，叫做当做模块来启动
```
直接运行会将该脚本所在目录添加至`sys.path`
当做模块启动则会将当前运行命令的路径添加至`sys.path`
参考[[sys-path]]，其中也提到导入模块时当前路径不同就会影响导入是否成功（是否能找到）