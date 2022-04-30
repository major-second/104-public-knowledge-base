前置
- 知道机械臂中软件版本号（比如可以[[connect-controller]]上去看）
- [[libfranka]]

步骤
- 就像[[libfranka]]. 有就直接`apt`装，没有就[[build-from-source]]
  - 可能需要参考[[create-catkin-ws]]，不过这里教程其实涵盖了create

教程的初始化
```sh 
cd /path/to/desired/folder
mkdir -p catkin_ws/src
cd catkin_ws
source /opt/ros/melodic/setup.sh
catkin_init_workspace src
```
- 总体看[这个](https://frankaemika.github.io/docs/installation_linux.html#building-the-ros-packages)，但是不能教条。参考[[read-doc]]
  - 版本不一定是`kinetic`
  - 过程中有一些转移目录的`cd`指令没写
  - 有些`/path/to`等需要自己填上

比如我们可能是
```sh
cd path/to/catkin_ws # 有一些前置步骤，具体参考文档
git clone --recursive https://github.com/frankaemika/franka_ros src/franka_ros
cd src/franka_ros
git checkout <version>
cd ../..
rosdep install --from-paths src --ignore-src --rosdistro melodic -y --skip-keys libfranka
catkin_make -DCMAKE_BUILD_TYPE=Release -DFranka_DIR:PATH=/path/to/libfranka/build
source devel/setup.sh
```

- 装完之后可以参考[[install-ros-package]]