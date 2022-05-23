前置
- [[file-system]]

[官网教程](http://docs.ros.org/en/melodic/api/moveit_tutorials/html/doc/move_group_python_interface/move_group_python_interface_tutorial.html)
其实`rosls 包名`，找到`.py`脚本文件名，然后`rosrun 包名 文件名.py`的效果，完全相当于`roscd 包名`再`python 文件名.py`
换句话说如果只是运行`python`脚本就不需要[[create-ros-package]]，非常方便