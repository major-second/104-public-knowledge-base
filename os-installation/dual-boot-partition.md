## preparation
- 开始菜单 - 搜索hard disk - 打开![](dual-boot-partition/hard-disk-win10.png)
在出来的界面中可以添加、删除、压缩卷等
比如在unallocated的部分，可以添加卷![](dual-boot-partition/add.png)
- for dual-boot:
腾出unallocated的磁盘空间
  - unallocated就是不对应任何分区。不能说“我现在弄个`E:`盘等下用来装Ubuntu
  - 要腾出成“黑色”如图![](dual-boot-partition/unallocated.png)
  - [[vmware/settings]]里也有类似的unallocated状态
  - if there're 2 hard disks: for the SSD (the one with windows boot manager), leave out 200M, for the other (HDD, "main data disk"), leave out >100G
## during installation
- ![](dual-boot-partition/partition.png)
- minimal: 4 partitions
- for all, choose "from the beginning"
  - efi, primary, efi system, 200M
    - in `C:\\` in windows there's also such a partition.
  - /, primary, ext4, 20G
    - just like `Program Files` in windows
  - swap, logical, swap, 2 * RAM size
  - /home, logical, ext4, 100G
    - just like `Data (D:)` in windows