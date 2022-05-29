用yaml列举好某个环境需要的包。示例：下面这样
可以看到
- 环境名称
- [[channel]]
- `conda`和[[pip]]各自装的包等等。
```yaml
name: dummy
channels:
  - anaconda
  - defaults
dependencies:
  - _libgcc_mutex=0.1=main
  - pip:
    - zipp==3.5.0
```
命令：`conda env create -f <path_to_yaml_file>`
- 注意不是`conda create`
- 注意有时可能需要[[sudo]]后`chmod -R 777`才有权限用`pip`装包