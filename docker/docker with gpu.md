关于配置docker19使用gpu，其实只用装官方提供的toolkit即可，把github上的搬下来：
```sh
# Add the package repositories
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker
```
测试安装是否成功
```sh
docker run --help | grep -i gpus
```
运行gpu的容器
```sh
# 使用所有GPU
docker run --gpus all nvidia/cuda:9.0-base nvidia-smi
# 使用两个GPU
docker run --gpus 2 nvidia/cuda:9.0-base nvidia-smi
# 指定GPU运行
docker run --gpus '"device=1,2"' nvidia/cuda:9.0-base nvidia-smi
docker run --gpus '"device=UUID-ABCDEF,1"' nvidia/cuda:9.0-base nvidia-smi
```
