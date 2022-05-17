用yaml写好环境需要的东西，典型的是下面这种感觉。可以看到名称，[[channel]]，`conda`和[[pip]]装的包等等。
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