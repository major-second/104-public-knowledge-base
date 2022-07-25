- 前置
  - [[docker/installation]]
  - 宿主机有[[ubuntu-nvidia-drivers]]
  - 了解[[software-management/source]]和[[systemd]]有助于理解本文档内容

[参考文档](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker)
对于官方文档一来的`Setting up Docker`一节，如果你已经[[docker/installation]]过，就可以省略
即：已经装过[[docker/installation]]的就从下面这里开始
```sh
distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
      && curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
      && curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list | \
            sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
            sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
sudo apt-get update
sudo apt-get install -y nvidia-docker2
sudo systemctl restart docker
```
测试安装是否成功
```sh
sudo docker run --rm --gpus all nvidia/cuda:<你想要的tag> nvidia-smi
# 一个可能的tag: `10.0-cudnn7-devel`
```
注：`all`可能还能替换成整数指定gpu个数（如`2`）
