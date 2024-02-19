前置：
- [[linux-proxy-client]]翻墙
- 针对`raw.githubusercontent.com`修改[[hosts]]
  - 因为`rosdep init`的代理[[configure-proxy]]很麻烦
  - 具体地，参考[[dns]]，修改`/etc/hosts`即可。例如加入`185.199.108.133 raw.githubusercontent.com`（注意具体要加的ip不同时间可能不一样）
- [[package-managers-source]]
  - 除了需要加ros的源，可能还要改默认源为阿里云（默认源缺包）
## general explanations
- [[version]]
  - 这是`melodic`版本（比较古早）版本是按照字母`a`开始排列的
  - 注：版本不同，加的软件[[package-managers-source]]不同
    - `melodic`版本只能安装`ros-melodic-<名字>`，如果安装`ros-<其他版本>-<名字>`就会报找不着包
    - 所以[[read-doc]]时不能总是照搬命令
- steps
  - 参考[官网文档](http://wiki.ros.org/melodic/Installation/Ubuntu#Installation)，对着不断输入命令即可
  - 如果你用[[zsh]]那么，要`source`的文件以及需要把`source`语句加到的文件都有区别. So you should pay attention to this step in the document.
  - 注意1.5节中提到：多个ros版本只能`source`一个`setup.bash`
    - 那我们就认准`melodic`吧
  - `rosdep update`即使在有[[dns]]手动解析情况下也可能不成功。你反复多几次，在不断地[[non-determinism]]尝试中，可能就能集齐所有他要的东西（每一次可能都有几个`.yaml`不成功，但只要总和覆盖所有即可）
## 验证安装成功
一个终端`roscore`
另一个终端`rqt_graph`，去掉hide中的勾选，看到`/rosout`
![](installation-rqt-graph.png)