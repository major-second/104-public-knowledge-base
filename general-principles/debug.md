- 在正式运行前，往往需要先调试确认没有问题。调试时往往
  - 使用较少资源（gpu、cpu等）和待测试数据，降低成本，加快调试迭代速率
  - 使用较简单的模式
    - 比如单线程，而不用distributed data parallel, ddp等
      - 多线程时，打一个断电会被断多次，使得调试过程不够清晰，参考[[breakpoint]]
      - 报错也会更模糊，例如[[make]]中的`-j8`会导致报错被“埋起来”
- 在跑一个大实验之前，下载大东西等等之前要做的调试
  - 确认小规模没问题
    - 存文件，checkpoint什么的
    - 以及有没有本质上的一些错误
      - 比如[[hand-eye-calibration]]可以先跑少数几个点看结果靠不靠谱，排除选错坐标系等情况
  - 确认断点、调试用的脚手架等都被去除了！要不然跑了一晚上，早上起来发现卡在断点，尴尬
  - 确认有没有[[silent]]（比如可能需要`y`确认，你没按，它一直等着，你晕不晕吧）
  - 确认磁盘空间够不够
    - [[code-data-debug]]中我们经常有code和data分开的思想。常常把data链接到code文件夹下
    - 那么code文件夹下做数据预处理时，要小心存放目录不要在code的那个盘
    - 常见模式
      - code是`/home`，data是`/DATA/disk1`（外接的TB级的硬盘）
      - code是`/`，data是`/home`（参考[[partition]]）
  - 有自己独占的就不要用和别人共用的。万一[[isolation]]没做好，对面来个新手把服务器搞崩了，就好玩了