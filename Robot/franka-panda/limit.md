- 到了诡异的位置（关节到接近**硬件**极限），就动不了了
  - 需要白灯，复位到合理位置，再蓝灯
    - 到底是谁接近了极限？终端里会有黄色警告
    - 复位时要特别小心，否则白灯会变红灯，需要重新开锁，再尝试复位
  - 注：此时要重新`roslaunch`，参考[[troubleshooting]]
- 怎么永久消除接近**硬件**极限的风险？
  - 我们百度知道有`soft*limit`这个东西的存在，于是到[[create-catkin-ws]]创建出的空间中，凭感觉，一搜`find . -type f | grep franka | xargs grep soft | grep limit`就搜到在哪了
  - 在`./src/franka_ros/franka_description/robots/panda_arm.xacro:      <safety_controller k_position="100.0" k_velocity="40.0" soft_lower_limit="-2.8973" soft_upper_limit="2.8973"/>`，我们直接`vim`进去改那些数值即可（比如`2.8973`改成`2.7973`）
- 改完了确认
  - 可以[[moveit-real-robot]]中左侧这个界面确认limit确实被修改了（不过要弧度转角度）![](moveit-limit.png)
  - 还可以`diff ./src/franka_ros/franka_description/robots/panda_arm.xacro ./src/franka_ros/franka_description/robots/panda_gazebo.xacro | grep safety_controller -C 2`进行确认我们确实都是改保守了
    - 参考[[xxd-diff]]，[[find-grep]]
    - 正确效果
```text
> 
64c61
<       <safety_controller k_position="100.0" k_velocity="40.0" soft_lower_limit="-2.7973" soft_upper_limit="2.7973"/>
---
>       <safety_controller k_position="100.0" k_velocity="40.0" soft_lower_limit="-2.8973" soft_upper_limit="2.8973"/>
69c66,67
<       <limit effort="87" lower="-2.8973" upper="2.8973" velocity="2.1750"/>
--
> 
97c93
<       <safety_controller k_position="100.0" k_velocity="40.0" soft_lower_limit="-1.6628" soft_upper_limit="1.6628"/>
---
>       <safety_controller k_position="100.0" k_velocity="40.0" soft_lower_limit="-1.7628" soft_upper_limit="1.7628"/>
102c98,99
<       <limit effort="87" lower="-1.7628" upper="1.7628" velocity="2.1750"/>
```
- 有趣的是，gripper有时也会到极限（张太大），手动往里推再Homing即可