前置：
- [[linux]]翻墙
- 针对`raw.githubusercontent.com`修改[[hosts]]（因为`rosdep init`的[[configure]]很麻烦）
- [[source]]
  - 除了需要加ros的源，可能还要改默认源为阿里云（默认源缺包

这是`melodic`版本（比较古早）版本是按照字母`a`开始排列的
上http://wiki.ros.org/melodic/Installation/Ubuntu#Installation，对着不断输入命令即可
- 如果你用[[zsh]]那么，要`source`的文件（以及需要把`source`语句加到的文件）都有区别
- 注意1.5节中提到：多个ros版本只能`source`一个`setup.bash`
  - 那我们就认准`melodic`吧
## 验证安装成功
一个终端`roscore`
另一个终端`rqt_graph`，去掉hide中的勾选，看到`/rosout`
![](installation-rqt-graph.png)