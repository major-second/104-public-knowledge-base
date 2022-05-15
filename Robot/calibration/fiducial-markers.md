前置：
- ros中使用相机，即[[realsense-ros]]，[[usb-camera-ros]]等中一个
- 打印机（todo）

fiducial markers是什么？[维基](https://en.wikipedia.org/wiki/Fiducial_marker)
例子：
- [ArUco](https://docs.google.com/document/d/1QU9KoBtjSM2kF6ITOjQ76xqL7H0TEtXriJX5kwi9Kgc/edit)
  - [其ros包](https://github.com/pal-robotics/aruco_ros/tree/melodic-devel)，是一层封装
  - ros包readme也太简略了。好在[ArUco](https://docs.google.com/document/d/1QU9KoBtjSM2kF6ITOjQ76xqL7H0TEtXriJX5kwi9Kgc/edit)这里写了要`-DOpenCV_DIR`

安装
- [ArUco](https://docs.google.com/document/d/1QU9KoBtjSM2kF6ITOjQ76xqL7H0TEtXriJX5kwi9Kgc/edit)中搜索Compiling即可看到相关文档
- 但你不用全听他的。你明白他在做什么，就可以：
- 参考[[cmake]]中的[opencv链接](https://docs.opencv.org/4.2.0/d7/d9f/tutorial_linux_install.html)安装依赖OpenCV
- 参考[[install-ros-package]]所说的“多`git clone https://github.com/pal-robotics/aruco_ros.git`”
- 即可用`catkin_make -DOpenCV_DIR=<pathTo-OpenCVConfig.cmake>`安装
  - 怎么找到那个文件`OpenCVConfig.cmake`？
  - 刚刚那个[opencv链接](https://docs.opencv.org/4.2.0/d7/d9f/tutorial_linux_install.html)让你在`/usr/local`装了
  - 所以你就`find /usr/local | grep CVConfig\.cmake`
  - 注意`grep`区分大小写
  - 最后显然不要用源码`/src`里的，要用`/usr/local/lib`里的