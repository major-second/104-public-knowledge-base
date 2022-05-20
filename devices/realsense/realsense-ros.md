前置：
- [[realsense/installation]]
- [[create-catkin-ws]]

步骤
- `sudo apt-get install ros-$ROS_DISTRO-realsense2-camera`即可
  - [参考](https://github.com/IntelRealSense/realsense-ros)，[[build-from-source]]肯定很麻烦
- 验证
  - `roslaunch realsense2_camera rs_camera.launch`
  - `rostopic list`看发布的topic
    - 从而`rostopic echo <rostopic/path/to>/camera_info`看到相机内参
  - `rqt_image_view`对应topic看是否有图像