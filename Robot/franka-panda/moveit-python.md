前置：
- [[moveit-installation]]
  - 如果需要真机则[[moveit-real-robot]]

步骤
- 无论是真机还是虚拟，都先`roslaunch`一个`panda_moveit_config`里的东西（参考[[moveit-installation]]和[[moveit-real-robot]]）
- 然后`rosrun moveit_tutorials move_group_python_interface_tutorial.py`
  - 注意这个运动动作有点大，其实你**最好**可以只看看[代码](https://github.com/ros-planning/moveit_tutorials/blob/melodic-devel/doc/move_group_python_interface/scripts/move_group_python_interface_tutorial.py)，不要实际运行
    - 最好是跳过这份脚本，直接执行这个文件夹下`moveit-python/minimum_example*.py`
  - 需要用默认`python2.7`，也就是如果你在`conda`环境里需要`conda deactivate`
    - 此时使用`python`命令直接运行脚本，和`rosrun`的效果是一致的
  - 该脚本停止是`Ctrl+D`键不是`Ctrl+C`
- 注：关于`moveit-python`文件夹下的`.py`脚本来源：我们直接
  - `roscd moveit_tutorials`
  - `find . | grep move_group_py`（参考[[find-grep]]）
  - 把对应`move_group_python_interface_tutorial.py`文件复制。结果是我们目前这个文件夹下的`moveit_python/original_tutorial.py`
  - 其他`.py`都是基于它的
- 注意[[troubleshooting]]中的：如果失败尝试重启`roslaunch`，排查延迟等等