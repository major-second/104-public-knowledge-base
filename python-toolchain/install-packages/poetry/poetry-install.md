- 前置
    - [[poetry]]
    - [[pyproject-toml]]
- [文档](https://python-poetry.org/docs/managing-dependencies/#installing-group-dependencies)
  - `poetry install --sync`：一般的。会删除不需要的
  - 不加`--sync`：layering, optional，例如[[docker]]中需要。不会删除不需要的
- [[package-managers#source]]
  - ```toml
    [[tool.poetry.source]]
    name = "tsinghua"
    url = "https://pypi.tuna.tsinghua.edu.cn/simple"
    priority = "primary"
    ```
  - `poetry`会利用已有[[proxy-basics]]所以国内需要关掉才能访问清华源
- 根目录和`--no-root` [[command-line-flags]]
  - `poetry install --no-root`：忽略根目录本身，不认为是个包
  - 如果没有`--no-root`，则根目录本身需要是包，需要有`pyproject.toml`，`<package name>/<file name>.py`，`README.md`等结构，否则不会识别成包