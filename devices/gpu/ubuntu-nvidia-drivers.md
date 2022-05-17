前置：[[禁用nouveau]]，[[timeshift]]

- 选择版本
  - nvidia大屑，官方推荐可能不对（可能黑屏），务必[[timeshift]]备份
  - 反而
`sudo apt install ubuntu-drivers-common`
`ubuntu-drivers devices`
推荐的版本很靠谱
    - 比如看到`nvidia-driver-470 - distro non-free recommended`
    - 那就`sudo apt install nvidia-driver-470`
- 重启，`nvidia-smi`，正常看到输出了
  - 注：还可以`watch nvidia-smi`每2秒输出一次，进行监测
  - 注：结合[[regex]]，可以有<code>watch "nvidia-smi | grep '[4-7]&nbsp;&nbsp;Tesla'"</code>这种操作，只看部分卡
    - 注意引号，注意空格个数