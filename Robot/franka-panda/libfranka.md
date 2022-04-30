前置
- [[linux-kernel]]（需要实时内核），[[rt-kernel-gpu]]
- [[ros/installation]]
- 知道机械臂中软件版本号（比如可以[[connect-controller]]上去看）

步骤
- [这里根据机械臂中软件版本号查询需要的其他软件版本号](https://frankaemika.github.io/docs/compatibility.html)
  - 注：如果你用Ubuntu 18.04和[[ros/installation]]的`melodic`版本，那么需要`apt-cache madison ros-melodic-libfranka`看有没有你需要的版本号。以此类推
  - 如果没有，就只能手动[[build-from-source]]，参考[官网教程](https://frankaemika.github.io/docs/installation_linux.html#building-from-source)