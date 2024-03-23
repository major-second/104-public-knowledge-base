- [[poetry]]
- [[version]]
- [[dependencies]]
- [文档](https://python-poetry.org/docs/dependency-specification/)
- 基本都在`[tool.poetry.dependencies]`下
  - [[poetry]]基础使用时可能就加了一些
- 设置[[git-basics/basics]]库依赖
  - `numpy = { git = "https://github.com/numpy/numpy.git", tag = "v0.13.2" }`
- 设置本地依赖
  - `my-package = { path = "../my-package/", develop = false }`
    - `develop = true`类似[[pip]]的`-e` [[command-line-flags]]
- 设置条件依赖
  - `pyarrow = { version = "^10.0.0", markers = "sys_platform == 'linux'" }`
- 依赖组（the following are not true. TODO）
  - 例如名称是`production`组
    ```toml
    [tool.poetry.group.production]
    optional = true
    [tool.poetry.group.production.dependencies]
    ...
    ```
    - 注意这里体现了[[toml]]一行格式和多行格式的等价性
    - [参考](https://python-poetry.org/docs/managing-dependencies/#optional-groups)
    - 但所有 optional groups 在 dependency resolve都会被考虑，会导致无解，报找不到本地包等错误
    - 如果不想要`production`组的依赖，可以`poetry install --without=production`
- [[CRUD]]
  - `poetry add`新增依赖
  - 更改刷新？根据命令行提示，如果和[[poetry-lock]]不一致，就`poetry lock`命令