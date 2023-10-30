是一些常用小工具
可视化
- `rqt_image_view`看各种相机出图，包括[[aruco]]，[[hand-eye-calibration]]监视情况
- `rqt_graph`节点间关系图
- py2环境`rosrun rqt_tf_tree rqt_tf_tree`
  - 很多小工具都有刷新按钮。不刷新可能导致[[hand-eye-calibration]]提到的“其实还没完全启动你就直接开始take sample导致crash”之类后果