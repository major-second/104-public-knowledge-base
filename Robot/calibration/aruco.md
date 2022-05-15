前置：
- ros中使用相机，即[[realsense-ros]]，[[usb-camera-ros]]等中一个
- 了解[[roslaunch]]修改和传递参数
- 打印机

fiducial markers是什么？[维基](https://en.wikipedia.org/wiki/Fiducial_marker)
ArUco就是一种fiducial marker
- [ArUco](https://docs.google.com/document/d/1QU9KoBtjSM2kF6ITOjQ76xqL7H0TEtXriJX5kwi9Kgc/edit)
  - [其ros包](https://github.com/pal-robotics/aruco_ros/tree/melodic-devel)，是一层封装
  - ros包readme也太简略了。好在[ArUco](https://docs.google.com/document/d/1QU9KoBtjSM2kF6ITOjQ76xqL7H0TEtXriJX5kwi9Kgc/edit)这里写了要`-DOpenCV_DIR`

安装
- [ArUco](https://docs.google.com/document/d/1QU9KoBtjSM2kF6ITOjQ76xqL7H0TEtXriJX5kwi9Kgc/edit)中搜索Compiling即可看到相关文档
- 但你不用全听他的。你明白他在做什么，就可以：
- 参考[[cmake]]中的[opencv链接](https://docs.opencv.org/4.2.0/d7/d9f/tutorial_linux_install.html)安装依赖OpenCV
- 参考[[install-ros-package]]所说的“多`git clone https://github.com/pal-robotics/aruco_ros.git`”
  - 其余命令参考[[install-ros-package]]不变
  - 注意版本号可能是`melodic`，就需要`-b`参数指定`melodic-devel`
- 即可用`catkin_make -DOpenCV_DIR=<pathTo-OpenCVConfig.cmake>`安装
  - 怎么找到那个文件`OpenCVConfig.cmake`？
  - 刚刚那个[opencv链接](https://docs.opencv.org/4.2.0/d7/d9f/tutorial_linux_install.html)让你在`/usr/local`装了
  - 所以你就`find /usr/local | grep CVConfig\.cmake`
  - 注意`grep`区分大小写
  - 最后显然不要用源码`/src`里的，要用`/usr/local/lib`里的

实体准备
- 下一节所说`single.launch`里能看到id为582，所以我们去https://chev.me/arucogen/
- ![](aruco-582.png)
- 100mm对应0.1m，在`single.launch`中需要改
- 点下方open打印成pdf
  - pdf再去打印机打印。注意不能缩放，完了之后要确认大小对不对

使用
- `roscd aruco_ros/launch`，`vim single.launch`
- 启动相机（比如[[realsense-ros]]）
- `rostopic`找相机相关的两个话题，填到`launch`文件中相应地方
  - 找`/camera_info`和`/image`
  - 如果你找不着`rect`的topic，可能还要改`image_is_rectified`为`False`
- （py2环境）`rosrun rqt_tf_tree rqt_tf_tree`
  - 看图，知道`camera_frame`，`reference_frame`参数应该填`camera_color_optical_frame`（因为这是单目相机）
  - 注意这里是最简单的setting：标定一个marker相对相机位置cd
- 根据上一节“实体准备”填写id和大小（注意单位是m）
- `rqt_image_view`看效果