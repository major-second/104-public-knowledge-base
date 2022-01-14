# 查找和解决Vulkan错误
如果成功打开了isaac sim，但是viewport没有显示（全灰），那有可能是Vulkan出错
## 2022.1.14更新
现在新版本Isaac，如果Vulkan出问题，会在安装时及时报错，而不是之后viewport看不到。
解决方法也有了[官方指南](https://docs.omniverse.nvidia.com/app_isaacsim/prod_kit/linux-troubleshooting.html#q3-how-to-verify-a-correct-vulkan-setup-with-vulkaninfo-or-vulkaninfosdk-utility)
即下载安装最新Vulkan SDK，而不要`apt install`一堆东西。
## 自我总结问答
0. Q: 这样问问题好吗？!
![](installation/question.png)
A: 我们先不吐槽垃圾英语和语法错误了。首先这截图，别人不方便查。其次明明完整的错误提示（日志）有很多关键信息都没放进来（事实上，这个错误是Vulkan出错的结果。光看这个根本看不出根本原因。而Vulkan那个错谷歌一下能解决）。