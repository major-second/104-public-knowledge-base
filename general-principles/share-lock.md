很多时候不能两个东西同时操作一个东西，否则导致意想之外的结果
- 比如[[python/trivial-mistakes]]，[[numpy/basics]]提到的
  - 所以经常要使用[[copy-paste]]
- cpp中的问题：[[oo/copy]]可能使两个对象的指针类型的成员指向同一个，导致问题，[[2-4-cpp]]有考到
- 比如共享内存很容易出错
- 比如[[realsense-ros]]的`roslaunch`和[[python-wrapper]]中的不能同时使用
    - 否则报错`RuntimeError: xioctl(VIDIOC_S_FMT) failed Last Error: Device or resource busy`
- 比如apt装软件时不能同时跑多个

为了解决这个，可能需要加锁
- 典型是`.lock`文件，有了就说明某个东西锁着。程序中用该文件存不存在来判断
- 但又有可能错误地没删导致卡死，比如[[file-baton]]，[[mujoco-py]]中的
    - 这时当然需要手工删除`.lock`