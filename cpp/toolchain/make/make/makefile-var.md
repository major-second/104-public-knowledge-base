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