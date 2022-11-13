- grub菜单，指的是有`Ubuntu`，`Advanced options for Ubuntu`的那个菜单。样式特征很明显
![](grub-menu.png)
- 根据你选择boot设备不同，是在安装还是在正常启动，grub菜单选项当然不同
    - 如果是U盘boot安装，那么就会有`Install`之类的选项
    - 如果是正常启动，就类似上图
    - 内容是由[[grub-cfg]]决定的
- 这里下面有一些重要提示，比如小写`e`，小写`c`等。小写`e`可以编辑一些选项用来应急（单次boot有效），作为[[temp-solution]]
    - 之后永久生效需要成功安装系统后进入`/etc/default/grub`修改设置
    - 举例：[[windows-ubuntu]]中解决花屏
- 对于[[multiple-ubuntu-versions]]安装成功（或新增内核）后，在“旧系统”终端中（[[tty]]也行），`sudo update-grub`，可能就会出现这些提示
```text
<其他信息>
Found Ubuntu 18.04.6 LTS (18.04) on /dev/sda6
done
```
- 之后即可在“旧系统”对应[[grub-menu]]中看到新item，且在开机时可以选新系统