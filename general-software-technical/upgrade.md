# 更新的好处
- 大部分情况下，当然是新的好，参考[[version]]
  - 比如[[tesseract]]，新的识别率高
  - 比如`python3`高版本有[[f-string]]
  - 比如[[pip]]升级后才有一些高级的包，否则根本装不了新包
  - [[cpp-vector]] `emplace_back`（需要C++11）
# 更新的坏处
## 不再兼容
- 参考[[compatibility]]
- 不要随便`upgrade`，小心软件突然用不了！重要升级版本前请备份系统！参考[[timeshift]], [[version]], [[compatibility]]
  - 例子
    - 软件A和软件B同时依赖C，A依赖版本1-3，B依赖版本2-4
    - A依赖B，B依赖C
      - A要求版本2-4
      - 但C太老只能支持B的1-3
      - 即C的[[compatibility#forward]]向前兼容性不好
  - 总之：很多时候不是最新的就一定好。有时候要找交集
- 举例体验
  - 比如[[distutils]]提到的问题
  - 比如一些老旧网站（如时至2022.6中国电信网上营业厅）必须用ie模式打开才正常
    - Edge的setting里搜索`explorer`，打开一个设置
    - 之后右上角有这个按钮![](ie-mode.png)
  - 更多：参考[[version]]
- 如何避免
  - 正常的软件开发习惯是用`deprecated`提醒你这个feature可能过一段时间新版本就没了
    - 你要赶紧想办法（换掉那些不推荐你再使用的api等）
    - 否则之后就别随便更新！
  - 使用lts [[version]]，稳定，社区检验过，等等
    - 比如[[vscode]] 1.85 -> 1.86 时出现过[[remote-ssh]]无法连接（无法兼容很多服务器）的问题
    - 并且可能需[[settings-and-configurations]]确保不自动更新
- 解决思路：如参考[[apt-version]]可能有帮助，例如
  - 如果有刚刚说的现象（只有中间某些版本能用），那就`apt-cache madison <包名>`（例如尝试`apt-cache madison docker-ce`）
  - 把拿出来的字符串（比如`5:18.09.0~3-0~ubuntu-bionic`这种东西）拿去从高版本到低版本，一个一个试（比如`apt install docker-ce=5:18.09.0~3-0~ubuntu-bionic`），看什么时候行即可
  - 当然，不一定要一个一个试。[[binary-search]]等搜索方法也行
## 其他问题
- 有时旧版本才能破解，新版本不能
  - 参考[[aida64]], [[pricing]]
  - 乃至国行苹果手机不能使用不少[[apple-features]]（2022左右，铁拳监管越来越严）
- 所以可以保留一些旧版安装包
- 没看清楚更新需要强制[[refresh]]某些东西（比如重启），错误导致工作丢失