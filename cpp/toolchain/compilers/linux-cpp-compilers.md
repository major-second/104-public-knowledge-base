- Prerequisites
  - [[apt]]
  - [[cpp-helloworld]]
- Install `g++`
  - [参考文档](https://gcc.gnu.org/onlinedocs/gcc/)
  - [Reference](https://zhuanlan.zhihu.com/p/476988995)
    - > Usually comes pre-installed
    - Can also be installed manually
    - Use `sudo apt update && sudo apt install g++` to install
    - Use `g++ -v` to check the [[version]]
- Usage
  - `g++ <file>.cpp -o test` to compile the program, `./test` to run it
  - Therefore,
    - Modifying the source code does not immediately cause changes like in [[python]]. It needs to be recompiled
    - Unlike [[shell]], it is not possible to make changes to the code while it is running
      - [[online]]
  - Flags
    - Optimization level: Recommended to use `-O2`
    - `-g`: Enables [[gdb]] for [[cpp-debug]]
    - `-Wall`: Enables all the warnings about constructions that some users consider questionable, and that are easy to avoid (or modify to prevent the warning), even in conjunction with macros.
    - `-shared`: Produces a shared object which can then be linked with other objects to form an executable. Not all systems support this option.
      - [[cpp-so]]需要，[[pybind11]]需要
    - `-std=c++11`: Specifies that the code should be compiled as C++11 standard.
    - `-fPIC`: Generates "Position Independent Code". The generated machine code is not dependent on being located at a specific address in order to work.
      - [参考](https://stackoverflow.com/questions/5311515/gcc-fpic-option)
      - 看起来[[cpp-so]]需要
- 有时出现[[linux-softlinks]]
  - 如`c++`可能最终指向`g++`（也可能其它编译器）
  - 参考[[help]]，`readlink -f $(which c++)`