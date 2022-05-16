前置：
- [[realsense/installation]]
- [[create-catkin-ws]]

步骤
- `catkin_ws/src`中额外`git clone https://github.com/intel-ros/realsense.git`即可。其它参考[[moveit-installation]]
- 验证
  - `roslaunch realsense2_camera rs_camera.launch`
  - `rostopic list`看发布的topic
    - 从而`rostopic echo <rostopic/path/to>/camera_info`看到相机内参
  - `rqt_image_view`对应topic看是否有图像