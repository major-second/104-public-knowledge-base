前置：
- [[sudo]]权限
- 了解[[package-managers-source]]
- 为了更好理解指令内容，可以看
  - [[tee命令]]
  - [[11-basic-scripting-partA]]的“命令替换”

[官方文档](https://docs.docker.com/engine/install/ubuntu/#installation-methods)
- 安装所需命令
```sh
sudo apt-get install -y ca-certificates curl gnupg lsb-release; \
sudo mkdir -p /etc/apt/keyrings; \
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg; \
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null; \
sudo apt-get update; \
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
```
- 过程中可能重启某些重要服务，因此会在终端给出提示。按提示操作即可
- 注意：请保证网络畅通，中途需要`curl`东西设置[[package-managers-source]]
- 验证安装成功：`sudo docker run hello-world`
  - 此时会自动下载`hello-world`这个[[docker/image]]，并自动创建运行[[container]]
  - 输出`Hello from Docker!`等