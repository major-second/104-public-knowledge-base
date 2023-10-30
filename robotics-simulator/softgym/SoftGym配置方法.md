# SoftGym配置方法
[git主页](https://github.com/Xingyu-Lin/softgym)
如果当前环境为Ubuntu 16.04 LTS以及CUDA 9.2，则按照主页进行配置
由于当前大多数环境不满足上述要求，此处主要介绍使用docker的配置方法
## 准备
- `git clone https://github.com/Xingyu-Lin/softgym.git`
- 并完成[[docker/installation]]，[[nvidia-docker]]，[[conda-installation]]
- `sudo docker pull xingyu/softgym`获得配置好的[[docker/image]]
## 环境配置部分

先执行

```
xhost +
```

以授予容器内用户使用显示器的权限

之后执行

```
sudo nvidia-docker run \
  -v /home/yourong/softgym:/home/yourong/softgym \
  -v /home/yourong/anaconda3/:/home/yourong/anaconda3/ \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  --gpus all \
  -e DISPLAY=$DISPLAY \
  -e QT_X11_NO_MITSHM=1 \
  -it xingyu/softgym:latest bash
```

进入docker环境，此处-v意味需要链接到docker容器的文件夹，例如这里需要anaconda文件夹和softgym文件夹，**注意填写绝对路径**

由于docker中的bashrc不具有一些库的路径，需要手动添加路径，例如

```
export PATH=/home/yourong/anaconda3/bin:$PATH
```

如此便可正常使用conda来创建环境，并且安装[[pybind11]]

```
conda install pybind11
```

**如果此步耗时过久，尝试切换下载源**

进入softgym文件夹并执行以进行路径添加

```
. prepare_1.0.sh
```

最后进行编译

```
. ./prepare_1.0.sh && ./compile_1.0.sh
```

编译成功后即可进行模拟器的运行

## 太长不看版

如果使用104的3090进行softgym实验

依次运行

```
xhost +

sudo nvidia-docker run \
  -v /home/yourong/softgym:/home/yourong/softgym \
  -v /home/yourong/anaconda3/:/home/yourong/anaconda3/ \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  --gpus all \
  -e DISPLAY=$DISPLAY \
  -e QT_X11_NO_MITSHM=1 \
  -it xingyu/softgym:latest bash

export PATH=/home/yourong/anaconda3/bin:$PATH

. prepare_1.0.sh

. activate softgym
```

