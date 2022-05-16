## 基本操作
- win10: 开始菜单 - 搜索hard disk - 打开![](partition/hard-disk-win10.png)
在出来的界面中可以添加、删除、压缩卷等
比如在unallocated的部分，可以添加卷![](partition/add.png)
- Ubuntu: `sudo apt install gparted`, `sudo gparted`
## unallocated状态
- unallocated就是目前不对应任何分区
  - 比如，装双系统时，不能说**我现在弄个`E:`盘等下用来装Ubuntu**，因为这样这部分空间就被Win占用了
- 腾出unallocated的磁盘空间：
  - 如win10，要腾出成“黑色”如图![](partition/unallocated.png)
  - [[vmware/settings]]里也有提到类似的unallocated状态
- 注：双系统需求：if there're 2 hard disks:
  - for the SSD (the one with windows boot manager), leave out 200M
  - for the other (HDD, "main data disk"), leave out >100G
## 刚刚装双系统时手动分区
- ![](partition/partition.png)
- minimal: 4 partitions
- for all, choose "from the beginning"
  - efi, primary, efi system, 200M
    - in `C:\\` in windows there's also such a partition.
  - /, primary, ext4, 20G
    - just like `Program Files` in windows
  - swap, logical, swap, 2 * RAM size
    - 中文“交换分区”
  - /home, logical, ext4, 100G
    - just like `Data (D:)` in windows