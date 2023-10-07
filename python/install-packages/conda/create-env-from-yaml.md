- 前置
  - [[yaml]]
  - [[conda/commands]]
- [参考](https://zhuanlan.zhihu.com/p/586560032)
- 用yaml列举好某个环境名，需要的包等信息
  - 可以有
    - 环境名称
      - 其实这是可选的。[[robocorp-conda-yaml]]就没有
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
      - 注：有时为了保险起见还能在`dependencies`节点下属增加`python=<版本号>`和`pip=<版本号>`
- 使用命令：`conda env create -f <path_to_yaml_file>`
  - 注意不是`conda create`
  - 注意有时可能需要[[sudo]]后`chmod -R 777`才有权限用`pip`装包
- 反向：`conda env export -f <文件名>.yaml -n <已有的环境名>`，就可以给别人用
  - [[encode-decode]]