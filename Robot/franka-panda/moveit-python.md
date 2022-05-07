前置：
- [[moveit-installation]]
  - 如果需要真机则[[moveit-real-robot]]

步骤
- 无论是真机还是虚拟，都先`roslaunch`一个`panda_moveit_config`里的东西（参考[[moveit-installation]]和[[moveit-real-robot]]）
- 然后`rosrun moveit_tutorials move_group_python_interface_tutorial.py`
  - 注意这个的机械臂运动动作有点大，其实你**最好**可以只看看[代码](https://github.com/ros-planning/moveit_tutorials/blob/melodic-devel/doc/move_group_python_interface/scripts/move_group_python_interface_tutorial.py)，不要实际运行
    - 最好是跳过这份脚本，直接执行这个文件夹下比较安全的`moveit-python/minimum_example*.py`
    - 注：里面的`set_max_velocity*`（限速）函数我们怎么找到的？参考[[find-grep]]
      - `cd /opt/ros/melodic`
      - `find . -type f -name "*.py" -print0 | xargs -0 grep set_max_velocity`
      - 当然百度说不定也能找到
      - 当然[C++ Interface](https://docs.ros.org/en/melodic/api/moveit_tutorials/html/doc/move_group_interface/move_group_interface_tutorial.html)也能找到。很多东西和python Interface是有对应关系的，然后C++ Interface文档显然更全
  - 需要用默认的`python2.7`，也就是如果你在`conda`环境里需要`conda deactivate`
    - 此时使用`python`命令直接运行脚本，和前面的`rosrun`的效果是一致的
  - 该脚本停止是`Ctrl+D`键不是`Ctrl+C`
- 注：关于`moveit-python`文件夹下的`.py`脚本来源：我们直接
  - `roscd moveit_tutorials`
  - `find . | grep move_group_py`（参考[[find-grep]]）
  - 把对应`move_group_python_interface_tutorial.py`文件复制。结果是我们目前这个文件夹下的`moveit_python/original_tutorial.py`
  - 其他`.py`都是基于它的
- 注意[[troubleshooting]]中的：如果失败
  - 尝试重启`roslaunch`
  - 白灯，手动复位，蓝灯（当然同时要重启`roslaunch`）
  - 排查延迟
  - 等等