- 前置
  - 了解[[vpn]], [[proxy-basics]]
    - 最好有一个能翻墙的[[vpn]]，而不是[[proxy-basics]]，否则很麻烦
  - [[temp-solution]]
  - [[windows/env-var]]
# 过程
- 请先阅读参考！
  - [微软官方教程](https://support.microsoft.com/zh-cn/windows/%E5%9C%A8-windows-%E4%B8%8A%E5%AE%89%E8%A3%85%E7%A7%BB%E5%8A%A8%E5%BA%94%E7%94%A8%E5%92%8Camazon-appstore-f8d0abb5-44ad-47d8-b9fb-ad6b1459ff6c)
    - 里面有讲到支持的地区，这可以作为参考让你选择[[vpn]]
  - [知乎教程](https://zhuanlan.zhihu.com/p/424959704)，进一步讲了安装自己的apk的方法等，这样就可以用[[download-resource]]中的apkpure等
  - [安装自己apk（adb调试）参考](https://www.jianeryi.com/1346.html)
- 过程中有时出玄学问题需要[[refresh]]重启
- 用[[vpn]]而不是[[proxy-basics]]上网
  - 其实[[proxy-basics]]也可以但是可能操作更复杂，因为[[configure-proxy]]是需要应用主动去用
  - [[vpn]]可能是[[temp-solution]]，因为可能进到了wsa系统里又会提示因为安全原因不让你用[[vpn]]
- `Microsoft Store`搜索`Amazon Appstore`
  - 下载安装
  - 登录Amazon账号
  - 然后可以在Amazon中下载已有应用
- 或参考[知乎教程](https://zhuanlan.zhihu.com/p/424959704)装第三方（需要开发者模式）
  - 需要下载解压 [platform tools](https://developer.android.com/studio/releases/platform-tools#downloads.html)
  - 设置[[windows/env-var]]等
  - 这时：推荐先安装apkpure之类的应用商店，参考[[download-resource]]
    - 然后就可以用应用商店下载安装应用
    - 无论国内[[wechat-tips]]还是国外软件都行
    - 这是[[temp-solution]]思想。只需要`adb`比较麻烦地装一次，后面即可都用应用商店
# 结果
- 对于[[wechat-tips]]，使用发朋友圈、发名片等只能用安卓的功能
- 进行自动化（如游戏、薅羊毛签到）等
- 大材小用，高速，大屏，非常流畅
  - 敏感羞羞网站/应用等，使用电脑高速大屏，爽
    - 直接用应用商店搜索下载即可
    - 安卓中代理怎么用参考后文
- 浏览器
  - 由于google play问题，很多都用不了
    - 参考[[huawei-google]]
  - `Opera`时至2022.12确认能用
  - 可用于确认[[configure-proxy]]成功
# 管理
- 开始菜单 - WSA Settings
- 可能用到的
  - system：文件，关闭 Advanced Networking（如后文）等
  - developer：需要打开！否则没法自己安装应用，设置代理等
  - compatibility：可以看应用列表，设置兼容性让没法用键盘的变得可用等等
# 代理[[configure-proxy]]
- 时至2022.12，必须关闭WSA Settings - Advanced Networking，否则很容易造成神秘问题
- 使用主机代理的方法
  - 主机[[powershell]]
  - 需要
    - [[wsl]]
    - WSA Settings打开开发者模式开启`58526`
    - `adb connect 127.0.0.1:58526`
  - 设置
    - `$WinNetIP=$(Get-NetIPAddress -InterfaceAlias 'vEthernet (WSL)' -AddressFamily IPV4)`
    - `$Port=7890 #7890换成你自己的代理端口`
    - 然后[[CRUD]]
      - `adb shell settings put global http_proxy "$($WinNetIP.IPAddress):$Port"; adb shell settings put global https_proxy "$($WinNetIP.IPAddress):$Port"`
      - `adb shell settings put global http_proxy :0; adb shell settings put global https_proxy :0`
      - `adb shell settings get global http_proxy; adb shell settings get global https_proxy`
# 局限性
- 不能用google play，所以一些应用用不了
  - [[huawei-google]]也不行
- 打微信电话有回声
  - 不像原生的安卓/windows微信电话能检测消除回声
- 电脑开一些[[vpn]]时，wsa会认为你不安全，不给你上网