[参考](https://zhuanlan.zhihu.com/p/262069479)
总之efi继承mbr，一个硬盘中可能有许多（用于[[dual-boot/steps]]），在bios可调整优先级，可用于引导系统启动
新电脑基本都是uefi模式
- 如win10的efi专用于启动win10
- ubuntu的efi可用于切换启动win10或ubuntu（但注意[[risk]]）
- [[u-disk-boot]]也有对应的efi用于临时进入u盘中的ubuntu
- 典型的对efi的操作：一般需要win10 diskpart命令，参考[[partition]]
  - [在win10 efi中删除ubuntu相关东西](https://blog.csdn.net/Cl2212/article/details/111304470)
  - 删除ubuntu的efi（用于重装ubuntu等）：`select`到指定partition后，`delete partition override`