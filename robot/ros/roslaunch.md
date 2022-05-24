前置：
- [[xml]]

- 使用`xml`语法设置参数。`xml`和`roslaunch`命令之间有对应关系
  - 所以一个`launch`文件可以同时launch多个`launch`文件。相当于打包
- 常见模式：`arg`传给`param`，而`arg`可以用命令行的`:=`语法传
  - 具体：[[hand-eye-calibration]]提到`roslaunch panda_moveit_config panda_control_moveit_rviz.launch robot_ip:=172.16.0.2`对应的`xml`是
```xml
    <include file="$(find panda_moveit_config)/launch/panda_control_moveit_rviz.launch">
        <arg name="robot_ip" value="172.16.0.2" />
    </include>
```
- 注：我们可以使用`$(find ...)`，这个不是[[find-grep]]的`find`，而是`rospack find`，参考[[file-system]]
- 自己写简单的launch文件：参考[[hand-eye-calibration]]
  - 一种是直接复制现有的，改一些`arg`和`param`（`ArUco`一节）
  - 一种是`<include>`（相当于套娃`launch`）
  - 前者更加低层，可以控制`param`，后者不行