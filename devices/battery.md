- 电池寿命损耗
  - [参考](https://zhuanlan.zhihu.com/p/71376047)
  - [参考](https://zhuanlan.zhihu.com/p/136393393)
  - [参考surface官方文档](https://support.microsoft.com/zh-cn/surface/%E4%BF%9D%E5%85%BB-surface-%E7%94%B5%E6%B1%A0-9ccdfa7b-d074-f629-425c-1c090ac66bed)
    - 长期插电时最好维持在50%-60%，需要借助软件/固件等，甚至可能和[[bios]]有关
    - [[sleep-hibernate]]就很有帮助了。大部分时候插电，拔电前休眠
  - 一些概念
    - wear level
      - 相当于“上限”变小，全充满后，电池能使用的时间更少
      - 一些厂商虚标。比如出厂时，实际是标称的110%，标记成健康值100%，然后看着很久都是100%，结果一旦开始掉掉得很快
    - efficiency：使用更少的电池损耗，充上更多的电量
      - 比如20% - 80%这种efficiency高
      - 80% - 100% 这种efficiency巨低
      - 所以最忌讳的就是用一点就去充，用一点就去充，频繁在高电量附近充
    - 参考资料（来自[这里](https://accubattery.zendesk.com/hc/en-us/articles/209507189-Tab-3-battery-health-screen)）
      - ![](wear-efficiency.png)
      - 举例
      - ![](efficiency-example.png)例子中，用0.10充了15%，efficiency就是1.5
  - 深度充放电（太低电才充，然后充得太满）会损害锂电池
    - 以前老旧的镍镉电池可能反而需要深度充放电。但现在时代变了！
    - 搜索“记忆效应”
  - 电池管理方法（怎么长期保持50-60%？）
    - 手动插拔
    - 手机app如
      - 安卓[[android/battery]]中的
      - 苹果
        - 寿命检测：iOS高版本系统设置-battery中自带
        - 充电闹钟：随便搜搜`Battery Alarm`等[[apple-app]]
    - 电脑软件和设置如[[power-options]]中的
  - 注意无线充电不要买劣质的/用非原装的，否则发热过大，损害电池
  - 电池老化后关机也会掉电
- 省电
  - 参考[[power-options]], [[android/battery]]
  - 注意省电和延长寿命有时并不是一致的