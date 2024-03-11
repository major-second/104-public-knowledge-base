- 前置[[makefile]]
- 定义举例
    ```makefile
    CXX = g++
    CXXFLAGS = -std=c++20 -O2 -Wall
    PYBIND11_INCLUDES = $(shell python3 -m pybind11 --includes)
    ```
    - 参考[[pybind11]], [[linux-cpp-compilers]]
    - [[shell-type]]可以用`SHELL := /bin/bash -i`指定
- 取用：`$(变量名)`
- 特殊
  - `$@` target
  - `$<` dependency
- `$$`是[[escape]]，可以变成[[shell]]中的`$`，从而使用 [[shell]]中的 `$()`和`${}`
  - 但由于使用的shell种类等拉拉杂杂问题，终端有的变量make未必有
    - 可能解决一些问题的
      - `SHELL := /bin/bash`
      - 使用`bash -i` [[shell-type]]（交互式）
    - [[non-standard]]