前置：
- [[franka-ros]]
- [[connect-controller]]

步骤
- 其实搞定前置后，如果不是`4.2.0`以上版本（参考[文档](https://frankaemika.github.io/docs/getting_started.html#preparing-the-robot-for-fci-usage-in-desk)），就已经可以用了。否则参考文档
- 验证：
  - [[libfranka]]目录（`/build`里）
    - `./examples/echo_robot_state <fci-ip>`
    - 同样地方`./examples/communication_test <fci-ip>`（需要蓝灯）
      - 如果延迟太高，可能直接一来就失败。参考[[troubleshooting]]
  - [ros可视化确认安装](https://frankaemika.github.io/docs/franka_ros.html#ros-visualization)
    - `roslaunch franka_visualization franka_visualization.launch robot_ip:=172.16.0.2 load_gripper:=true`
      - 注：因为`franka_visualization`是`franka_ros`里的东西，所以（如果你`franka_ros`在catkin_ws里就）需要`source`你catkin_ws里的`devel/setup.bash`
    - [[connect-base]]中提到过怎么移动。你一边动就可以一边看到visualize结果了