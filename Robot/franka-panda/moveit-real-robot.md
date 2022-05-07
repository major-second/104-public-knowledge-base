前置
- [[fci]]
- [[moveit-installation]]
- 机械臂蓝灯亮

步骤
- 这里和[[moveit-installation]]中命令的唯一区别就是`roslaunch panda_moveit_config`后面跟的指令不同
  - 其它的，你会动虚拟机械臂就也会动真实机械臂！非常爽
  - 注意一定要![](speed-limit.png)限速！手时刻拿软紧急制动！否则非常危险！
    - 如果猛地撞墙，很有可能就报错红灯亮了！只能[[on-off]]重启，并在[[control-using-desk]]修复错误
    - 如果制动了，则粉色灯亮，则需要白灯再蓝灯，从而参考[[troubleshooting]]需要重新`roslaunch`
  - 即：rviz操作、保存等和[[moveit-installation]]相同
- [[moveit-installation]]中的`demo.launch`和我们这里需要的`panda_moveit_config demo.launch`显然是并列关系
  - 参考https://github.com/ros-planning/panda_moveit_config/tree/melodic-devel/launch
  - 具体命令：`roslaunch panda_moveit_config panda_control_moveit_rviz.launch robot_ip:=172.16.0.2`