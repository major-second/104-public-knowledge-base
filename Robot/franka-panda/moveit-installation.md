前置
- [[ros/installation]]
- 已有或新建[[create-catkin-ws]]

安装
- 文档
http://docs.ros.org/en/melodic/api/moveit_tutorials/html/doc/getting_started/getting_started.html
`sudo apt install ros-melodic-moveit`
- 之后不要照文档，而是应该微调[[franka-ros]]的安装步骤，增加
```sh 
git clone https://github.com/ros-planning/moveit_tutorials.git -b melodic-devel
git clone https://github.com/ros-planning/panda_moveit_config.git -b melodic-devel
```
- 原理是[[catkin-make]]一般来说都是一次make所有。我们应该全部准备好，一起`make`
参考[[install-ros-package]]
- 具体地，如果你已经初始化了
那么就
```sh
cd path/to/catkin_ws # 有一些前置步骤，具体参考文档
git clone --recursive https://github.com/frankaemika/franka_ros src/franka_ros
cd src
git clone https://github.com/ros-planning/moveit_tutorials.git -b melodic-devel
git clone https://github.com/ros-planning/panda_moveit_config.git -b melodic-devel
cd franka_ros
git checkout <version>
cd ../..
rosdep install --from-paths src --ignore-src --rosdistro melodic -y --skip-keys libfranka
catkin_make -DCMAKE_BUILD_TYPE=Release -DFranka_DIR:PATH=/path/to/libfranka/build
source devel/setup.sh
```
- 当然可以看到文档的命令和我们这里的命令有对应关系
  - `-DCMAKE_BUILD_TYPE=Release`对应了
  - `rosdep`那句运行的地方，此处和文档不同

rviz可视化
- 直接对着[文档](http://docs.ros.org/en/melodic/api/moveit_tutorials/html/doc/quickstart_in_rviz/quickstart_in_rviz_tutorial.html#getting-started)即可
  - 命令`roslaunch panda_moveit_config demo.launch rviz_tutorial:=true`，之后参考文档进行操作
  - 注意可以保存界面设置，方便下次复现
- 不过这个不是真机