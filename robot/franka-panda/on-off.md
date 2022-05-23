前置：
- 硬件上安装好franka机械臂：[教程，看第一个视频](https://mp.weixin.qq.com/mp/homepage?__biz=MzI1MDQyMTQ2Mw==&hid=2&sn=b0ae69e54148897202a821d0a48d79e9&scene=1&devicetype=android-29&version=28000653&lang=zh_CN&nettype=3gnet&ascene=7&session_us=gh_8f8e4c6a8bf8&pass_ticket=v3fxJbAjVoDUxQTg9j07UZ1xyvu8oHbx4Mk%2F5beeCBiI87W8PE%2FgLDbCygl6zF0M&wx_header=1&from=groupmessage)
  - 参考：[[螺丝]]
  - 其中需要防漏电的**德标**转接头（观察你的插头，除了两个凸棒，还有一个凹孔用来接地！否则会漏电）
  - 功率：参考手册：Franka Emika Robot必须在平均功率介于140 - 350W的情况下才能进行标准操作。电源所产生的电功率可能瞬间高达600W. 功率不够可能开不了机
    - 所以请不要和太多高功率电器共享一个排插，否则开机会很难，可能很多次才能成功一次
  - 网线不能吝啬！一定要买最好的，否则到时候`ping`延迟太高，`communication_test`成功不了

开关等方法
- 开机：按控制柜处开关（在控制柜电源线一面），`-`字按下是开
  - 此时红色紧急按钮不能处于按下状态，否则开不了
  - 先观察到黄灯闪烁，停止了才是开好
- 关机：最好通过[[connect-base]]连接上，登录操作关机
  - 如果实在不行，只能先握手刹让粉色灯亮，再控制箱强关
- 重启：关机之后等一小会（几分钟吧），再按按钮开机
  - 马上按没反应是正常现象
  - 要有明显的轰鸣声，手摸网口旁边出风，才是有反应