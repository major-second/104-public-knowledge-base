前置：
- [[create-catkin-ws]]

[官网教程](http://wiki.ros.org/ROS/Tutorials/NavigatingTheFilesystem)
- `rospack find`跟包名
- `roscd`，`rosls`直接跳过前置各层路径，从包名开始（例如`rosls panda_moveit_config/launch/`），也可以tab补全
  - `roscd log`：如果有过log，可以看log
> Note that roscd, like other ROS tools, will only find ROS packages that are within the directories listed in your ROS_PACKAGE_PATH

为了保证`ROS_PACKAGE_PATH`正确，这些命令能使用，请注意[[create-catkin-ws]]和[[ros/installation]]等提到的`source`命令
具体地
```sh 
source /opt/ros/melodic/setup.bash #或zsh等
source ~/catkin_ws/devel/setup.bash
```