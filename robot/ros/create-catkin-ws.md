前置：
- [[ros/installation]]

[官网教程1](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment)
[官网教程2](http://wiki.ros.org/catkin/Tutorials/create_a_workspace)
其实差不多
- 注意必须先`source /opt/ros/melodic/setup.bash`（以melodic为例）
  - 此命令不能在`sudo su`中运行
  - 之后`catkin_ws`不能在必须要[[sudo]]权限的地方
  - 故典型可行的就是在`~`
  - 当然，如果你已经加到`~/.bashrc`，那就不用手动运行了
- 之后跟着官网指令即可
- 注意最后`source devel/setup.bash`（也可以写到`~/.bashrc`）
- 检查：`echo $ROS_PACKAGE_PATH`看效果
  - 例如`/home/<用户名>/catkin_ws/src:/opt/ros/melodic/share`就表示
    - 先看用户自己这边的包
    - 再看`/opt/ros`的包（往往是`apt`装的）