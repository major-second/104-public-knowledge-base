前置：
- ros中使用相机，即[[realsense-ros]]，[[usb-camera-ros]]等中一个
- 打印

fiducial markers是什么？[维基](https://en.wikipedia.org/wiki/Fiducial_marker)
例子：[ArUco](https://docs.google.com/document/d/1QU9KoBtjSM2kF6ITOjQ76xqL7H0TEtXriJX5kwi9Kgc/edit)
安装
- 参考[[install-ros-package]]所说的“多`git clone https://github.com/pal-robotics/aruco_ros.git`”即可**尝试**安装
  - 注：对于melodic，需要进去`git checkout -b melodic-level`
- 但直接尝试会`catkin_make`失败，提示没有`OpenCV 4.2.0`
  - 参考[[cmake]]中的[链接](https://docs.opencv.org/4.2.0/d7/d9f/tutorial_linux_install.html)安装依赖即可