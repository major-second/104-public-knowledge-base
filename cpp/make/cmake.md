- 安装：`sudo apt install cmake`
- 使用
  - 到项目根目录（一般下属`src`等等）
  - `mkdir build && cd build`
  - `cmake ..`
  - `make`
  - 则出现可执行文件
- 如果一次失败后，可能需要把部分多余的（`devel, build`等）删除再重试，参考[[general-programming/cache]]
- [[configure-proxy]]
  - 在`CMakeLists.txt`开头增加
    ```cmake
    set(ENV{http_proxy} "某某")
    set(ENV{https_proxy} "某某")
    ```
- 可能需要[[sudo]]权限
- `-D`用来添加参数，格式为`-DKEY=value`
  - 示例：[OpenCV](https://docs.opencv.org/4.2.0/d7/d9f/tutorial_linux_install.html)
  - `-DCMAKE_BUILD_TYPE=Debug`：可能用于生成debug的用于[[gdb]]