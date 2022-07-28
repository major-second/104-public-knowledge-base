- `pip`本身来源：
  - linux
    - `python3`：`apt install python3-pip`
        - 此时`pip3 --version`查看版本
        - `pip --version`一下发现也在`/usr/lib/python3`而不在`python2.7`
          - 和`apt install python-pip`结果完全不同
        - `pip3 install --upgrade pip`做[[software-management/upgrade]]
    - `python2`：`apt install python-pip`
  - windows：[官网下载](https://www.python.org/downloads/windows/)安装时可选
- 普通使用：直接`pip install 包名`
- 从源码安装python包（比如需要指定版本，比如conda和pip都找不到包时）
    - clone源码，进去
    - `pip install -e .`
    - 此时`pip list`可以看到有的包是在本地某个源码文件夹装的
- 批量安装依赖
  1. 原生方法：有个`requirements.txt`里面一行一行写需要什么包，该文件内容形如
`gym==0.19`
`termcolor`
    - 然后`pip install -r requirements.txt`即可
    - 注：`requirements.txt`有时还能看到`git`开头的一些行，表示一些从git下载源码安装的包
  2. 和conda结合：[[create-env-yaml]]中的`dependencies - pip`子树
    - 当然为了更加保险，`dependencies`子树中可以增加`python=版本`和`pip=版本`
- 一般来说`pip`效率不如`conda`，但有些`pip`有的包`conda`没有，有些包`pip`才有较新版本
  - 所以`pip`简单来说就是质量差，东西多
- 当然，`pip install`得到的包有时需要一些更底层的依赖。也就是python包只是一些上层接口而已
  - 其实这个有点像vscode插件和python解释器的关系，参见[[extensions/general]]
  - 比如[[mujoco-py]]中的mujoco
  - 比如[[mpi4py]]中需要
    - linux先`sudo apt install libopenmpi-dev`使得有`mpi.h`头文件等
    - windows可以搜索安装microsoft mpi![](microsoft-mpi.png)