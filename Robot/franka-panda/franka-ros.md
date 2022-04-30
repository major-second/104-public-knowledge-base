前置
- 知道机械臂中软件版本号（比如可以[[connect-controller]]上去看）
- [[libfranka]]

步骤
- 参考[[libfranka]]. 有就直接`apt`装，没有就[[build-from-source]]
  - 可能需要参考[[create-catkin-ws]]，不过这里教程其实涵盖了create
- 总体看[这个](https://frankaemika.github.io/docs/installation_linux.html#building-the-ros-packages)，但是不能教条。参考[[read-doc]]
  - 版本不一定是`kinetic`
  - 过程中有一些转移目录的`cd`指令没写
  - 有些`/path/to`等需要自己填上