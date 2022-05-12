前置：[[禁用nouveau]]，[[timeshift备份镜像]]

- 选择版本
  - nvidia大屑，官方推荐可能不对（可能黑屏），务必[[timeshift备份镜像]]！
  - 反而
`sudo apt install ubuntu-drivers-common`
`ubuntu-drivers devices`
推荐的版本很靠谱
    - 比如看到`nvidia-driver-470 - distro non-free recommended`
    - 那就`sudo apt install nvidia-driver-470`
- 重启，`nvidia-smi`，正常看到输出了
  - 注：还可以`watch nvidia-smi`每2秒输出一次，进行监测