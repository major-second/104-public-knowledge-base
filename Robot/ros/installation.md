这是`melodic`版本（比较古早）
版本是按照字母排列的
上http://wiki.ros.org/melodic/Installation/Ubuntu#Installation，对着不断输入命令即可
可能需要[[linux]]翻墙

注意1.5节中提到：多个ros版本只能`source`一个`setup.bash`
如果你用[[zsh]]那么当然要`source`的（以及把`source`语句加到的文件）有区别

## 验证安装成功
一个终端`roscore`
另一个终端`rqt_graph`，去掉hide中的勾选，看到`/rosout`
![](installation-rqt-graph.png)