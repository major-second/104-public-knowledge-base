前置
- 已有或新建[[create-catkin-ws]]
- 如果是用于控制真机需要[[franka-ros]]

安装
- 文档
http://docs.ros.org/en/melodic/api/moveit_tutorials/html/doc/getting_started/getting_started.html
  - 必做的：文档的
  - `sudo apt-get install ros-melodic-catkin python-catkin-tools`
  - `sudo apt install ros-melodic-moveit`
  - 我犯了的错误：想当然以为有`catkin_make`命令就说明`sudo apt-get install ros-melodic-catkin python-catkin-tools`可以省略。其实不行！
- 之后（如果你需要控制真机）不要照文档，而是应该微调[[franka-ros]]的安装步骤，增加
```sh 
git clone https://github.com/ros-planning/moveit_tutorials.git -b melodic-devel
git clone https://github.com/ros-planning/panda_moveit_config.git -b melodic-devel
```
- 原理是[[catkin-make]]一般来说都是一次make所有。我们应该全部准备好，一起`make`
  - 参考[[install-ros-package]]
  - 总之就是这里的教程只是告诉你通过什么命令可以多装这个包。如果你有原来就需要装的包那么就是incremental改动命令
  - 注意`-D`参数也是incremental添加的。参考阅读[[basic-syntax]]
- 具体地，如果你已经初始化了
那么就
```sh
cd path/to/catkin_ws # 有一些前置步骤，具体参考文档
cd src
git clone --recursive https://github.com/frankaemika/franka_ros franka_ros
git clone https://github.com/ros-planning/moveit_tutorials.git -b melodic-devel
git clone https://github.com/ros-planning/panda_moveit_config.git -b melodic-devel
# 这里可能再加入其它包
cd franka_ros
git checkout <version>
cd ../..
rosdep install --from-paths src --ignore-src --rosdistro melodic -y --skip-keys libfranka
catkin_make -DCMAKE_BUILD_TYPE=Release -DFranka_DIR:PATH=</path/to/>libfranka/build
source devel/setup.sh
```
- 当然可以看到文档的命令和我们这里的命令有对应关系
  - `-DCMAKE_BUILD_TYPE=Release`有对应
  - `rosdep`那句运行的所在目录，此处和文档不同（但有对应）

rviz可视化
- 直接对着[文档](http://docs.ros.org/en/melodic/api/moveit_tutorials/html/doc/quickstart_in_rviz/quickstart_in_rviz_tutorial.html#getting-started)即可
  - 命令`roslaunch panda_moveit_config demo.launch rviz_tutorial:=true`，之后参考文档进行操作
  - 注意可以保存界面设置，方便下次复现
- 这个不是真机。但和真机区别很小，参考[[moveit-real-robot]]
- `[ERROR] [1652916881.887429384]: Exception while loading planning adapter plugin 'default_planner_request_adapters/ResolveConstraintFrames': According to the loaded plugin descriptions the class default_planner_request_adapters/ResolveConstraintFrames with base class type planning_request_adapter::PlanningRequestAdapter does not exist. Declared types are  default_planner_request_adapters/AddIterativeSplineParameterization default_planner_request_adapters/AddTimeOptimalParameterization default_planner_request_adapters/AddTimeParameterization default_planner_request_adapters/Empty default_planner_request_adapters/FixStartStateBounds default_planner_request_adapters/FixStartStateCollision default_planner_request_adapters/FixStartStatePathConstraints default_planner_request_adapters/FixWorkspaceBounds`错误可以忽略