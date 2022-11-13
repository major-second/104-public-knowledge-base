一个示例：[OpenCV](https://docs.opencv.org/4.2.0/d7/d9f/tutorial_linux_install.html)
- 一般是先
  - `mkdir build && cd build`，进去之后再`cmake`
    - 所以失败了要把这个`build`文件夹删除新建再`cd`进去操作！不能残留之前的
    - 注：[[catkin-make]]也同理。而且除了`build`可能还有`devel`要删除
      - 参考[[general-principles/cache]]
  - 往往`cmake`之后再`make`再`make install`，才能增加可用的shell命令。参考[[make]]
- 代理设置：在`CMakeLists.txt`开头增加
```cmake
set(ENV{http_proxy} "某某")
set(ENV{https_proxy} "某某")
```
- 可能需要[[sudo]]权限
- `-D`用来添加参数，格式为`-DKEY=value`