- 安装：`sudo apt install cmake`
- 使用
  - 可能需要[[sudo]]权限
  - 步骤
    - 到项目根目录
      - 下属东西一般有
        - [[makefile]]
        - [[cmakelists-txt]]
        - `src`目录，即源码
        - 你之后的`build`也会放里面
          - 可能已经有`build`了，此时
            - 如果
              - 之前有人用过，你不放心之前版本
              - 之前失败过，有残缺的
            - 则需要删除`build`，这是[[refresh]]
    - `mkdir build && cd build`
    - 此时可选：加载依赖（包等），例如在此处[[conan-install]]
    - `cmake ..`
      - `-D`用来添加参数，格式为`-DKEY=value`
        - `-D CMAKE_BUILD_TYPE`或`-DCMAKE_BUILD_TYPE`
          - 这是[[naming]]约定俗成
          - 一般`-D CMAKE_BUILD_TYPE=Release`
          - 有时`-D CMAKE_BUILD_TYPE=Debug`
            - 可能用于生成能用于[[general-programming/debug]]的[[binary-executable]]
            - 用于[[gdb]]
        - 示例：[OpenCV](https://docs.opencv.org/4.2.0/d7/d9f/tutorial_linux_install.html)
          - `-D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local`
    - `make`
      - 参考[[make]], [[makefile]]
  - 结果
    - 则出现`build`下[[binary-executable]]
- [[configure-proxy]]
  - 在`CMakeLists.txt`开头增加
    ```cmake
    set(ENV{http_proxy} "某某")
    set(ENV{https_proxy} "某某")
    ```