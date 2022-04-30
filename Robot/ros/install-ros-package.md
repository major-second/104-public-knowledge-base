前置：
- [[create-catkin-ws]]
- [[ros/installation]]

步骤
- 举例体会：比如[[franka-ros]]的安装流程（具体参考[[franka-ros]]）
- 装多个package，头尾不变，中间`git clone`多一些，参考[[moveit]]
  - 也就是准备许多源码一起make
- 安装之后，为了省事，应当在你的`~/.bashrc`末尾加上`source <路径>/devel/setup.bash`，否则之后每次想用你自己的命令前都要`source devel/setup.sh`
  - 当然[[zsh]]就对应改成zsh