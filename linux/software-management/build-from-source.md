即下载源码（用户级源码一般可以放到`/usr/local/src`），通过下载的源码构建到`/usr/local`

比如[[libfranka]]的build，本质上是
- `git clone`（参考[[git/installation]]）
- [[checkout]]指定版本
- `git submodule update`来更新[[submodule]]
- 用[[cmake]]从源码build
  - 一般都是`mkdir build && cd build`，进去之后再`cmake`
  - 所以失败了要把这个`build`文件夹删除新建再`cd`进去操作！不能残留之前的
- 结果在`build`文件夹里。比如[[fci]]里就用了`/path/to/libfranka/build/examples/echo_robot_state`

比如[[franka-ros]]的build用了比[[cmake]]高一层的[[catkin-make]]，需要[[create-catkin-ws]]