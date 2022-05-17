即下载源码（用户级源码一般可以放到`/usr/local/src`），通过下载的源码进行构建
参考[[make]]，[[cmake]]，[[catkin-make]]等等
- 比如[[libfranka]]的build，本质上是
  - `git clone`（参考[[git/installation]]）
  - [[checkout]]指定版本
  - `git submodule update`来更新[[submodule]]
  - 用[[cmake]]从源码build
  - 结果在`build`文件夹里。比如[[fci]]里就用了`/path/to/libfranka/build/examples/echo_robot_state`
- 比如[[franka-ros]]的build用了比[[cmake]]高一层的[[catkin-make]]，需要[[create-catkin-ws]]
- 比如[[realsense/installation]]中[[cmake]]后又进行了[[make]]