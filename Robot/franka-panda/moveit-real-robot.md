前置
- [[fci]]
- [[moveit-installation]]
- 机械臂蓝灯亮

步骤
- 这里和[[moveit-installation]]唯一区别就是`roslaunch panda_moveit_config`后面跟的指令不同
  - 参考https://github.com/ros-planning/panda_moveit_config/tree/melodic-devel/launch
  - [[moveit-installation]]中的`demo.launch`和我们这里需要的`panda_moveit_config demo.launch`显然是并列关系
- 命令`roslaunch panda_moveit_config panda_control_moveit_rviz.launch robot_ip:=172.16.0.2`
- rviz操作、保存等和[[moveit-installation]]相同