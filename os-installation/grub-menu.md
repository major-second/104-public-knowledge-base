grub菜单，指的是有`Ubuntu`，`Advanced options for Ubuntu`的那个菜单。样式特征很明显
![](grub-menu.png)
根据你选择boot设备不同，是在安装还是在正常启动，grub菜单选项当然不同。
如果是U盘boot安装，那么就会有`Install`之类的选项。如果是正常启动，就类似上图
这里下面有一些重要提示，比如小写`e`，小写`c`等。小写`e`可以编辑一些选项用来应急（单次boot有效）
之后永久生效需要成功安装系统后进入`/etc/default/grub`修改设置