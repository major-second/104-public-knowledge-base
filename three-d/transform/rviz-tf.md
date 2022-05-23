前置：
- [[moveit-installation]]中的rviz基本用法

如何可视化transform
- rviz窗口（比如[[moveit-installation]]里的）
  - `Displays - Add`中可以加Axes，其中`Reference Frame`，`Length`，`Radius`参数含义都很直观
  - 加`TF`则能可视化所有坐标系
- py2环境中`rosrun rqt_tf_tree rqt_tf_tree`看`tf_tree`
- `TF`结合`rqt_tf_tree`，可以直观在[[hand-eye-calibration]]等复杂过程中看到各个frame的关系
  - 有相机的一系列frame，有机械臂的一系列frame，如果没有标定，那么自然就各自独立，没法在rviz的`TF`中标出，强行打开`TF`会有警告
- 实践：查看`camera_link`和其他相机frame的关系
  - `Global Options`中改Fixed Frame为`camera_link`
  - 其它地方比如`Grid`等相应修改
  - `TF - Frames`中可以打钩和去掉钩等，看关系
  - 对于[[realsense-ros]]，我们看到`camera_link`和`*optical*`之间原点相同，轴不同