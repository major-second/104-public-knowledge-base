在跑一个大实验之前，下载大东西等等之前
- 确认小规模没问题（存文件，checkpoint什么的）
- 确认断点、调试用的脚手架等都被去除了！
- 确认有没有[[silent]]（比如可能需要`y`确认，你没按，它一直等着，你晕不晕吧）
- 确认磁盘空间够不够
  - [[code-data-debug]]中我们经常有code和data分开的思想。常常把data链接到code文件夹下
  - 那么code文件夹下做数据预处理时，要小心存放目录不要在code的那个盘
  - 常见模式
    - code是`/home`，data是`/DATA/disk1`（外接的TB级的硬盘）
    - code是`/`，data是`/home`（参考[[dual-boot-partition]]）